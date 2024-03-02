"""
This script reads the edges of a spanning tree from a file and counts the number of nodes and leaf nodes in the spanning tree.
"""

import networkx as nx

# Function to read edges of spanning tree from file
def read_spanning_tree(file_name):
    with open(file_name, 'r') as file:
        edges = [tuple(map(int, line.split())) for line in file]
    return edges

# Function to check if a graph is a tree
def is_tree(graph):
    return len(graph.edges()) == len(graph.nodes()) - 1 and nx.number_connected_components(graph) == 1

# Function to count leaf nodes in a graph
def count_leaf_nodes(graph):
    return sum(1 for node in graph.nodes() if graph.degree[node] == 1)

# Read spanning tree from file
spanning_tree_edges = read_spanning_tree('spanning_tree_edge_list.txt')

# Create a graph object for the spanning tree
spanning_tree = nx.Graph()
spanning_tree.add_edges_from(spanning_tree_edges)

assert is_tree(spanning_tree) == True , "The spanning tree must be a tree"

# printing number of nodes and leaf nodes

print(f"Number of nodes: {spanning_tree.number_of_nodes()}")
print(f"Number of leaf nodes: {count_leaf_nodes(spanning_tree)}")
