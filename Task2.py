from queue import PriorityQueue

#uniform cost search using priority queue
def ucs(start, end, energyBudget, g, dist, cost):
    visited = [0] * (len(g)+1)
    parent = [-1] * (len(g)+1)
    tCost = [0] * (len(g)+1) #keep track of total energy cost from start for each vertex

    q = PriorityQueue()
    q.put((0, start))

    while(q.empty()==0):
        v = q.get()[1]
        visited[v] = 1

        if(v == end): 
            printResult(parent, start, v, dist, cost)
            return

        for w in g[str(v)]:
            w = int(w)
            if(not visited[w]):
                c = cost[str(v) + "," + str(w)]
                curCost = tCost[v]+c
                if(curCost <= energyBudget):
                    q.put((curCost, w))
                    tCost[w] = curCost
                    parent[w] = v
    print("not found")
    return


def printResult(parent: list, start, end, dist, cost):
    d = 0 #distance
    e = 0 #energy
    v = end
    path = str(end)

    while (v != start):
        edge = str(parent[v]) + "," + str(v) 
        d += dist[edge]
        e += cost[edge]

        path = str(parent[v]) +" -> "+path
        v = parent[v]        

    print("Path for UCS: " + path)
    print(f"Path Distance : {d}")
    print(f"Total Energy Cost {e}")


 
