import networkx as nx
import random 
import matplotlib.pyplot as plt
from matplotlib import pylab
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import chain

global T, COUNTER
COUNTER = 1
T = nx.MultiDiGraph()

""" Simulate a random walk on the binary tree for N steps. """ 
def loop_contraction(N, T): 
    path = [1] #the path that will be animated, stored as a ordered list of vertices
    edge_list = [(1,0)]
    T.add_node(1, parent =-1, isInSuperVertex = False)
    for _ in range(N): #each step
        #see if the last entry is a tupple of tupples or just a tuple of ints (i.e are we in a super vertex)
        v = edge_list[-1][0] #if not super vertex, then this is where our walk is at right now
        next_step = -1
        print(f"STEP NUMBER {_}")
        if type(v) is int:
            #normal vertex
            #determine our possible paths out
            temp_set = set()
            temp_set.add(v)
            v, next_step = out_edges_from(T,edge_list, temp_set) #pick a random one
            print(f"We are at {v}")
        else:
            #we are in a super vertex
            #make a set of all the vertices inside the super vertex
            vertices = set()
            for vertex in edge_list[-1]:
                vertices.add(vertex[0])
                vertices.add(vertex[1])
            v, next_step = out_edges_from(T, edge_list, vertices)

        #check the list if we have made any contractions,i.e check for cycles
        print((v, next_step) in edge_list)
        if (v, next_step) in edge_list: #we have a cycle, contract
            #remove the first part of the cycle, put it at the front and turn into super vertex
            print("CYCLE DETECTED")
            edge_list.remove((v, next_step))
            edge_list.append(((next_step, v), (v, next_step)))
            if T.nodes[next_step]["isInSuperVertex"] == True or T.nodes[v]["isInSuperVertex"] == True:
                #gotta union the super vertices if they overlap
                print("OVERLAP DETECTED")
                overlapping_svert = []
                for edge in edge_list:
                    print(edge)
                    if isVertexInSuperEdge(v, edge) or isVertexInSuperEdge(next_step, edge): #contract
                        print("OVERLAPPED ^")
                        overlapping_svert.append(edge)
                        edge_list.remove(edge)

                union = tuple(flatten_edge_list(overlapping_svert)) #flatten the above list from ((),(),((),())) into ((),(),())       
                edge_list.append(union)
            else:
                T.nodes[next_step]["isInSuperVertex"] = True
                T.nodes[v]["isInSuperVertex"] = True #book keeping for next step
        else:
            edge_list.append((next_step,v))

        path.append(next_step)
        print(edge_list)
        print("----")
        
    return edge_list, path

def out_edges_from(T, edge_list, vertices):
    #
    global COUNTER
    possible_out_verticies = []
    vert_to_out = {}
    flat_edge_list = flatten_edge_list(edge_list)
    print(f"The flat edge list: {flat_edge_list}")
    print(f"VERTICES: {vertices}")
    next_step = -1
    d = 3 #what kind of tree is this
    for v in vertices:
        vert_to_out[v] = [] #empty list
        possible_out_verticies.extend([v]*d)
        for v_tup in flat_edge_list:
            #count how many times, keep an account of to where  
            if v_tup[1] == v:
                possible_out_verticies.remove(v)
                vert_to_out[v].append(v_tup[1])
    out_vertex = random.choice(possible_out_verticies) #pick out of which vertex to come out from
    #pick which edge to go thru
    direction = random.randrange(1,d)
    if direction ==1 and (T.nodes[out_vertex]["parent"] not in vert_to_out[out_vertex]) and (out_vertex != 1): #the parent hasnt been walked to
        next_step = T.nodes[out_vertex]["parent"]
    else:
        #make a new edge to walk to
        COUNTER += 1
        T.add_node(COUNTER, parent = out_vertex, isInSuperVertex = False)
        next_step = COUNTER

    print(f"Next step ({next_step}, {out_vertex})")
    T.add_edge(out_vertex, next_step)
    return (out_vertex, next_step)
    
def flatten_edge_list(edge_list):
    #take a list of tupples and tupples of tupples, and flatten into just a list of tupples
    flat_list = []
    for elem in edge_list:
        if type(elem[0]) is int: # (int, int)
            flat_list.append(elem)
        else: #((int, int), (int, int))
            for i in elem:
                flat_list.append(i)
    return flat_list

def isVertexInSuperEdge(vertex, edge_list_obj):
    if type(edge_list_obj[0]) is tuple:
        for edge in edge_list_obj:
            if vertex == edge[0] or vertex == edge[1]:
                return True
        
    return False
#Gives the animation
def animate_graph_traversal(graph, traversal_order):
    pos = graphviz_layout(T, prog="dot")  # Position nodes using spring layout
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update_animation, frames=len(traversal_order), fargs=(graph, pos, traversal_order, ax), interval=1500)
    plt.show()

def update_animation(frame, graph, pos, traversal_order, ax):
    ax.clear()
    current_node = traversal_order[frame]
    nx.draw(graph, pos, with_labels=True, node_size=200, ax=ax)
    nx.draw_networkx_nodes(graph, pos, nodelist=[current_node], node_color='r', node_size=100)
    #nx.draw_networkx_labels(graph, pos, labels=None, font_color='w', font_size=3, ax=ax)

N = 50
edge_list, path = loop_contraction(N, T) 
print(edge_list)
pos = graphviz_layout(T, prog="dot")
nx.draw(T, pos, with_labels= True, node_size = 200)
#plt.show() # Gives a static image
animate_graph_traversal(T,path) #Animated the thing
