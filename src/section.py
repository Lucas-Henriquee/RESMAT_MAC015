from .all_imports import *
from .node import NodeManager

class Section:
    def __init__(self):
        self.node_manager = NodeManager()
        self.main_figure = None  
        self.cut_figures = [] 

    def create_main_figure(self, figure_type, data):
        self.node_manager.clear_nodes()  
        self.main_figure = [] 

        if figure_type == "retangulo":
            width, height = data
            self.main_figure = self._create_rectangle(width, height) 

        elif figure_type == "triangulo":
            base, height = data
            self.main_figure = self._create_triangle(base, height)  

        elif figure_type == "circulo":
            radius = data
            self.main_figure = self._create_circle(cx=0, cy=0, radius=radius) 

        else:
            raise ValueError("Tipo de figura inválido.")

    def _create_rectangle(self, width, height):

        nodes = [
            (0, 0),
            (width, 0), 
            (width, height),  
            (0, height)  
        ]
        return self._add_nodes(nodes)

    def _create_triangle(self, base, height):
        nodes = [
            (0, 0),
            (base, 0),  
            (base / 2, height)  
        ]
        return self._add_nodes(nodes)

    def _create_circle(self, cx=0, cy=0, radius=0):
        node = self.node_manager.add_node(cx, cy, radius=radius)  
        return [self.node_manager.get_node(node)]  

    def force_counterclockwise(self, polygon):
            area = 0
            for i in range(len(polygon)):
                x1, y1 = polygon[i]
                x2, y2 = polygon[(i + 1) % len(polygon)]
                area += (x2 - x1) * (y2 + y1)

            if area > 0: 
                polygon.reverse()
            
            return polygon
    
    def _create_polygon(self, coordinates):
        nodes = []
        for x, y in coordinates:
            existing_node = self.node_manager.get_node_by_coordinates(x, y)
            if existing_node:
                nodes.append(existing_node)
            else:
                name = self.node_manager.add_node(x, y)
                nodes.append(self.node_manager.get_node(name))

        if len(nodes) >= 3:
            points = [(node.x, node.y) for node in nodes]
            if not self._is_counterclockwise(points):
                nodes.reverse()

        return nodes

    def _calculate_circle_intersection_area(self, cx, cy, radius, main_polygon):
        circle_shape = Point(cx, cy).buffer(radius)

        main_shape = Polygon(main_polygon)

        intersection = main_shape.intersection(circle_shape)

        return intersection.area

    def _calculate_intersection_area(self, main_coords, cut_coords, cut_circle=None):

        intersection_polygon = []

        def shoelace_area(polygon):
            if len(polygon) < 3:
                return 0.0 
            
            x, y = zip(*polygon) 
            return abs(sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(polygon)))) / 2

        if cut_circle:
            cx, cy, radius = cut_circle  

            num_points = 100

            if radius is None:
                return 0.0 
    
            circle_coords = [(cx + radius * np.cos(theta), cy + radius * np.sin(theta)) for theta in np.linspace(0, 2*np.pi, num_points)]
            circle = Polygon(circle_coords)

            main_polygon = Polygon(main_coords)

            intersection = main_polygon.intersection(circle)

            if intersection.is_empty:
                return 0.0 

            if isinstance(intersection, Polygon):
                area = intersection.area
            elif isinstance(intersection, MultiPolygon):
                area = sum(poly.area for poly in intersection.geoms)
            else:
                area = 0.0

            if area == 0.0:
                return (np.pi * radius ** 2) / 2

            return area

        else:

            def sutherland_hodgman(subject_polygon, clip_polygon):
                def inside(p, edge_start, edge_end):
                    
                    result = (edge_end[0] - edge_start[0]) * (p[1] - edge_start[1]) > (edge_end[1] - edge_start[1]) * (p[0] - edge_start[0])
                    return result

                def compute_intersection(p1, p2, edge_start, edge_end):
                    x1, y1 = p1
                    x2, y2 = p2
                    x3, y3 = edge_start
                    x4, y4 = edge_end

                    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
                    if denom == 0:
                        return None  

                    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
                    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

                output_list = subject_polygon

                for i in range(len(clip_polygon)):
                    edge_start = clip_polygon[i]
                    edge_end = clip_polygon[(i + 1) % len(clip_polygon)]
                    input_list = output_list
                    output_list = []

                    if len(input_list) == 0:
                        break  

                    s = input_list[-1]
                    for e in input_list:
                        if inside(e, edge_start, edge_end):
                            if not inside(s, edge_start, edge_end):
                                inter = compute_intersection(s, e, edge_start, edge_end)
                                if inter:
                                    output_list.append(inter)
                            output_list.append(e)
                        elif inside(s, edge_start, edge_end):
                            inter = compute_intersection(s, e, edge_start, edge_end)
                            if inter:
                                output_list.append(inter)
                        s = e

                if len(output_list) == 0:
                    if all(self._point_inside_polygon(p, main_coords) for p in cut_coords):
                        return cut_coords  

                    return []  

                return output_list 

            if not self._is_counterclockwise(main_coords):
                main_coords.reverse()

            def ordenar_pontos(pontos, _is_counterclockwise):
                
                cx = sum(p[0] for p in pontos) / len(pontos)
                cy = sum(p[1] for p in pontos) / len(pontos)
                
                pontos_ordenados = sorted(pontos, key=lambda p: atan2(p[1] - cy, p[0] - cx))
                
                if not _is_counterclockwise(pontos_ordenados):
                    pontos_ordenados.reverse()

                return pontos_ordenados



            cut_coords = ordenar_pontos(cut_coords, self._is_counterclockwise)


            intersection_polygon = sutherland_hodgman(main_coords, cut_coords)

            if len(intersection_polygon) < 3:
                if all(self._point_inside_polygon(p, main_coords) for p in cut_coords):
                    return self._shoelace_area(cut_coords), cut_coords

                return 0.0, []


            if not intersection_polygon:

                if all(self._point_inside_polygon(p, main_coords) for p in cut_coords):
                    return self._shoelace_area(cut_coords), cut_coords

                return 0.0, [] 


            if cut_circle is not None:
                return area if area > 0 else 0, []

            if intersection_polygon:
                intersection_polygon = self.force_counterclockwise(intersection_polygon)
                area = shoelace_area(intersection_polygon)
            return area, intersection_polygon

    def _add_nodes(self, nodes):
        node_list = []
        for x, y, *radius in nodes:
            existing_node = self.node_manager.get_node_by_coordinates(x, y)
            if existing_node:
                node_list.append(existing_node)
            else:
                name = self.node_manager.add_node(x, y, radius=radius[0] if radius else None)
                node_list.append(self.node_manager.get_node(name))
        return node_list

    def add_cut_figure(self, figure_type, coordinates):
        if not self.main_figure:
            raise ValueError("Nenhuma figura principal foi definida.")

        if figure_type == "retangulo":
            cut_figure = self._create_polygon(coordinates)
        elif figure_type == "triangulo":
            cut_figure = self._create_polygon(coordinates)
        elif figure_type == "circulo":
            cx, cy, radius = coordinates
            cut_figure = self._create_circle(cx, cy, radius)
        else:
            raise ValueError("Tipo de figura inválido para recorte.")

        main_coords = [(node.x, node.y) for node in self.main_figure]
        cut_figure = [node for node in cut_figure if self._point_inside_polygon((node.x, node.y), main_coords)]

        if not cut_figure:
            return

        if self._is_cut_valid(cut_figure):
            self.cut_figures.append(cut_figure)
        else:
            raise ValueError("A figura de corte deve estar pelo menos parcialmente dentro da figura principal e não sobrepor cortes existentes.")

    def _is_cut_valid(self, cut_figure):
        main_coords = [(node.x, node.y) for node in self.main_figure]
        cut_coords = []
        cut_circle = None  

        for node in cut_figure:
            if hasattr(node, "radius") and node.radius is not None:
                cut_circle = (node.x, node.y, node.radius)
            else:
                cut_coords.append((node.x, node.y))

        if cut_circle:
            cx, cy, r = cut_circle
            if self._circle_intersects_polygon(cx, cy, r, main_coords):
                return True
            else:
                return False

        inside_main = any(self._point_inside_polygon((x, y), main_coords) for x, y in cut_coords)

        if not inside_main:
            return False

        intersected_area, _ = self._calculate_intersection_area(main_coords, cut_coords, cut_circle)

        if intersected_area > 0:
            return True

        if all(self._point_inside_polygon(p, main_coords) for p in cut_coords):
            return True

        return False

    def _circle_intersects_polygon(self, cx, cy, r, polygon):
        if self._point_inside_polygon((cx, cy), polygon):
            return True

        num_samples = 200 
        for angle in np.linspace(0, 2 * np.pi, num_samples):
            x = cx + r * np.cos(angle)
            y = cy + r * np.sin(angle)
            if self._point_inside_polygon((x, y), polygon):
                return True

        main_polygon = Polygon(polygon)
        circle = Point(cx, cy).buffer(r)

        if circle.intersects(main_polygon):
            return True

        for px, py in polygon:
            if (px - cx) ** 2 + (py - cy) ** 2 <= r ** 2:
                return True
        return False

    def _clip_polygon(self, cut_x, cut_y, main_coords):
        cut_polygon = list(zip(cut_x, cut_y))
        main_polygon = main_coords
        clipped_polygon = []

        if len(cut_polygon) == 3:  
            cut_polygon = self._clip_triangle(cut_polygon, main_polygon)

        result = self._calculate_intersection_area(main_polygon, cut_polygon)
        if isinstance(result, tuple):
            area, clipped_polygon = result
        else:
            area, clipped_polygon = result, []

        if not clipped_polygon or len(clipped_polygon) < 3:
            return None

        return clipped_polygon
    
    def _clip_circle(self, circle, main_polygon):
        cx, cy, r = circle
        circle_points = self._generate_circle_points(cx, cy, r) 

        clipped_circle = [p for p in circle_points if self._point_inside_polygon(p, main_polygon)]

        return clipped_circle

    def _clip_triangle(self, triangle, main_polygon):
        return self._sutherland_hodgman(triangle, main_polygon)

    def _circle_inside_polygon(self, cx, cy, r, polygon):
        num_samples = 100 

        for angle in np.linspace(0, 2 * np.pi, num_samples):
            x = cx + r * np.cos(angle)
            y = cy + r * np.sin(angle)
            if self._point_inside_polygon((x, y), polygon):
                return True

        if self._point_inside_polygon((cx, cy), polygon):
            return True

        circle = Point(cx, cy).buffer(r) 
        main_polygon = Polygon(polygon)  

        if circle.intersects(main_polygon):
            return True  

        return False

    def _point_inside_polygon(self, point, polygon):
        x, y = point
        n = len(polygon)
        inside = False

        p1x, p1y = polygon[0]
        for i in range(n + 1):
            p2x, p2y = polygon[i % n]

            if (p1x == p2x and x == p1x and min(p1y, p2y) <= y <= max(p1y, p2y)) or \
            (p1y == p2y and y == p1y and min(p1x, p2x) <= x <= max(p1x, p2x)):
                return True  

            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside

    def list_figures(self):

        main_nodes = [f"{node.name}: ({node.x}, {node.y})" for node in self.main_figure] if self.main_figure else []
        cut_nodes = []
        for i, figure in enumerate(self.cut_figures, 1):
            cut_nodes.extend([f"Recorte {i} - {node.name}: ({node.x}, {node.y})" for node in figure])

        return {"Main Figure": main_nodes, "Cut Figures": cut_nodes}

    def draw_section(self, ax):

        if not self.main_figure:
            raise ValueError("Nenhuma figura principal foi definida.")
        
        ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.axvline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.grid(color='lightgray', linestyle='--', linewidth=0.5, alpha=0.7)

        all_x = []
        all_y = []

        self._draw_figure(ax, self.main_figure, color='blue', hatch=None, label="Figura Principal")
        all_x.extend([node.x for node in self.main_figure])
        all_y.extend([node.y for node in self.main_figure])

        for i, cut_figure in enumerate(self.cut_figures, start=1):
            self._draw_figure(ax, cut_figure, color='red', hatch='//', label="Figuras Cortadas", index=i)
            all_x.extend([node.x for node in cut_figure])
            all_y.extend([node.y for node in cut_figure])

        if len(self.main_figure) == 1 and hasattr(self.main_figure[0], "radius"):
            circle = self.main_figure[0]
            radius = circle.radius
            all_x.extend([circle.x - radius, circle.x + radius])
            all_y.extend([circle.y - radius, circle.y + radius])

        if all_x and all_y:
            x_min, x_max = min(all_x), max(all_x)
            y_min, y_max = min(all_y), max(all_y)
            margin = min(max(x_max - x_min, y_max - y_min) * 0.05, 2)  
            ax.set_xlim(x_min - margin, x_max + margin)
            ax.set_ylim(y_min - margin, y_max + margin)
            ax.set_aspect('equal')


        ax.set_xlabel("Coordenada X")
        ax.set_ylabel("Coordenada Y")
        ax.legend(loc='upper right', fontsize=8)

    def _draw_figure(self, ax, nodes, color, hatch, label, index=None):

        if nodes is self.main_figure and len(nodes) == 1 and hasattr(nodes[0], "radius"):
            node = nodes[0]
            cx, cy, radius = node.x, node.y, node.radius
            self._draw_circle(ax, cx, cy, radius, color, hatch, label, index)

        elif len(nodes) == 1 and hasattr(nodes[0], "radius"):
            node = nodes[0]
            cx, cy, radius = node.x, node.y, node.radius
            self._draw_circle(ax, cx, cy, radius, color, hatch, None, index) 

        else:
            self._draw_polygon(ax, nodes, color, hatch, None, index)  

        if len(nodes) == 1 and hasattr(nodes[0], "radius"):
            node = nodes[0]
            cx, cy = node.x, node.y
        else:
            x_coords = [node.x for node in nodes]
            y_coords = [node.y for node in nodes]
            cx, cy = sum(x_coords) / len(x_coords), sum(y_coords) / len(y_coords)  

        if index is not None:
            ax.text(cx, cy, f"Corte {index}", ha='center', va='center', fontsize=10, color='black', weight='bold')

    def _draw_circle(self, ax, cx, cy, radius, color, hatch, label, index=None):
        main_coords = [(node.x, node.y) for node in self.main_figure]
        main_polygon = Polygon(main_coords)
        circle_shape = Point(cx, cy).buffer(radius)

        intersection = main_polygon.intersection(circle_shape)

        if intersection.is_empty:
            return 

        x, y = intersection.exterior.xy
        ax.fill(x, y, facecolor=color, edgecolor='black', alpha=0.5, hatch=hatch, label=label)

    def _draw_polygon(self, ax, nodes, color, hatch, label, index=None):
        x_coords = [node.x for node in nodes]
        y_coords = [node.y for node in nodes]

        x_coords.append(x_coords[0])  
        y_coords.append(y_coords[0])

        main_coords = [(node.x, node.y) for node in self.main_figure]
        intersected_area, intersected_polygon = self._calculate_intersection_area(main_coords, [(node.x, node.y) for node in nodes])

        if not isinstance(intersected_polygon, list) or len(intersected_polygon) == 0:
            if nodes is not self.main_figure: 
                return
            intersected_polygon = [(node.x, node.y) for node in self.main_figure] 

        if not intersected_polygon or len(intersected_polygon) < 3:
            return 

        if intersected_polygon:
            x_int, y_int = zip(*intersected_polygon)
            ax.fill(x_int, y_int, color=color, alpha=0.5, edgecolor='black', hatch=hatch, label=label)

            if index is not None:
                centroid_x = sum(x_int) / len(x_int)
                centroid_y = sum(y_int) / len(y_int)
                ax.text(centroid_x, centroid_y, f"Corte {index}", ha='center', va='center', fontsize=10, color='black', weight='bold',
                        bbox=dict(facecolor='white', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.3'))

    def _is_counterclockwise(self, points):
 
        sum_edges = 0
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]
            sum_edges += (x2 - x1) * (y2 + y1)

        return sum_edges < 0 