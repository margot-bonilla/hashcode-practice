class Ingredient:
    def __init__(self, name):
        self.id = id(self)
        self.name = name
        self.client_likes = set()
        self.client_dislikes = set()

