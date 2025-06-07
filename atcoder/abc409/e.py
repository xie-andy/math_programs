num_vertices = int(input())
vertice_trons = input().split(" ")
vertice_trons = list(map(int, vertice_trons))

edge_list = {}

# initialise each vertice
for i in range(num_vertices):
    i = i + 1
    edge_list[i] = [[], 0, vertice_trons[i-1]]

# scan each edge and update the dictionary thing
for i in range(num_vertices-1):
    edge = input().split(" ")
    edge = list(map(int, edge))

    vertex_1 = edge[0]
    vertex_2 = edge[1]
    weight = edge[2]

    # updating the nodes
    edge_list[vertex_1][0].append((vertex_2, weight))
    edge_list[vertex_1][1] += 1
    edge_list[vertex_2][0].append((vertex_1, weight))
    edge_list[vertex_2][1] += 1

sorted_edge_list = dict(sorted(edge_list.items(), key=lambda x:x[1][1], reverse = True))

# print(sorted_edge_list)

sum = 0

while len(sorted_edge_list) > 0:
    node = sorted_edge_list.popitem()[1]
    node_key = sorted_edge_list.popitem()[0]
    print(node)
# for node_key in sorted_edge_list:
#     # print(node)
#     node = sorted_edge_list[node_key]
    if (node[1] != 0):
        #print(node)
        weight = node[0][0][1]
        trons = node[2]
        sum += abs(weight * trons)
        # next, delete
        neighbour = sorted_edge_list[node[0][0][0]]
        own_representation = (node_key, weight)
        #neighbour[0].remove(own_representation)
        neighbour[1] -= 1
        neighbour[2] += trons
        sorted_edge_list[node[0][0][0]] = neighbour
    # sorted_edge_list.pop(node_key)
    # sorted_edge_list = dict(sorted(sorted_edge_list.items(), key=lambda x:x[1][1]))

print(sum)