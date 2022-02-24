import json


def jsonToDict():
    with open("G.json") as graph_file:
        graphdict = json.load(graph_file)
    with open("Dist.json") as dist_file:
        distdict = json.load(dist_file)
    return distdict, graphdict

def makegraph(distdict, graphdict):
    graph = {}
    connlist = []

    for cur_node in graphdict.keys():
        for connected_node in graphdict[cur_node]:
            node_pair = cur_node + "," + connected_node
            connlist.append([distdict[node_pair], int(connected_node)])
        graph[int(cur_node)] = connlist.copy()
        connlist.clear()
    return graph


distdict, graphdict = jsonToDict()
graph = makegraph(distdict, graphdict)
print(graph)
f = open("Graph.json", "w")
json.dump(graph, f)
f.close()
