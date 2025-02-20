from .all_imports import *
from .section import Section
from .node import Node

def calculate_moments(section: Section):
    if not section.main_figure:
        raise ValueError("Nenhuma figura principal definida.")

    I_x, I_y, I_xy = 0, 0, 0
    total_area = 0

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

    results = [
        f"Principal  |  Área: {area_main:.2f}  |  x̄: {x_bar_main:.2f}  |  ȳ: {y_bar_main:.2f}  |  "
        f"I_x: {I_x:.2f}  |  I_y: {I_y:.2f}  |  I_xy: {I_xy:.2f}"
    ]

    for idx, cut_figure in enumerate(section.cut_figures, 1):

        if isinstance(cut_figure[0], Node) and getattr(cut_figure[0], "radius", None) is not None:
            cx, cy, r = cut_figure[0].x, cut_figure[0].y, cut_figure[0].radius

            intersec_area = section._calculate_intersection_area(main_coords, [(cx, cy)], cut_circle=(cx, cy, r))

            if intersec_area > 0:
                x_bar_cut = cx
                y_bar_cut = cy + (4 * r) / (3 * np.pi) 

                I_xx_cut = (np.pi * r**4) / (8 if intersec_area < np.pi * r**2 else 4)
                I_yy_cut = I_xx_cut
                I_xy_cut = 0  

                I_x -= I_xx_cut + intersec_area * y_bar_cut**2
                I_y -= I_yy_cut + intersec_area * x_bar_cut**2
                I_xy -= I_xy_cut + intersec_area * x_bar_cut * y_bar_cut
                total_area -= intersec_area

                results.append(
                    f"Corte {idx}  |  Área: {-intersec_area:.2f}  |  x̄: {x_bar_cut:.2f}  |  ȳ: {y_bar_cut:.2f}  |  "
                    f"I_x: {I_x:.2f}  |  I_y: {I_y:.2f}  |  I_xy: {I_xy:.2f}"
                )

        else:
            cut_coords = [(node.x, node.y) for node in cut_figure]

            area_cut, x_bar_cut, y_bar_cut, I_xx_cut, I_yy_cut, I_xy_cut = polygon_moments(cut_coords)
               
            if len(cut_coords) == 3: 
                x_bar_cut = sum(p[0] for p in cut_coords) / 3
                y_bar_cut = sum(p[1] for p in cut_coords) / 3
                I_xy_cut = (area_cut * x_bar_cut * y_bar_cut) / 2  

            elif len(cut_coords) == 4: 
                x_bar_cut = (cut_coords[0][0] + cut_coords[2][0]) / 2
                y_bar_cut = (cut_coords[0][1] + cut_coords[2][1]) / 2
                I_xy_cut = 0  

            if area_cut > 0:
                I_x -= I_xx_cut + area_cut * y_bar_cut**2
                I_y -= I_yy_cut + area_cut * x_bar_cut**2
                I_xy -= I_xy_cut + area_cut * x_bar_cut * y_bar_cut
                total_area -= area_cut

                results.append(
                    f"Corte {idx}  |  Área: {-area_cut:.2f}  |  x̄: {x_bar_cut:.2f}  |  ȳ: {y_bar_cut:.2f}  |  "
                    f"I_x: {I_x:.2f}  |  I_y: {I_y:.2f}  |  I_xy: {I_xy:.2f}"
                )

    if total_area != 0:
        x_bar_final = (
            (area_main * x_bar_main) +
            sum(-area_cut * x_bar_cut for cut_figure in section.cut_figures
                for area_cut, x_bar_cut, _, _, _, _ in [polygon_moments([(node.x, node.y) for node in cut_figure])])
        ) / total_area

        y_bar_final = (
            (area_main * y_bar_main) +
            sum(-area_cut * y_bar_cut for cut_figure in section.cut_figures
                for area_cut, _, y_bar_cut, _, _, _ in [polygon_moments([(node.x, node.y) for node in cut_figure])])
        ) / total_area
    else:
        x_bar_final, y_bar_final = 0, 0  

    results.append(
        f"Total  |  Área: {total_area:.2f}  |  x̄: {x_bar_final:.2f}  |  ȳ: {y_bar_final:.2f}  |  "
        f"I_x: {I_x:.2f}  |  I_y: {I_y:.2f}  |  I_xy: {I_xy:.2f}"
    )

    results.append("* Todos os valores estão em unidades consistentes conforme o sistema de entrada.")

    return results