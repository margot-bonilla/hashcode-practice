# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from edge import *
from car import *
from node import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nodos = [node(i) for i in range(5)]
    edges = []
    edges.append(Edge(1, nodos[0], nodos[1], 0))
    edges.append(Edge(1, nodos[1], nodos[2], 1))
    edges.append(Edge(1, nodos[2], nodos[3], 2))
    edges.append(Edge(1, nodos[4], nodos[1], 3))

    car1 = car([edges[i] for i in range(3)], 1)
    car2 = car([edges[i] for i in range(2)], 2)
    car = [car2, car1]
    for i in range(3):
        edges[i].turn_on(edges)

    for i in range(10):
        for j in range(2):
            if len(car[j].route)>0:
                car[j].traffic_light(car[j].route[0].on, i+1)
            else:
                car[j].destroy(i)

        if i == 2:
            edges[0].turn_on(edges)

