import sys


class Client:
    def __init__(self):
        self.id = id(self)
        self.likes = set()
        self.dislikes = set()

    def is_good_pizza(self, pizza):
        return len(self.likes - pizza) == 0 and len(pizza - self.dislikes) == len(pizza)


class Ingredient:
    def __init__(self, name):
        self.id = id(self)
        self.name = name
        self.client_likes = set()
        self.client_dislikes = set()


def fill_ingredients(client, ingredients, ingredients_to_check, ingredients_lookup, liked):
    total_ingredients = set()
    for liked_ingredient in ingredients_to_check:
        if liked_ingredient not in ingredients_lookup:
            ingredients_lookup[liked_ingredient] = Ingredient(liked_ingredient)
            ingredients.append(ingredients_lookup[liked_ingredient])
        if liked:
            ingredients_lookup[liked_ingredient].client_likes.add(client)
        else:
            ingredients_lookup[liked_ingredient].client_dislikes.add(client)

        total_ingredients.add(ingredients_lookup[liked_ingredient].id)

    return total_ingredients


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
    ingredients = []
    ingredients_lookup = dict()

    # Read the file into variables    
    with open(in_file, 'r') as infile:
        number_of_clients = int(infile.readline())
        for client in range(number_of_clients):
            client = Client()
            client.likes = fill_ingredients(client, ingredients, infile.readline().strip().split(' ')[1:], ingredients_lookup, True)
            client.dislikes = fill_ingredients(client, ingredients, infile.readline().strip().split(' ')[1:], ingredients_lookup, False)
            clients.append(client)

    return clients


def process(result_params):
    """
    The main program reads the input file, processes the calculation
    and writes the output file

    Args:
        result_params: Resulted Parameters  

    Returns:
        final_score: Final Score
        , final_result: Final Result    
    """
    final_score = 0
    final_result = []

    ### Logic here

    return final_score, final_result    # return process result


def write_file(out_file, final_result):
    """
    Write the submission file

    Args:
        out_file: output file path
    """
    with open(out_file, 'w') as outfile:
        # Save result into the output file
        pass


def main(in_file, out_file):
    """
    The main program reads the input file, processes the calculation
    and writes the output file

    Args:
        in_file: input file path
        out_file: output file path
    """

    # Read File
    result_params = read_file(in_file)
    # Process Algorithm
    final_score, final_result = process(result_params)
    # Print Score
    print('Score: {}'.format(final_score))
    # Save results into the output if instructed
    if out_file is not None:
        write_file(out_file, final_result)
        print('{} is saved. The program completed.'.format(out_file))
    else:
        print('The program completed.')


if __name__ == "__main__":
    # test
    main('input_data/a_an_example.in.txt', None)


    # Check arguments
    # if len(sys.argv) < 2:
    #     print(sys.argv[0] + ' [in file] [out file: optional]')
    # elif len(sys.argv) == 2:
    #     main(sys.argv[1], None)
    # else:
    #     main(sys.argv[1], sys.argv[2])

### End of Program ###