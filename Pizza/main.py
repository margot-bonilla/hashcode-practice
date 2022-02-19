import sys
import random as rand
import copy

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Clients:
    def __init__(self):
        self.clients = list()

    def append(self, client):
        self.clients.append(client)

    def __str__(self):
        return '\n\n'.join([str(client) for client in self.clients])

    def __repr__(self):
        return '\n\n'.join([str(client) for client in self.clients])


class Client:
    def __init__(self, likes, dislikes):
        self.likes = likes
        self.dislikes = dislikes

    def __str__(self):
        return f'likes: {",".join(self.likes)}\ndislikes: {",".join(self.dislikes)}'

    def __repr__(self):
        return f'likes: {",".join(self.likes)}\ndislikes: {",".join(self.dislikes)}'


def read_file(in_file):
    """
    Read Input File

    Args:
        in_file: input file path

    Returns:
        List of Clients
    """
    # Define variables
    clients = Clients()

    # Read the file into variables
    with open(in_file, 'r') as infile:
        number_of_clients = int(infile.readline())
        products = set()
        for client in range(number_of_clients):
            likes = [ingredient for ingredient in infile.readline().strip().split(' ')[1:]]
            dislikes = [ingredient for ingredient in infile.readline().strip().split(' ')[1:]]
            products = products.union(likes).union(dislikes)
            clients.append(Client(likes, dislikes))

    return clients.clients, list(products)

def write_file(out_file, final_result):
    """
    Write the submission file

    Args:
        out_file: output file path
    """
    with open(out_file, 'w') as outfile:
        outfile.write(f'{len(final_result)} {" ".join(final_result)}')

def eval_sol(Clients, pizza):
    puntos = 0
    for i in Clients:
        if len(set(i.likes)-set(pizza)) == 0 and len(set(pizza) - set(i.dislikes)) == len(pizza):
            puntos += 1

    return puntos

def inicializar_lista(Clients, productos):
    dic = {k: 0 for k in productos}
    for i in productos:
        for j in Clients:
            if i in j.likes:
                dic[i] += 1
            if i in j.dislikes:
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


def main(in_file, out_file):
    """
    The main program reads the input file, processes the calculation
    and writes the output file

    Args:
        in_file: input file path
        out_file: output file path
    """

    # Read File
    clients, products = read_file(in_file)
    # Process Algorithm
    final_result, final_score = algo(clients, products)
    # Print Score
    print(f'Result: {final_result}')
    print('Score: {}'.format(final_score))
    # Save results into the output if instructed
    if out_file is not None:
        write_file(out_file, final_result)
        print('{} is saved. The program completed.'.format(out_file))
    else:
        print('The program completed.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(sys.argv[0] + ' [in file] [out file: optional]')
    elif len(sys.argv) == 2:
        main(sys.argv[1], None)
    else:
        main(sys.argv[1], sys.argv[2])

