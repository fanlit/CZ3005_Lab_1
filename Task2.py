from queue import PriorityQueue

#uniform cost search using priority queue
def ucs(start, end, energyBudget, g, dist, cost):
    visited = [0] * (len(g)+1) 
    parent = [-1] * (len(g)+1)
    pathCost = [0] * (len(g)+1)

    q = PriorityQueue()
    q.put((0, start))

    count = 0

    while(q.empty()==0):
        v = q.get()[1]
        visited[v] = 1
        count+=1

        if(v == end): 
            printResult(parent, start, v, dist, cost)
            break
        
        #v is current vertex, w is adjacent vertex
        for w in g[str(v)]:
            w = int(w)

            if(not visited[w]):
                c = cost[str(v) + "," + str(w)] #energy cost from current vertex to adjacent vertex
                curCost = pathCost[v]+c #total energy cost from start to adjacent vertex

                if(curCost <= energyBudget):
                    q.put((curCost, w))
                    pathCost[w] = curCost
                    parent[w] = v

    print(f"Visited: {count}")                
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

    print(path)
    print(f"Path Distance = {d}")
    print(f"Total Energy Cost = {e}")


 
