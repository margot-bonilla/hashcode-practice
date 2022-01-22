import random
from car import *
import copy
from edge import *

def GA(max_time_simulation, car_routes_id, nodos, edges, car_score, len_population = 200, iter = 100, best = 4, alpha_mutation = 0.4):

    population = initial_population(len_population, max_time_simulation, edges, nodos)
    for _ in range(iter):
        for k in population:
            ind = k
            aux_edges = ind[0:(len(ind) - 1)][:]
            #car1 = car([edges[i] for i in range(3)], 1)
            car_aux = [car([copy.deepcopy(aux_edges[0][j]) for j in car_routes_id[i]], i) for i in range(len(car_routes_id))]
            for i in car_aux:
                i.route[0].cost = 0

            for i in range(max_time_simulation):
                car_aux = create_new_cars(car_aux, aux_edges[i])
                for j in car_aux:
                    if len(j.route) > 0:
                        j.traffic_light(j.route[0].on, i+1)
                    else:
                        ind[-1] += j.destroy(i+1, max_time_simulation, car_score)

        population_sorted = sorted(population, key=lambda population: population[-1], reverse=True)
        population = cross_over(population_sorted, len(population_sorted)-best)
        for i in range(len(population)):
            random_value = random.random()
            if random_value < alpha_mutation:
                mutation(population, i)
        for i in range(best):
            population.append(population_sorted[i][0:-1] + [0])

    return population_sorted[0][-1]

def initial_population(len_population, max_time_simulation, edges, nodos):
    population = []
    for j in range(len_population):
        individual = []
        for _ in range(max_time_simulation):
            aux_edges = copy.deepcopy(edges)
            aux_nodes = copy.deepcopy(nodos)
            for i in aux_nodes:
                if len(i.edges_intersection) != 0:
                    rand = random.randint(0, len(i.edges_intersection) - 1)
                    i.turn_on(i.edges_intersection[rand], aux_edges)

            individual.append(copy.deepcopy(aux_edges))
        individual.append(0)
        population.append(copy.deepcopy(individual))

    return population

def cross_over(population, n_child):
    new_population = []


    for i in range(n_child):
        rand = random.randint(1, len(population[0]) - 2)
        minimum = min([random.randint(0, len(population) - 1) for _ in range(3)])
        child_1 = population[minimum]
        child_2 = child_1
        while child_2 == child_1:
            minimum = min([random.randint(0, len(population) - 1) for _ in range(3)])
            child_2 = population[minimum]

        new_population.append(child_1[0:rand] + child_2[rand:-1] + [0])

    return new_population

def mutation(population, i):
    ind = population[i][0:-1]
    iter = random.randint(1, len(ind) - 1)
    random_values = random.randint(1, iter)
    num = random.sample([i for i in range(iter)], k=random_values)
    for j in num:
        num_changes = random.randint(1, len(ind[j])-1)
        index = random.sample([i for i in range(len(ind[j]))], num_changes)
        aux = [ind[i] for i in index][0]
        for k in aux:
            if k.on == False:
                k.turn_on(aux)

def create_new_cars(old_cars, new_edges):

    #[car([Edge(aux_edges[i][k], car_aux) for k in range(len(aux_edges[i])) if aux_edges[i][k].id in [car_aux[j].route[q].id for q in range(len(car_aux[j].route))]], car_aux[j].id, car_aux[j].out_of_road_in, car_aux[j].is_in_queue) for j in range(len(car_aux))]
    cars = []
    for i in range(len(old_cars)):
        edges = [[Edge(old_cars[i].route[k].cost, None, None, None, Edge = new_edges[j], on_queue = old_cars[i].route[k].on_queue) for j in range(len(new_edges)) if new_edges[j].id == old_cars[i].route[k].id ][0] for k in range(len(old_cars[i].route))]
        cars.append(car(edges, old_cars[i].id, old_cars[i].out_of_road_in, old_cars[i].is_in_queue))

    return cars

