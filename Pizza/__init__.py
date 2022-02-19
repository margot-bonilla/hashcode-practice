from Client import *
import random as rand
import copy

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def eval_sol(Clients, pizza):
    puntos = 0
    for i in Clients:
        if len(set(i.like)-set(pizza)) == 0 and len(set(pizza) - set(i.dislike)) == len(pizza):
            puntos += 1

    return puntos

def inicializar_lista(Clients, productos):
    dic = {k: 0 for k in productos}
    for i in productos:
        for j in Clients:
            if i in j.like:
                dic[i] += 1
            if i in j.dislike:
                dic[i] -= 1

    dic = dict(sorted(dic.items(), reverse=True, key=lambda item: item[1]))
    return dic

def algo(Clients, productos):
    dic = inicializar_lista(Clients, productos)

    best_pizza = []
    best_points = 0
    for _ in range(10000):
        pizza = []
        while len(dic) > 0:
            n = rand.randint(0, min([len(dic)-1, 2]))
            pizza.append([*dic][n])
            del dic[[*dic][n]]
            points = eval_sol(Clients, pizza)
            if points > best_points:
                best_pizza = copy.deepcopy(pizza)
                best_points = points

    return (best_pizza, best_points)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    productos = ["lechuga", "pepino", "tomate", "Bacon"]

    Moein = Client(["lechuga", "pepino", "tomate"], ["Bacon"])
    Margot = Client(["lechuga", "pepino", "Bacon"], ["tomate"])
    Juanfran = Client(["lechuga", "tomate"], ["Bacon"])
    Douglas = Client(["lechuga", "pepino"], ["Bacon"])

    Clients = [Moein, Margot, Juanfran, Douglas]

    algo(Clients, productos)
