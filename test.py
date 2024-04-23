import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_graph_traversal(graph, traversal_order):
    pos = nx.spring_layout(graph)  # Position nodes using spring layout
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update_animation, frames=len(traversal_order), fargs=(graph, pos, traversal_order, ax), interval=1000)
    plt.show()

def update_animation(frame, graph, pos, traversal_order, ax):
    ax.clear()
    current_node = traversal_order[frame][1]
    nx.draw(graph, pos, with_labels=True, ax=ax)
    nx.draw_networkx_nodes(graph, pos, nodelist=[current_node], node_color='r', node_size=500)
    nx.draw_networkx_labels(graph, pos, labels={current_node: frame}, font_color='b', ax=ax)

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7)])
traversal_order = [(0,1),(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]  # Example traversal order (BFS)
animate_graph_traversal(G, traversal_order)
