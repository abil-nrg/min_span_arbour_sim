import networkx as nx
import random 
import matplotlib.pyplot as plt
from matplotlib import pylab
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys


global T
T = nx.Graph()

""" Simulate a random walk on the binary tree for N steps. """ 
def random_walk(N, T): 
    path = [(0, 0)] # starting point
    T.add_node(0, rchild = -1, lchild = -1, parent=-2)
    ctr = 0
    for _ in range(N): 
        v = path[-1][-1] # Randomly choose a direction: up, down, left, or right 
        direction = -1
        if v == 0: #root
            direction = random.choice(["rchild", "lchild"])
        else:
            direction = random.choice(["rchild", "lchild", "parent"])

        
        if nx.get_node_attributes(T, direction)[v] == -1: #dne i.e guaranteed to be not parent
            ctr += 1
            T.add_node(ctr, rchild = -1, lchild = -1, parent = v)
            T.add_edge(v,ctr)
            path.append((v, ctr))
        
        else: #is parent
            #alter nothing
            T.add_edge(v, T.nodes[v]["parent"])
            path.append((v, T.nodes[v]["parent"]))

    return path  

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

N = 1000
path = random_walk(N, T) 
print(path)

if int(sys.argv[1]) == 1:
    print("Saving tree ...")
    pos = graphviz_layout(T, prog="dot")
    fig = plt.figure()
    nx.draw(T, pos, with_labels= False, ax = fig.add_subplot() ,node_size =5)
    #plt.show() # Gives a static image
    plt.savefig(f"random_walk_bin_tree_{N}.png")
elif int(sys.argv[1]) == 2:
    print("Animating tree ...")
    animate_graph_traversal(T,path) #Animated the thing
"""
TO DO :
 Add some kind of colored signature as to how early in the walk the node was visited
"""