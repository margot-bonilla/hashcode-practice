
class car:

    def __init__(self, route, id):
        self.route = route
        self.out_of_road_in = -1
        self.id = id

        self.is_in_queue = False

    def traffic_light(self, is_green, time_on_simulation):

        if is_green and self.out_of_road_in - time_on_simulation <= 0 and self.is_in_queue == False:
            self.in_road(self.route[0].cost, time_on_simulation)
            self.route.pop(0)

        elif not is_green and self.out_of_road_in - time_on_simulation <= 0:
            if self.is_in_queue == False:
                self.route[0].on_queue.append(self)
                self.is_in_queue = True

        elif is_green and self.out_of_road_in - time_on_simulation <= 0 and self.route[0].on_queue[0].id == self.id:
            self.in_road(self.route[0].cost, time_on_simulation)
            self.route[0].on_queue.pop(0)

            for i in self.route[0].on_queue:
                i.out_of_road_in = time_on_simulation

            self.route.pop(0)
            self.is_in_queue = False

    def in_road(self, time_in_road, time_ini):
        self.out_of_road_in = time_ini + time_in_road

    def destroy(self, time_on_simulation):
        if len(self.route) == 0 and self.out_of_road_in - time_on_simulation <= 0:
            self.out_of_road_in = 99999