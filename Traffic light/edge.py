
class Edge:

    def __init__(self, cost, road_a, road_b, id):
        self.cost = cost
        self.road_a = road_a
        self.road_b = road_b
        self.id = id

        self.on = False
        self.on_queue = []

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False
    