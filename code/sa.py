import heapq
import random
from collections import defaultdict
import math
import copy

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.degrees = defaultdict(int)

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        self.degrees[u] += 1
        self.degrees[v] += 1

    def degree(self, vertex):
        return sum(self.adj_matrix[vertex])
    
    def max_degree_vertex(self):
        return max(self.degrees, key=self.degrees.get)
    def copy(self):
        new_graph = Graph(self.num_vertices)
        new_graph.adj_matrix = copy.deepcopy(self.adj_matrix)
        new_graph.degrees = copy.deepcopy(self.degrees)
        return new_graph

def priority_bfs(graph):
    start = graph.max_degree_vertex()
    T = Graph(graph.num_vertices)
    Q = []
    visited = set()  # Set to keep track of visited nodes
    heapq.heappush(Q, (-graph.degrees[start], start))
    visited.add(start)
    
    while Q:
        _, i = heapq.heappop(Q)
        for v in range(graph.num_vertices):  # Iterate over the adjacency matrix
            if graph.adj_matrix[i][v] == 1 and v not in visited:  # Check if there is an edge and the node is not visited
                priority = graph.degrees[v] - graph.degrees[i]
                heapq.heappush(Q, (-priority, v))
                T.add_edge(i, v)
                visited.add(v)  # Mark this node as visited

    return T


def random_neighbouring_tree(T):
    num_vertices = T.num_vertices
    # Step 1: Remove a random edge
    edges = []
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if T.adj_matrix[i][j] == 1:
                edges.append((i, j))
    random_edge = random.choice(edges)
    T.adj_matrix[random_edge[0]][random_edge[1]] = 0
    T.adj_matrix[random_edge[1]][random_edge[0]] = 0
    
    # Step 2: Find a random edge to reconnect the components
    disconnected_components = []
    visited = [False] * num_vertices
    for i in range(num_vertices):
        if not visited[i]:
            component = []
            stack = [i]
            while stack:
                v = stack.pop()
                component.append(v)
                visited[v] = True
                for j in range(num_vertices):
                    if T.adj_matrix[v][j] == 1 and not visited[j]:
                        stack.append(j)
            disconnected_components.append(component)
    
    # Pick two different components
    component_indices = list(range(len(disconnected_components)))
    i, j = random.sample(component_indices, 2)
    component1 = disconnected_components[i]
    component2 = disconnected_components[j]

    # Randomly select edges between the two components
    u = random.choice(component1)
    v = random.choice(component2)
    while T.adj_matrix[u][v] == 1:
        u = random.choice(component1)
        v = random.choice(component2)

    # Step 3: Add the random edge to reconnect the components
    T.adj_matrix[u][v] = 1
    T.adj_matrix[v][u] = 1

def fitness_function(T):
    num_leaves = 0
    total_weight = 0
    for i in range(T.num_vertices):
        degree = T.degree(i)
        if degree == 1:
            total_weight += 1
        elif degree == 2:
            total_weight += 0.5
        elif degree == 3:
            total_weight += 0.5
        elif degree > 3:
            total_weight += 0
        num_leaves += 1 if degree == 1 else 0
    return total_weight / T.num_vertices, num_leaves

def simulated_annealing(initial_tree, iterations):
    current_tree = initial_tree
    current_fitness, _ = fitness_function(current_tree)
    temperature = 1.0
    cooling_rate = 0.995

    for _ in range(iterations):
        new_tree = current_tree.copy()
        random_neighbouring_tree(new_tree)
        new_fitness, _ = fitness_function(new_tree)

        if new_fitness >= current_fitness or random.random() < math.exp((new_fitness - current_fitness - 1) / temperature):
            current_tree = new_tree
            current_fitness = new_fitness

        temperature *= cooling_rate

    return current_tree

def is_tree(graph):
    # A graph is a tree if it has n - 1 edges and is connected
    num_edges = sum(sum(row) for row in graph.adj_matrix) // 2
    num_nodes = graph.num_vertices
    return num_edges == num_nodes - 1 and is_connected(graph)

def is_connected(graph):
    # Use BFS to check if the graph is connected
    start = 0  # Start BFS from node 0
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for i in range(graph.num_vertices):
                if graph.adj_matrix[node][i] == 1 and i not in visited:
                    queue.append(i)
    return len(visited) == graph.num_vertices

# Function to count leaf nodes in a graph
def count_leaf_nodes(graph):
    return sum(1 for i in range(graph.num_vertices) if graph.degree(i) == 1)


def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        num_vertices , num_edges = map(int, file.readline().split())
        graph = Graph(num_vertices)
        graph.num_vertices = num_vertices
        for line in file:
            u, v = map(int, line.split())
            graph.add_edge(u, v)
    return graph

file_path = 'example_graph.txt'
graph = read_graph_from_file(file_path)
initial_tree = priority_bfs(graph)

# check if the initial tree is a tree and count the number of leaf nodes
print(is_tree(initial_tree))
print(count_leaf_nodes(initial_tree))
iterations = 1000
result_tree = simulated_annealing(initial_tree, iterations)

# check if the resulting tree is a tree and count the number of leaf nodes
print(is_tree(result_tree))
print(count_leaf_nodes(result_tree))