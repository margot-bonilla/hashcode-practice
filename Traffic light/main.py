# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from edge import *
from car import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    edges = []
    edges.append(Edge(1, 0, 1, 1))
    edges.append(Edge(1, 1, 2, 2))
    edges.append(Edge(1, 2, 3, 3))

    car1 = car(edges[:], 1)
    car2 = car(edges[:], 2)
    car = [car1, car2]
    for i in range(3):
        edges[i].turn_on()
    edges[0].turn_off()

    for i in range(10):
        for j in range(2):
            if len(car[j].route)>0:
                car[j].traffic_light(car[j].route[0].on, i+1)

        if i == 2:
            edges[0].turn_on()

