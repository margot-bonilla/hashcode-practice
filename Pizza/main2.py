import sys
from multiprocessing import Process, Queue
from collections import defaultdict
import copy


class Client:
    def __init__(self, likes, dislikes):
        self.likes = likes
        self.dislikes = dislikes


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
        products_liked = set()
        products_disliked = set()
        products_total = set()
        for client in range(number_of_clients):
            likes = infile.readline().strip().split(' ')[1:]
            dislikes = infile.readline().strip().split(' ')[1:]
            clients.append(Client(likes, dislikes))

            products_liked = products_liked.union(likes)
            products_disliked = products_disliked.union(dislikes)
            products_total = products_total.union(likes).union(dislikes)

    return clients, list(products_total), list(products_liked), list(products_disliked)


def write_file(out_file, final_result):
    """
    Write the submission file

    Args:
        out_file: output file path
        final_result: list with the result
    """
    with open(out_file, 'w') as outfile:
        outfile.write(f'{len(final_result)} {" ".join(final_result)}')


def get_picky_clients(clients):
    picky_clients = defaultdict(int)
    picky_products = defaultdict(int)
    for client in clients:
        picky_clients['_'.join(sorted(client.dislikes))] += 1
        for product in client.dislikes:
            picky_products[product] += 1

    # return dict(sorted(picky_clients.items(), key=lambda item: item[1])[::-1])
    return dict(sorted(picky_products.items(), key=lambda item: item[1]))


def algorithm(clients, products_total, products_liked, products_disliked, q, seed):
    best_pizza = set()
    best_points, happy_clients, unhappy_clients = get_score(clients, best_pizza)

    # picky_clients = get_picky_clients(clients)

    pizza = set()
    for unhappy_client in unhappy_clients:
        pizza = pizza.union(set(unhappy_client.likes))
        pizza.discard(set(unhappy_client.dislikes))

        new_score, happy_clients, unhappy_clients = get_score(clients, pizza)
        if new_score > best_points:
            best_points = new_score
            best_pizza = copy.deepcopy(pizza)

    return list(best_pizza), best_points


def get_score(clients, pizza):
    score = 0
    happy_clients = []
    unhappy_clients = []
    for client in clients:
        if len(set(client.likes) - set(pizza)) == 0 and len(set(pizza) - set(client.dislikes)) == len(pizza):
            score += 1
            happy_clients.append(client)
        else:
            unhappy_clients.append(client)

    return score, happy_clients, unhappy_clients


def main(in_file, process_count, out_file):
    """
    The main program reads the input file, processes the calculation
    and writes the output file

    Args:
        in_file: input file path
        out_file: output file path
    """

    # Read File
    clients, products_total, products_liked, products_disliked = read_file(in_file)
    print(f"We have a total of {len(products_total)} products")
    print(f"We have a total of {len(products_liked)} products liked")
    print(f"We have a total of {len(products_disliked)} products disliked")

    # Process Algorithm
    final_result, final_score = algorithm(clients, products_total, products_liked, products_disliked, 0, 0)

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
    main('input_data/a_an_example.in.txt', 1, 'output_data/a_an_example.out.txt')
    main('input_data/b_basic.in.txt', 1, 'output_data/b_basic.out.txt')
    main('input_data/c_coarse.in.txt', 1, 'output_data/c_coarse.out.txt')
    main('input_data/d_difficult.in.txt', 1, 'output_data/d_difficult.out.txt')
    # main('input_data/e_elaborate.in.txt', 1, 'output_data/e_elaborate.out.txt')
    # if len(sys.argv) < 2:
    #     print(sys.argv[0] + ' [in file] [out file: optional]')
    # elif len(sys.argv) == 2:
    #     main(sys.argv[1], 1, None)
    # elif len(sys.argv) == 3:
    #     main(sys.argv[1], int(sys.argv[2]), None)
    # else:
    #     main(sys.argv[1], int(sys.argv[2]), sys.argv[3])

