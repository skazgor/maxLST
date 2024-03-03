import random
import networkx as nx
random.seed(42)

def check_is_simple_and_connected(G: nx.Graph):
    is_connected = nx.is_connected(G)
    has_self_loops = any(u == v for u, v in G.edges())
    has_parallel_edges = len(G.edges()) != len(set(G.edges()))
    is_simple = not (has_self_loops or has_parallel_edges)
    return is_connected and is_simple


def generate_random_graph(file_name: str, N: int, p: float):
    """
    Generate a random graph with N nodes and probability p for edge creation.
    Erdos Renyi model.

    Parameters:
        N (int): Number of nodes in the network.
        p (float): Probability for edge creation.

    Returns:
        nx.Graph: A random graph.
    """
    generated_graph = nx.erdos_renyi_graph(N, p)

    if check_is_simple_and_connected(generated_graph):
        fhand = open(file_name, "w")
        fhand.write(
            f"{generated_graph.number_of_nodes()} {generated_graph.number_of_edges()}\n"
        )
        for edge in generated_graph.edges():
            fhand.write(f"{edge[0]} {edge[1]}\n")
        fhand.close()
    
    else:
        generate_random_graph(file_name, N, p)



def generate_scale_free_graph(file_name: str, N: int, m: int):
    """
    Generate a scale-free graph with N nodes and m edges to attach from a new node to existing nodes.
    Barabasi Albert model.

    Parameters:
        N (int): Number of nodes in the network.
        m (int): Number of edges to attach from a new node to existing nodes.

    Returns:
        nx.Graph: A scale-free graph.
    """
    generated_graph = nx.barabasi_albert_graph(100, 2)

    if check_is_simple_and_connected(generated_graph):
        fhand = open(file_name, "w")
        fhand.write(
            f"{generated_graph.number_of_nodes()} {generated_graph.number_of_edges()}\n"
        )

        for edge in generated_graph.edges():
            fhand.write(f"{edge[0]} {edge[1]}\n")
        fhand.close()

    else:
        print("Graph is not simple and connected.")


def generate_random_d_regular_graph(file_name: str, N: int, d: int):
    """
    Generate a random d-regular graph with N nodes and degree d.
    Random regular graph model.

    Parameters:
        N (int): Number of nodes in the network.
        d (int): Degree of each node.

    Returns:
        nx.Graph: A random d-regular graph.
    """
    if N * d % 2 != 0:
        raise ValueError("N * d must be even to create a d-regular graph.")

    generated_graph = nx.random_regular_graph(d, N)

    if check_is_simple_and_connected(generated_graph):
        fhand = open(file_name, "w")
        fhand.write(
            f"{generated_graph.number_of_nodes()} {generated_graph.number_of_edges()}\n"
        )

        for edge in generated_graph.edges():
            fhand.write(f"{edge[0]} {edge[1]}\n")

        fhand.close()

    else:
        print("Graph is not simple and connected.")


def generate_complete_grid_graph(file_name: str, rows: int, cols: int):
    """
    Generate a complete grid graph with the specified number of rows and columns.

    Parameters:
        file_name (str): Name of the file to save the graph.
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.

    Returns:
        nx.Graph: A complete grid graph.
    """
    generated_graph = nx.grid_2d_graph(rows, cols)

    grid_to_node_number = {node: i for i, node in enumerate(generated_graph.nodes())}

    if check_is_simple_and_connected(generated_graph):
        fhand = open(file_name, "w")
        fhand.write(
            f"{generated_graph.number_of_nodes()} {generated_graph.number_of_edges()}\n"
        )
        for edge in generated_graph.edges():
            fhand.write(f"{grid_to_node_number[edge[0]]} {grid_to_node_number[edge[1]]}\n")
        fhand.close()

    else:
        print("Graph is not simple and connected.")


def generate_incomplete_grid_graph(file_name : str, rows: int, cols: int, removal_prob: float):
    """
    Generate an incomplete grid graph with the specified number of rows and columns.

    Parameters:
        file_name (str): Name of the file to save the graph.
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.

    Returns:
        nx.Graph: An incomplete grid graph.
    """
    generated_graph = nx.grid_2d_graph(rows, cols)

    incomplete_grid_graph = generated_graph.copy()
    for edge in list(generated_graph.edges()):
        if random.random() < removal_prob:
            incomplete_grid_graph.remove_edge(*edge)

    generated_graph = incomplete_grid_graph

    grid_to_node_number = {node: i for i, node in enumerate(generated_graph.nodes())}

    if check_is_simple_and_connected(generated_graph):
        fhand = open(file_name, "w")
        fhand.write(
            f"{generated_graph.number_of_nodes()} {generated_graph.number_of_edges()}\n"
        )
        for edge in generated_graph.edges():
            fhand.write(f"{grid_to_node_number[edge[0]]} {grid_to_node_number[edge[1]]}\n")
        fhand.close()
    else:
        generate_incomplete_grid_graph(file_name, rows, cols, removal_prob)


# for i in range(1, 11):
#     generate_random_graph(f"random_graph_{i}.txt", 100, 0.1)
#     generate_scale_free_graph(f"scale_free_graph_{i}.txt", 100, 2)
#     generate_random_d_regular_graph(f"random_d_regular_graph_{i}.txt", 100, 3)
#     generate_complete_grid_graph(f"complete_grid_graph_{i}.txt", 5, 5)
#     generate_incomplete_grid_graph(f"incomplete_grid_graph_{i}.txt", 5, 5, 0.3)


for i in range(10):
    number_of_nodes = 10 + i*4
    generate_random_graph(f"random_graph_{i+1}.txt", number_of_nodes, 0.1)

