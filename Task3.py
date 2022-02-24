from queue import PriorityQueue
import math

def heuristic(v, w, coord):
    xy1 = coord[str(v)] 
    xy2 = coord[str(w)]

    dx = abs(xy1[0]-xy2[0])
    dy = abs(xy1[1]-xy2[1])

    return math.sqrt(dx*dx + dy*dy) #return straight line cost of the two vertex using pythagorean

#A star search; f(n) = g(n) + h(n)
def aStar(start, end, energyBudget, g, dist, cost, coord):
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
                gn = pathCost[v]+c #total energy cost from start to adjacent vertex
                
                if(gn <= energyBudget):
                    hn = heuristic(w, end, coord) #future cost from w to end
                    fn = gn + hn

                    q.put((fn, w))
                    pathCost[w] = gn
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


 
