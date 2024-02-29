import networkx as nx
import matplotlib.pyplot as plt

def draw_graph_from_file(file_name):
    with open(file_name, 'r') as f:
        num_nodes, num_edges = map(int, f.readline().split())
        edges = [tuple(map(int, line.split())) for line in f]

    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    G.add_edges_from(edges)

    # Draw the graph
    pos = nx.spring_layout(G)  # Positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=8, font_color='black', font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, font_color='red', edge_labels={(u, v): f"{u}-{v}" for u, v in G.edges()})
    plt.title("Graph from File")
    plt.show()

# Example usage:
draw_graph_from_file("incomplete_grid_graph.txt")
