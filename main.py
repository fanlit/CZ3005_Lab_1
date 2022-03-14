import Task1 
import Task2
import Task3
import json


def jsonToDict(filename):
    with open(filename) as json_file:
        dic = json.load(json_file)
    return dic


if __name__ == "__main__":
    g = jsonToDict("G.json")
    dist = jsonToDict("Dist.json")
    cost = jsonToDict("Cost.json")
    coord = jsonToDict("coord.json")

    print("Task 1: Dijkstra Path:")
    Task1.run()
    print()
    print("Task 2: Uniform Cost Search Path:")
    Task2.ucs(1, 50, 287932, g, dist, cost)
    print()
    print("Task 3: A-Star Search Path:")
    Task3.aStar(1, 50, 287932, g, dist, cost, coord)
