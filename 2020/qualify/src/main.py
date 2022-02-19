from entities.library import Library
from entities.problem import Problem


def load_problem(file_name):
    with open(file_name) as f:
        B, L, D = map(int, f.readline().split())
        scores = map(int, f.readline().split())
        p = Problem(B, L, D, scores)

        for _ in range(L):
            lib_n_books, lib_signup, lib_ship = map(int, f.readline().split())
            lib_books = map(int, f.readline().split())
            lib = Library(lib_n_books, lib_signup, lib_ship, lib_books)
            p.add_library(lib)
        return p


if __name__ == "__main__":
    print("Welcome to the Google Books Challenge")

    problem_1 = load_problem("../input/a_example.txt")
    print(problem_1)
    problem_2 = load_problem("../input/b_read_on.txt")
    print(problem_2)




