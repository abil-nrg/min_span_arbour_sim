import networkx as nx
import random 
import matplotlib.pyplot as plt
from matplotlib import pylab
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class HyperEdge:
    def __init__(self, members):
        self.members = members #list of vertice labels (ints)
    def append(self, v):
        self.members.append(v)
    def out_edges(self, T):
        out_edges = []
        for v in self.members:
            if(T.nodes[v]["out_degree"] > 0): #a member has a vertex out
                out_edges = out_edges + T.node[v]["out_edges"]
        return out_edges # a list of edge values

global T
T = nx.MultiDiGraph()

""" Simulate a random walk on the binary tree for N steps. """ 
def loop_contraction(N, T): 
    path = [(0,0)]
    T.add_node(0, out_degree=0, in_edges=[], out_edges=[])
    ctr = 0
    cur_step = 0 #start at root
    for _ in range(N):
        origin_of_step, next_step, H = step(cur_step, H) #changes the hypergraph
        
        if next_step >ctr:#change the multiditree, legality of step is already verified above
            T.add_node(ctr, out_degree=0, in_edges=[], out_edges=[]) #add the node

            if origin_of_step == cur_step: #no hyper edge was used
                T.nodes[cur_step]["out_edges"] += 1
                T.nodes[cur_step]["out_degree"] += 1
                T.add_edge(cur_step, ctr)
                path.append((cur_step, next_step))
            else: #a hyper edge was used
                T.nodes[origin_of_step]["out_edges"] += 1
                T.nodes[origin_of_step]["out_degree"] += 1
                T.add_edge(origin_of_step, ctr)
                path.append((cur_step, origin_of_step))
                path.append((origin_of_step, next_step))
    return path  

"""
Needs a hypergraph, H, and a current vertex, v
"""
def step(v, H):
    #alter the graph
    #chose randomly
    origin_of_step = -1
    next_step = -2
    return origin_of_step, next_step, H
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
