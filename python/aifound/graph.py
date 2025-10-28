import networkx as nx
import matplotlib.pyplot as plt

# Define node positions
node_positions = {
    'A': (0, 0),
    'B': (2, 0),
    'C': (1, 5),
    'D': (3, 3)
}

# Get the adjacency matrix from the user
adj_matrix = []
nodes = ['A', 'B', 'C', 'D']
for i in range(4):
    row = list(map(int, input(f"Enter row {nodes[i]} (space-separated): ").split()))
    adj_matrix.append(row)

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from(nodes)

# Add edges based on the adjacency matrix
for i in range(4):
    for j in range(4):
        if adj_matrix[i][j] == 1:
            G.add_edge(nodes[i], nodes[j])

# Draw the graph
nx.draw(G, node_positions, with_labels=True, node_color='lightblue', node_size=5000, width=2, font_size=12)
plt.show()
