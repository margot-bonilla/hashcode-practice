
class node:

    def __init__(self, id):
        self.id = id
        self.edges_intersection = []

    def turn_on(self, id_to_turn_on, edges):
        for i in self.edges_intersection:
            edges[i].on = False

        edges[id_to_turn_on].on = True