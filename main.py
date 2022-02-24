import Task1 
import Task2
import json

def jsonToDict(filename):
    with open(filename) as json_file:
        dic = json.load(json_file)
    return dic

if __name__ == "__main__":
    g = jsonToDict("G.json")
    dist = jsonToDict("Dist.json")
    cost = jsonToDict("Cost.json")

    Task2.ucs(1, 50, 287932, g, dist, cost)