
class Edge:

    def __init__(self, cost, node_a, node_b, id):
        self.cost = cost
        self.node_a = node_a
        self.node_b = node_b
        self.id = id
        node_b.edges_intersection.append(id)
        self.on = False
        self.on_queue = []

    def turn_on(self, edges):
        self.node_b.turn_on(self.id, edges)

    def turn_off(self):
        self.on = False
    