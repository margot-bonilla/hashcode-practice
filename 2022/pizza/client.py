class Client:
    def __init__(self):
        self.id = id(self)
        self.likes = set()
        self.dislikes = set()

    def is_good_pizza(self, pizza):
        return len(self.likes - pizza) == 0 and len(pizza - self.dislikes) == len(pizza)

