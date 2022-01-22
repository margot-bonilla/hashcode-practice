
class car:

    def __init__(self, route, id, out_of_road_in = -1, is_in_queue = False):
        self.route = route
        self.out_of_road_in = out_of_road_in
        self.id = id

        self.is_in_queue = is_in_queue

    def traffic_light(self, is_green, time_on_simulation):

        if is_green and self.out_of_road_in - time_on_simulation <= 0 and self.is_in_queue == False:
            if self.route[0].cost == 0:
                self.in_road(self.route[1].cost, time_on_simulation)
                self.route.pop(0)
                self.route.pop(0)
            else:
                self.in_road(self.route[0].cost, time_on_simulation)
                self.route.pop(0)

        elif not is_green and self.out_of_road_in - time_on_simulation <= 0:
            if self.is_in_queue == False:
                self.route[0].on_queue.append(self)
                self.is_in_queue = True

        elif is_green and self.out_of_road_in - time_on_simulation <= 0 and self.route[0].on_queue[0].id == self.id:
            if self.route[0].cost == 0:
                self.in_road(self.route[1].cost, time_on_simulation)
            else:
                self.in_road(self.route[0].cost, time_on_simulation)

            self.route[0].on_queue.pop(0)

            for i in self.route[0].on_queue:
                i.out_of_road_in = time_on_simulation

            if self.route[0].cost == 0:
                self.route.pop(0)
                self.route.pop(0)
            else:
                self.route.pop(0)

            self.is_in_queue = False

    def in_road(self, time_in_road, time_ini):
        self.out_of_road_in = time_ini + time_in_road

    def destroy(self, time_on_simulation, max_time_simulation, car_score):
        if len(self.route) == 0 and self.out_of_road_in - time_on_simulation <= 0:
            self.out_of_road_in = max_time_simulation + 1
            return car_score + (max_time_simulation + 1 - time_on_simulation)
        else:
            return 0

    def __str__(self):
        return str(self.id)