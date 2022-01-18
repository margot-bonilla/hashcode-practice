class Problem:
    def __init__(self, B, L, D, scores):
        self.B = B
        self.D = D
        self.L = L

        self.scores = scores
        self.libraries = []

    def add_library(self, library):
        self.libraries.append(library)

    def solve(self):
        pass

