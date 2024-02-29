import random
import networkx as nx


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

    fhand = open(file_name, "w")
    fhand.write(
        f"{generated_graph.number_of_nodes()} {generated_graph.number_of_edges()}\n"
    )

    for edge in generated_graph.edges():
        fhand.write(f"{edge[0]} {edge[1]}\n")

    fhand.close()


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

    fhand = open(file_name, "w")
    fhand.write(
        f"{generated_graph.number_of_nodes()} {generated_graph.number_of_edges()}\n"
    )

    for edge in generated_graph.edges():
        fhand.write(f"{edge[0]} {edge[1]}\n")

    fhand.close()


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

    fhand = open(file_name, "w")
    fhand.write(
        f"{generated_graph.number_of_nodes()} {generated_graph.number_of_edges()}\n"
    )

    for edge in generated_graph.edges():
        fhand.write(f"{edge[0]} {edge[1]}\n")

    fhand.close()


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

    fhand = open(file_name, "w")

    fhand.write(
        f"{generated_graph.number_of_nodes()} {generated_graph.number_of_edges()}\n"
    )

    for edge in generated_graph.edges():
        fhand.write(f"{grid_to_node_number[edge[0]]} {grid_to_node_number[edge[1]]}\n")

    fhand.close()


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

    fhand = open(file_name, "w")

    fhand.write(
        f"{generated_graph.number_of_nodes()} {generated_graph.number_of_edges()}\n"
    )

    for edge in generated_graph.edges():
        fhand.write(f"{grid_to_node_number[edge[0]]} {grid_to_node_number[edge[1]]}\n")

    fhand.close()


# generate_scale_free_graph("scale_free_graph.txt", 100, 2)
# generate_random_graph("random_graph.txt", 100, 0.1)
# generate_random_d_regular_graph("random_d_regular_graph.txt", 100, 3)
# generate_complete_grid_graph("complete_grid_graph.txt", 5, 5)
generate_incomplete_grid_graph("incomplete_grid_graph.txt", 5, 5, 0.3)
