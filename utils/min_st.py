"""
This module contains a function to read a graph from a file, find a minimum spanning tree of the graph, and write the spanning tree to a file.
"""
import networkx as nx

# Function to read graph from file
def read_graph(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_nodes, num_edges = map(int, lines[0].split())
        edges = [tuple(map(int, line.split())) for line in lines[1:]]
    return num_nodes, edges

# Function to write spanning tree to file
def write_spanning_tree(tree_edges, file_name):
    with open(file_name, 'w') as file:
        for edge in tree_edges:
            file.write(f"{edge[0]} {edge[1]}\n")

# Read graph from file
num_nodes, edges = read_graph('random_d_regular_graph.txt')

# Create a graph object
G = nx.Graph()

# Add edges to the graph
G.add_edges_from(edges)

# Get a minimum spanning tree of the graph
spanning_tree = nx.minimum_spanning_tree(G)

# Get the edges of the spanning tree
tree_edges = list(spanning_tree.edges())

# Write spanning tree to file
write_spanning_tree(tree_edges, 'spanning_tree_edge_list.txt')
