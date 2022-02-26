import heapq
import json


def readGraph():
    with open("Graph.json") as graph_file:
        graphdict = json.load(graph_file)
    return graphdict


def dijkstra(graph, source, des):
    pqheap = []
    parent = [-1 for i in range(len(graph))]
    for child_node in graph[str(source)]:
        parent[child_node[1]] = source
    found = False
    visited = [0 for i in range(len(graph))]
    visited[source] = 1
    cur_cost = 0
    for i in range(len(graph[str(source)])):
        pqheap.append(graph[str(source)][i])
    heapq.heapify(pqheap)

    while len(pqheap) != 0:
        min_cost_node = heapq.heappop(pqheap)                  # returns the vertex with the lowest cost
        cur_node = min_cost_node[1]                            # takes the cost to the node from source as d[u]
        visited[cur_node] = 1                                  # mark as selected/visited. - prevents inf loop if cycle
        if visited[des] == 1:
            break
        for next_node in graph[str(cur_node)]:                 # 'look' at all the nodes connected to current node.
            cur_cost = min_cost_node[0]                        # need to reinitialize or will use unoriginal value
            if visited[next_node[1]] != 1:                     # only need to consider non-visited nodes
                for conn in graph[str(source)]:                # find existing connection in source vertex if it exists
                    if conn[1] == next_node[1]:                # If there is a existing connection
                        found = True
                        if cur_cost + next_node[0] < conn[0]:  # if cur path is cheaper than recorded path: update src
                            cur_cost += next_node[0]
                            conn[0] = cur_cost
                            parent[next_node[1]] = cur_node
                            heapq.heappush(pqheap, [cur_cost, next_node[1]])
                if not found:                                  # if there is no existing connection, add new one.
                    cur_cost += next_node[0]
                    parent[next_node[1]] = cur_node
                    graph[str(source)].append([cur_cost, next_node[1]])
                    heapq.heappush(pqheap, [cur_cost, next_node[1]])
                found = False
    return parent, cur_cost


def constructpath(path, des):
    i = des
    src_des_path = [i]
    while path[i] != -1:
        src_des_path.append(path[i])
        i = path[i]
    src_des_path.reverse()
    return src_des_path


def printpath(path):
    j = 0
    for i in range(len(path)-1):
        print(path[i], end=" -> ")
        j = i
    print(path[j+1])

def run():
    Graph = readGraph()
    source = 1
    destination = 50
    path, cost = dijkstra(Graph, source, destination)
    todespath = constructpath(path, 50)
    printpath(todespath)
    print("Path Distance = " + str(cost))
