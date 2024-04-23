import networkx as nx
import random 
import matplotlib.pyplot as plt
from matplotlib import pylab
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


global T
T = nx.DiGraph()

""" Simulate a random walk on the binary tree for N steps. """ 
def loop_contraction(N, T): 
    
    return path  

#Gives the animation
def animate_graph_traversal(graph, traversal_order):
    pos = graphviz_layout(T, prog="dot")  # Position nodes using spring layout
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update_animation, frames=len(traversal_order), fargs=(graph, pos, traversal_order, ax), interval=50)
    plt.show()

def update_animation(frame, graph, pos, traversal_order, ax):
    ax.clear()
    current_node = traversal_order[frame][1]
    nx.draw(graph, pos, with_labels=False, node_size=10, ax=ax)
    nx.draw_networkx_nodes(graph, pos, nodelist=[current_node], node_color='r', node_size=10)
    #nx.draw_networkx_labels(graph, pos, labels=None, font_color='w', font_size=3, ax=ax)

N = 500
path = loop_contraction(N, T) 
print(path)
pos = graphviz_layout(T, prog="dot")
nx.draw(T, pos, with_labels= False, node_size =5)
plt.show() # Gives a static image
#animate_graph_traversal(T,path) #Animated the thing
