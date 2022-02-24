import random as rnd

def create_list(proyectos, alpha1, alpha2):
    list = []
    for i in proyectos:
        list.append((i.name, i.punt/(alpha1 * i.n_roles + alpha2 * i.time)))

    return list

def select_as_random(list):
    return list.pop(rnd.randint(0, 2))

def select_developer():
    pass

def algo(proyectos, alpha1, alpha2):

    list = create_list(proyectos, alpha1, alpha2)
    proyect = select_as_random(list)



