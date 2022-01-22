
class car:

    def __init__(self, route, id, out_of_road_in = -1, is_in_queue = False):
        self.route = route
        self.out_of_road_in = out_of_road_in
        self.id = id

        self.is_in_queue = is_in_queue

    def traffic_light(self, is_green, time_on_simulation, verbose = False):

        if is_green and self.out_of_road_in - time_on_simulation <= 0 and self.is_in_queue == False:
            if self.route[0].cost == 0:
                self.in_road(self.route[1].cost, time_on_simulation)
                if verbose:
                    print("Car ", str(self.id), " has passed the road " + str(
                        self.route[1].id) + " without waitting and it's going to stay in the next road for " + str(
                        self.route[1].cost) + " secods")
                self.route.pop(0)
                self.route.pop(0)

            else:
                self.in_road(self.route[0].cost, time_on_simulation)
                if verbose:
                    print("Car ", str(self.id), " has passed the road " + str(
                        self.route[0].id) + " without waitting and it's going to stay in the next road for " + str(
                        self.route[0].cost) + " secods")
                self.route.pop(0)




        elif not is_green and self.out_of_road_in - time_on_simulation <= 0:
            if self.is_in_queue == False:
                self.route[0].on_queue.append(self)
                self.is_in_queue = True
                if verbose:
                    print("Car ", str(self.id), " is still waitting because the traffic light of the road " + str(
                        self.route[0].id) + " is red :'( ")


        elif is_green and self.out_of_road_in - time_on_simulation <= 0 and self.route[0].on_queue[0].id == self.id:
            if self.route[0].cost == 0:
                self.in_road(self.route[1].cost, time_on_simulation)
                if verbose:
                    print("Car ", str(self.id),
                          " has leaved the queue of the red traffic light!. Now it's passing through the road " + str(
                              self.route[1].id) + " and it will take ", str(
                            self.route[1].cost))
            else:
                self.in_road(self.route[0].cost, time_on_simulation)
                if verbose:
                    print("Car ", str(self.id),
                          " has leaved the queue of the red traffic light!. Now it's passing through the road " + str(
                              self.route[0].id) + " and it will take ", str(
                            self.route[0].cost))

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

    def destroy(self, time_on_simulation, max_time_simulation, car_score, verbose = False):
        if len(self.route) == 0 and self.out_of_road_in - time_on_simulation <= 0:
            self.out_of_road_in = max_time_simulation + 1
            if verbose:
                print("Car "+ str(self.id) + " has arrived at time " + str(time_on_simulation)+ "! So the score for this car is: "+ str(car_score + (max_time_simulation - 1 - time_on_simulation)))
            return car_score + (max_time_simulation - 1 - time_on_simulation)
        else:
            return 0

    def __str__(self):
        return str(self.id)