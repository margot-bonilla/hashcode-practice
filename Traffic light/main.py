# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from edge import *
from car import *
from node import *
from algo import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    car_score = 1000
    max_time_simulation = 6 + 1
    
    nodos = [node(i) for i in range(4)]
    edges = []
    edges.append(Edge(1, nodos[2], nodos[0], 0))
    edges.append(Edge(1, nodos[0], nodos[1], 1))
    edges.append(Edge(1, nodos[3], nodos[1], 2))
    edges.append(Edge(2, nodos[2], nodos[3], 3))
    edges.append(Edge(3, nodos[1], nodos[2], 4))

    car_routes_id = [[0, 1, 4, 3], [2, 4, 0]]


    #print("El score ha sido de:")
    final_score = GA(max_time_simulation, car_routes_id, nodos, edges, car_score, len_population = 100, iter = 20, verbose = True)
    print()
    print("The final_score is: " + str(final_score))


