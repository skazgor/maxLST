import heapq
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
import time


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.degrees = defaultdict(int)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.degrees[u] += 1
        self.degrees[v] += 1

    def max_degree_vertex(self):
        return max(self.degrees, key=self.degrees.get)
    
    # Function to visualize the graph
    def visualize_graph(self, title='Graph'):
        G_nx = nx.Graph()
        for node, edges in self.graph.items():
            for edge in edges:
                G_nx.add_edge(node, edge)
        
        plt.figure(figsize=(8, 5))
        plt.title(title)
        nx.draw(G_nx, with_labels=True, node_color='skyblue', node_size=700, edge_color='black')
        plt.show()

def priority_bfs(graph):
    start = graph.max_degree_vertex()
    T = set()
    Q = []
    visited = set()  # Set to keep track of visited nodes
    heapq.heappush(Q, (-graph.degrees[start], start))
    visited.add(start)
    
    while Q:
        _, i = heapq.heappop(Q)
        for v in graph.graph[i]:
            if v not in visited:
                priority = graph.degrees[v] - graph.degrees[i]
                heapq.heappush(Q, (-priority, v))
                T.add((i, v))
                visited.add(v)  # Mark this node as visited

    return T

def read_graph_from_file(file_path):
    graph = Graph()
    with open(file_path, 'r') as file:
        for line in file:
            u, v = line.strip().split()
            graph.add_edge(u, v)
    return graph

def visualize_tree(tree_edges, title='Resulting Tree'):
    G_nx = nx.Graph()
    G_nx.add_edges_from(tree_edges)
    
    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(G_nx, with_labels=True, node_color='lightgreen', node_size=700, edge_color='black')
    plt.show()


# Function to check if a graph is a tree
def is_tree(graph):
    return len(graph.edges()) == len(graph.nodes()) - 1 and nx.number_connected_components(graph) == 1

# Function to count leaf nodes in a graph
def count_leaf_nodes(graph):
    return sum(1 for node in graph.nodes() if graph.degree[node] == 1)


# We'll use the graph we've already created and saved to a file
file_path = 'example_graph.txt'
graph_from_file = read_graph_from_file(file_path)

# Visualize the original graph
# graph_from_file.visualize_graph('Original Graph')

# Apply Priority-BFS and visualize the resulting tree
start_time=time.time()
resulting_tree = priority_bfs(graph_from_file)
end_time=time.time()
print('Time taken: ', end_time-start_time)

graph=nx.Graph()
graph.add_edges_from(resulting_tree)
assert is_tree(graph)==True
print('number of nodes: ', graph.number_of_nodes())
print('number of leaf nodes: ', count_leaf_nodes(graph))
# visualize_tree(resulting_tree, 'Resulting Tree from Priority-BFS')
