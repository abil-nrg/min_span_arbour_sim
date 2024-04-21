import random 

""" Simulate a random walk on the integer grid for N steps. """ 
def random_walk(N): 
    path = [(0, 0)] # starting point 
    for _ in range(N): 
        x, y = path[-1] # Randomly choose a direction: up, down, left, or right 
        direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)]) 
        next_step = (x + direction[0], y + direction[1]) 
        path.append(next_step) 
    return path 

""" Two-pass loop erasure algorithm. First pass: Record the latest occurrence of each point in a dictionary. Second pass: Use the dictionary to skip over points leading into loops. """ 
def loop_erasure(path): 
    latest_occurrence = {} # First Pass: Record the latest occurrence of each point 
    for i, point in enumerate(path): 
        latest_occurrence[point] = i 
    erased_path = [] 
    i = 0 # Second Pass: Use the dictionary to skip over points leading into loops 
    while i < len(path): 
        point = path[i] 
        erased_path.append(point) 
        i = latest_occurrence[point] + 1 

    return erased_path 

import matplotlib.pyplot as plt 
def plot_paths(path, erased_path): 
    """ Plot the given path and its loop-erased subpath. """ # Unzip the coordinates for plotting 
    x_path, y_path = zip(*path) 
    x_erased, y_erased = zip(*erased_path) 
    plt.figure(figsize=(16,16)) # Plot the original path in black 
    plt.plot(x_path, y_path, color='black', label='Original Path') # Plot the erased path in red 
    plt.plot(x_erased, y_erased, color='red', linestyle='--', label='Erased Path') # Set aspect ratio to 1:1 
    plt.gca().set_aspect('equal', adjustable='box') # Remove gridlines and axes 
    plt.grid(False) 
    plt.axis('off') 
    plt.savefig(f"loop_erasure_{N}.png") 

N = 1000000 
path = random_walk(N) 
erased_path = loop_erasure(path) 
plot_paths(path, erased_path)