

def create_list(proyectos, alpha1, alpha2):
    list = []
    for i in proyectos:
        list.append((i.name, i.punt/(alpha1 * i.n_roles + alpha2 * i.time)))

    return list

def algo(proyectos, alpha1, alpha2):

    create_list(proyectos, alpha1, alpha2)
    

