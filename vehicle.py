import math


class Vehicle:

    def __init__(self):
        self.movements = []
        self.average_speed = 0
        self.distance_driven = 0
        self.distance_from_start = 0
        self.total_time = 0
        self.current_pos = (0, 0)

    def record_movement(self, movement_record):
        self.movements.append(movement_record)

        # average speed = total distance/total time
        distance_travled_since_last_movement = movement_record['speed'] * movement_record['time']
        self.distance_driven += distance_travled_since_last_movement
        self.total_time += movement_record['time']
        self.average_speed = round(self.distance_driven / self.total_time, 2)

        rad = math.radians(movement_record['heading'])
        x = self.current_pos[0] + (distance_travled_since_last_movement * math.cos(rad))
        y = self.current_pos[1] + (distance_travled_since_last_movement * math.sin(rad))
        self.current_pos = (x, y)

        self.distance_from_start = round(math.sqrt(x ** 2 + y ** 2), 2)

    def get_estimate(self):
        return self.average_speed, self.distance_driven, self.distance_from_start

    def get_movements_data(self):
        return self.movements