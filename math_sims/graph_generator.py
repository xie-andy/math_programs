import random
import sys

num_nodes = int(input("How many nodes would you like? "))
num_edges = int(input("How many edges would you like? "))

if (num_edges > ((num_nodes*(num_nodes-1))/2)):
    print("Too many edges for a simple graph. Quitting program.")
    sys.exit()

# edge_weights = bool(input("Would you like your graph to have edge weights? Type True or False: "))
edge_weight_lower = int(input("Enter the lower bound of your edge weights: "))
edge_weight_upper = int(input("Enter the upper bound of your edge weights: "))
# directivity = bool(input("Would you like your graph to be directed? Type True or False: "))
# parallel = bool(input("Would you like to allow parallel edges? Type True or False: "))
# anti_parallel = bool(input("Would you like to allow anti-parallel edges? Type True or False: "))

edges = []
weights = []

i = 0
while i < num_edges:
    node_a = random.randint(1, num_nodes)
    node_b = random.randint(1, num_nodes)
    while (node_b == node_a):
        node_b = random.randint(1, num_nodes)
    if ((node_a, node_b) not in edges) and ((node_b, node_a) not in edges):
        edges.append((node_a, node_b))
        weights.append(random.randint(edge_weight_lower, edge_weight_upper))
        i += 1
    else:
        continue

i = 0
while i < len(edges):
    print(f"{edges[i]}, Weight: {weights[i]}")
    # print(edges[i])
    # print(weights[i])
    i += 1