from .all_imports import *
from .section import Section
from .node import Node

def calculate_moments(section: Section):
    if not section.main_figure:
        raise ValueError("Nenhuma figura principal definida.")

    I_x, I_y, I_xy = 0, 0, 0
    total_area = 0
    cut_moments = []  

    def polygon_moments(coords):
        n = len(coords)
        area = 0
        I_xx, I_yy, I_xy = 0, 0, 0
        Cx, Cy = 0, 0

        for i in range(n):
            x0, y0 = coords[i]
            x1, y1 = coords[(i + 1) % n]
            common = x0 * y1 - x1 * y0

            area += common
            I_xx += (y0**2 + y0 * y1 + y1**2) * common
            I_yy += (x0**2 + x0 * x1 + x1**2) * common
            I_xy += (x0 * y1 + 2 * x0 * y0 + 2 * x1 * y1 + x1 * y0) * common
            Cx += (x0 + x1) * common
            Cy += (y0 + y1) * common

        area *= 0.5
        I_xx /= 12.0
        I_yy /= 12.0
        I_xy /= 24.0

        if abs(area) < 1e-9:
            area = max(abs(area), 1e-6) 

        Cx /= (6 * area)
        Cy /= (6 * area)

        return abs(area), Cx, Cy, I_xx, I_yy, I_xy

    main_coords = [(node.x, node.y) for node in section.main_figure]
    area_main, x_bar_main, y_bar_main, I_xx_main, I_yy_main, I_xy_main = polygon_moments(main_coords)

    I_x += I_xx_main + area_main * y_bar_main**2
    I_y += I_yy_main + area_main * x_bar_main**2
    I_xy += I_xy_main + area_main * x_bar_main * y_bar_main
    total_area += area_main

    for idx, cut_figure in enumerate(section.cut_figures, 1):

        if isinstance(cut_figure[0], Node) and getattr(cut_figure[0], "radius", None) is not None:
            cx, cy, r = cut_figure[0].x, cut_figure[0].y, cut_figure[0].radius

            intersec_area = section._calculate_intersection_area(main_coords, [(cx, cy)], cut_circle=(cx, cy, r))

            if intersec_area > 0:
                x_bar_cut = cx
                y_bar_cut = cy + (4 * r) / (3 * np.pi) 

                if intersec_area == np.pi * r**2:  
                    I_xx_cut = (np.pi * r**4) / 4
                else:  
                    I_xx_cut = (np.pi * r**4) / 8  

                I_yy_cut = I_xx_cut

                I_xy_cut = 0  

                I_x -= (I_xx_cut + intersec_area * y_bar_cut**2) if intersec_area > 0 else 0
                I_y -= (I_yy_cut + intersec_area * x_bar_cut**2) if intersec_area > 0 else 0
                I_xy -= (I_xy_cut + intersec_area * x_bar_cut * y_bar_cut) if intersec_area > 0 else 0

                total_area -= intersec_area

                cut_moments.append((intersec_area, x_bar_cut, y_bar_cut, I_xx_cut, I_yy_cut, I_xy_cut))

        else:
            cut_coords = [(node.x, node.y) for node in cut_figure]

            area_cut, x_bar_cut, y_bar_cut, I_xx_cut, I_yy_cut, I_xy_cut = polygon_moments(cut_coords)

            if area_cut > 0:
                I_x -= I_xx_cut + area_cut * y_bar_cut**2
                I_y -= I_yy_cut + area_cut * x_bar_cut**2
                I_xy -= I_xy_cut + area_cut * x_bar_cut * y_bar_cut
                total_area -= area_cut

                cut_moments.append((area_cut, x_bar_cut, y_bar_cut, I_xx_cut, I_yy_cut, I_xy_cut))

    if total_area != 0:
        x_bar_final = (area_main * x_bar_main - sum(area * x_bar for area, x_bar, _, _, _, _ in cut_moments)) / total_area
        y_bar_final = (area_main * y_bar_main - sum(area * y_bar for area, _, y_bar, _, _, _ in cut_moments)) / total_area
    else:
        x_bar_final, y_bar_final = 0, 0  

    results = [I_x, I_y, I_xy, x_bar_final, y_bar_final]

    return results
