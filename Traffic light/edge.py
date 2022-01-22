
class Edge:

    def __init__(self, cost, node_a, node_b, id, Edge = None, on_queue = None):
        if Edge is None:
            self.cost = cost
            self.node_a = node_a
            self.node_b = node_b
            self.id = id
            node_b.edges_intersection.append(id)
            self.on = False
            self.on_queue = []
        else:
            self.cost = cost
            self.node_a = Edge.node_a
            self.node_b = Edge.node_b
            self.id = Edge.id
            Edge.node_b.edges_intersection.append(Edge.id)
            self.on = Edge.on
            self.on_queue = on_queue

    def turn_on(self, edges):
        self.node_b.turn_on(self.id, edges)

    def turn_off(self):
        self.on = False

    def __str__(self):
        return str(self.id)
    