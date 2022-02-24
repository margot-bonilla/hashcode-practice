import random as rnd

def create_list(proyectos, alpha1, alpha2):
    list = []
    for i in proyectos:
        list.append((i.name, i.punt/(alpha1 * i.len(roles) + alpha2 * i.time)))

    return list

def select_as_random(list):
    return list.pop(rnd.randint(0, 2))

def select_developer(developers, proyect, dict):
    
    # No puedo /  Becario  / Puede
    #    -1          0         1

    #for skill in developers:
    #    for code in proyect.roles:
    for i in developers:

    pass




def algo(proyectos, alpha1, alpha2):

    list = create_list(proyectos, alpha1, alpha2)
    proyect = select_as_random(list)



