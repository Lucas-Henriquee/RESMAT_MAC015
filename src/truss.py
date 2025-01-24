from .all_imports import *

def solve_truss(nodes, bars, supports):

    node_map = {node.name: (node.x, node.y) for node in nodes}

    num_nodes = len(nodes)
    num_bars = len(bars)

    A = np.zeros((2 * num_nodes, num_bars)) 
    forces = np.zeros(2 * num_nodes)         

    for i, node in enumerate(nodes):
        forces[2 * i] = sum(force.x for force in node.forces)  
        forces[2 * i + 1] = sum(force.y for force in node.forces)  

    for j, bar in enumerate(bars):
        start_coords = node_map[bar.start_node]
        end_coords = node_map[bar.end_node]

        length = ((end_coords[0] - start_coords[0])**2 + (end_coords[1] - start_coords[1])**2) ** 0.5
        cos_theta = (end_coords[0] - start_coords[0]) / length
        sin_theta = (end_coords[1] - start_coords[1]) / length

        start_idx = nodes.index(next(node for node in nodes if node.name == bar.start_node))
        end_idx = nodes.index(next(node for node in nodes if node.name == bar.end_node))

        A[2 * start_idx, j] = cos_theta
        A[2 * start_idx + 1, j] = sin_theta
        A[2 * end_idx, j] = -cos_theta
        A[2 * end_idx + 1, j] = -sin_theta

    for support in supports:
        node_idx = nodes.index(next(node for node in nodes if node.name == support.node))
        if support.support_type == 1:  
            A[2 * node_idx + 1, :] = 0
            A[2 * node_idx + 1, node_idx] = 1
            forces[2 * node_idx + 1] = 0
        elif support.support_type == 2:  
            A[2 * node_idx, :] = 0
            A[2 * node_idx + 1, :] = 0
            A[2 * node_idx, node_idx] = 1
            A[2 * node_idx + 1, node_idx] = 1
            forces[2 * node_idx] = 0
            forces[2 * node_idx + 1] = 0

    rank = np.linalg.matrix_rank(A)

    try:
        forces_in_bars = np.linalg.lstsq(A, forces, rcond=None)[0]
    
    except np.linalg.LinAlgError:
        raise ValueError("O sistema de equações não pode ser resolvido. Verifique as condições de isostaticidade.")

    results = []
    for j, bar in enumerate(bars):
        force = forces_in_bars[j]
        status = "T" if force > 0 else "C"
        bar_name = f"{bar.start_node}{bar.end_node}"
        results.append((bar_name, status, abs(force)))

    return results

def solve_truss_by_nodes(nodes, bars, supports):

    node_map = {node.name: (node.x, node.y) for node in nodes}

    results = {}

    bar_data = {}
    for bar in bars:
        start_coords = node_map[bar.start_node]
        end_coords = node_map[bar.end_node]
        dx = end_coords[0] - start_coords[0]
        dy = end_coords[1] - start_coords[1]
        length = (dx**2 + dy**2) ** 0.5
        cos_theta = dx / length
        sin_theta = dy / length
        bar_data[bar.name] = {"cos": cos_theta, "sin": sin_theta, "length": length}

    for node in nodes:

        fx = sum(force.x for force in node.forces)
        fy = sum(force.y for force in node.forces)

        for support in supports:
            if support.node == node.name:
                if support.support_type == 1: 
                    fy = 0  
                elif support.support_type == 2:  
                    fx = 0  
                    fy = 0 

        connected_bars = [bar for bar in bars if bar.start_node == node.name or bar.end_node == node.name]

        if len(connected_bars) > 1:
            A = []
            b = [-fx, -fy]

            for bar in connected_bars:
                bar_info = bar_data[bar.name]
                cos_theta = bar_info["cos"]
                sin_theta = bar_info["sin"]
                direction = 1 if bar.start_node == node.name else -1

                A.append([direction * cos_theta, direction * sin_theta])

            A = np.array(A).T  
            b = np.array(b)

            try:
                forces = np.linalg.lstsq(A, b, rcond=None)[0]
                for i, bar in enumerate(connected_bars):
                    results[bar.name] = forces[i]
            except np.linalg.LinAlgError:
                print(f"Não foi possível resolver o sistema no nó {node.name}.")
        else:
            print(f"O nó {node.name} tem menos de 2 barras conectadas.")

    formatted_results = []
    for bar_name, force in results.items():
        status = "T" if force > 0 else "C"
        formatted_results.append((bar_name, status, abs(force)))

    return formatted_results


def solve_truss_by_global_stiffness(nodes, bars, supports):
    node_map = {node.name: (node.x, node.y) for node in nodes}

    num_nodes = len(nodes)
    num_bars = len(bars)

    if num_bars != 2 * num_nodes - 3:
        return

    dof = 2 * num_nodes  
    global_stiffness = np.zeros((dof, dof))
    force_vector = np.zeros(dof)

    bar_data = {}
    for bar in bars:
        start_idx = nodes.index(next(n for n in nodes if n.name == bar.start_node))
        end_idx = nodes.index(next(n for n in nodes if n.name == bar.end_node))

        start_coords = np.array(node_map[bar.start_node])
        end_coords = np.array(node_map[bar.end_node])
        delta = end_coords - start_coords
        length = np.linalg.norm(delta)

        cos_theta = delta[0] / length
        sin_theta = delta[1] / length

        bar_data[bar.name] = {"cos": cos_theta, "sin": sin_theta, "length": length}

        k_local = (1 / length) * np.array([
            [cos_theta**2, cos_theta*sin_theta, -cos_theta**2, -cos_theta*sin_theta],
            [cos_theta*sin_theta, sin_theta**2, -cos_theta*sin_theta, -sin_theta**2],
            [-cos_theta**2, -cos_theta*sin_theta, cos_theta**2, cos_theta*sin_theta],
            [-cos_theta*sin_theta, -sin_theta**2, cos_theta*sin_theta, sin_theta**2],
        ])

        global_indices = [2 * start_idx, 2 * start_idx + 1, 2 * end_idx, 2 * end_idx + 1]

        for i in range(4):
            for j in range(4):
                global_stiffness[global_indices[i], global_indices[j]] += k_local[i, j]

    for node in nodes:
        node_idx = nodes.index(node)
        force_vector[2 * node_idx] += sum(f.x for f in node.forces)
        force_vector[2 * node_idx + 1] += sum(f.y for f in node.forces)

    constrained_dofs = []
    for support in supports:
        node_idx = nodes.index(next(n for n in nodes if n.name == support.node))
        if support.node == "A": 
            constrained_dofs.extend([2 * node_idx, 2 * node_idx + 1])  
        elif support.node == "B":  
            constrained_dofs.append(2 * node_idx + 1)  


    free_dofs = [i for i in range(dof) if i not in constrained_dofs]

    reduced_stiffness = global_stiffness[np.ix_(free_dofs, free_dofs)]
    reduced_forces = force_vector[free_dofs]

    displacements = np.zeros(dof)
    displacements[free_dofs] = np.linalg.solve(reduced_stiffness, reduced_forces)

    bar_forces = {}
    for bar in bars:
        start_idx = nodes.index(next(n for n in nodes if n.name == bar.start_node))
        end_idx = nodes.index(next(n for n in nodes if n.name == bar.end_node))

        start_disp = displacements[2 * start_idx:2 * start_idx + 2]
        end_disp = displacements[2 * end_idx:2 * end_idx + 2]
        delta_disp = np.concatenate([start_disp, end_disp])

        k_local = bar_data[bar.name]
        force = (1 / k_local["length"]) * np.dot(
            np.array([-k_local["cos"], -k_local["sin"], k_local["cos"], k_local["sin"]]),
            delta_disp,
        )
        bar_forces[bar.name] = force

    results = [] 
    for bar in bars: 
        force = bar_forces[bar.name]
        status = "T" if force > 0 else "C" if force < 0 else "N"       
        bar_name = f"  {bar.start_node}{bar.end_node}"
        results.append((bar_name, status, (force)))

    return results