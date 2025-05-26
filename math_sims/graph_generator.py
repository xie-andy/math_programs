import random
import sys

num_nodes = int(input("How many nodes would you like? "))
num_edges = int(input(f"How many edges would you like? Maximum of {int((num_nodes*(num_nodes-1))/2)}: "))

if (num_edges > ((num_nodes*(num_nodes-1))/2)):
    print("Too many edges for a simple graph. Quitting program.")
    sys.exit()

edge_weight_input = input("Would you like your graph to have edge weights? Type Y or N: ")
if (edge_weight_input == "Y"):
    edge_weights = True
else:
    edge_weights = False
if edge_weights:
    edge_weight_lower = int(input("Enter the lower bound of your edge weights: "))
    edge_weight_upper = int(input("Enter the upper bound of your edge weights: "))
    weights = []
# directivity = bool(input("Would you like your graph to be directed? Type True or False: "))
# parallel = bool(input("Would you like to allow parallel edges? Type True or False: "))
# anti_parallel = bool(input("Would you like to allow anti-parallel edges? Type True or False: "))

edges = []

i = 0
while i < num_edges:
    node_a = random.randint(1, num_nodes)
    node_b = random.randint(1, num_nodes)
    while (node_b == node_a):
        node_b = random.randint(1, num_nodes)
    if ((node_a, node_b) not in edges) and ((node_b, node_a) not in edges):
        edges.append((node_a, node_b))
        if edge_weights:
            weights.append(random.randint(edge_weight_lower, edge_weight_upper))
        i += 1
    else:
        continue

i = 0
while i < len(edges):
    if edge_weights:
        print(f"{edges[i]}, Weight: {weights[i]}")
    else:
        print(f"{edges[i]}")
    i += 1