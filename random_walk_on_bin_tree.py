import networkx as nx
import matplotlib
import random

"""
step(tree T, vertex v)
Takes a tree T (vertices and edges) and the vertex to step from , v.
Depending on whether the vertex is a root or not, a random number
[0-2] for non root and [0-1] for vertex, to then take a step.
Returns a tupple of the modified tree and next vertex.
"""

def step(T, v):
    if v == 1 : #is root?
        next_step = random.randint(0,1) # 1/2 go left, 1/2 go right
    else:
        next_step = random.randint(0,2) # 1/3 go left, 1/3 go right, 1/3 go parent

    if next_step == 1: #left
        pass

def main():
    T = nx.Graph()
    T.add_node(1) #root
    amt_of_steps = 100
    next_step_v = 1
    print(T.number_of_nodes())
    for i in range(0,amt_of_steps):
        [T, next_step_v] = T, step(T, next_step_v)
    
    return 1

main()