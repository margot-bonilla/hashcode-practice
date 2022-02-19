import sys
import random as rand
import copy
from multiprocessing import Process, Queue


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
    clients = []

    # Read the file into variables
    with open(in_file, 'r') as infile:
        number_of_clients = int(infile.readline())
        products = set()
        for client in range(number_of_clients):
            likes = infile.readline().strip().split(' ')[1:]
            dislikes = infile.readline().strip().split(' ')[1:]
            products = products.union(likes).union(dislikes)
            clients.append(Client(likes, dislikes))

    return clients, list(products)


def write_file(out_file, final_result):
    """
    Write the submission file

    Args:
        out_file: output file path
        final_result: list with the result
    """
    with open(out_file, 'w') as outfile:
        outfile.write(f'{len(final_result)} {" ".join(final_result)}')


def eval_sol(clients, pizza):
    print(f'Evaluating {len(clients)} clients for pizza with {len(pizza)} ingredients')
    score = 0
    for i in clients:
        if len(set(i.likes)-set(pizza)) == 0 and len(set(pizza) - set(i.dislikes)) == len(pizza):
            score += 1

    return score


def inicializar_lista(Clients, productos):
    dic = {k: 0 for k in productos}
    for i in productos:
        for j in Clients:
            if i in j.likes:
                dic[i] += 1
            if i in j.dislikes:
                dic[i] -= 1

    dic = dict(sorted(dic.items(), reverse=True, key=lambda item: item[1]))

    print(f'List of products initialized')
    # print(dic)
    return dic


def algo(clients, products, q, seed):
    print(f'{len(products)} number of products')
    dic = inicializar_lista(clients, products)

    best_pizza = []
    best_points = 0
    for _ in range(1):
        pizza = []
        while len(dic) > 0:
            n = rand.randint(0, min([len(dic)-1, 2]))
            pizza.append([*dic][n])
            del dic[[*dic][n]]
            points = eval_sol(clients, pizza)
            if points > best_points:
                print(f'Found a good pizza :)')
                # print(best_pizza)
                print(best_points)
                best_pizza = copy.deepcopy(pizza)
                best_points = points

    return q.put((best_pizza, best_points))


def main(in_file, process_count, out_file):
    q = Queue()
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
    processes = []
    for i in range(process_count):
        p = Process(target=algo, args=(clients, products, q, i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = []
    while not q.empty():
        results.append(q.get())
    sorted_results = sorted(results, key=lambda tup: tup[1], reverse=True)
    final_result, final_score = sorted_results[0]
    # Print Score
    # print(f'Result: {final_result}')
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
        main(sys.argv[1], 1, None)
    elif len(sys.argv) == 3:
        main(sys.argv[1], int(sys.argv[2]), None)
    else:
        main(sys.argv[1], int(sys.argv[2]), sys.argv[3])

