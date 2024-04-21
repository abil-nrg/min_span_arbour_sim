import networkx as nx
import random 
import matplotlib.pyplot as plt
from matplotlib import pylab
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation


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

def animate_nodes(T, ):
    pos = graphviz_layout(T, prog="dot")

    nodes = nx.draw_networkx_nodes(T, pos)
    edges = nx.draw_networkx_edges(T, pos)
    plt.axis('off')

    def update(ii):
        # nodes are just markers returned by plt.scatter;
        # node color can hence be changed in the same way like marker colors
        nodes.set_array(node_colors[ii])
        return nodes,

    fig = plt.gcf()
    animation = FuncAnimation(fig, update, interval=50, frames=len(node_colors), blit=True)
    return animation   

N = 100
path = random_walk(N, T) 
print(path)
#pos = graphviz_layout(T, prog="dot")
#nx.draw(T, pos, with_labels= True)
#plt.show()
ani = animate_nodes(T)
