from random import choice


class RandomWalk:
    def __init__(self, num_points=55000):
        self.num_points = num_points
        self.x_val = [0]
        self.y_val = [0]

    def fill_walk(self):

        while len(self.x_val) < self.num_points:
            if self.x_val[-1] > 100:
                x_step = choice([0, -1, -2, -3, -4])
            elif self.x_val[-1] < -100:
                x_step = choice([0, 1, 2, 3, 4])
            else:
                x_direction = choice([1, -1])
                x_distance = choice([0, 1, 2, 3, 4])
                x_step = x_direction * x_distance

            if self.y_val[-1] > 100:
                y_step = choice([0, -1, -2, -3, -4])
            elif self.y_val[-1] < -100:
                y_step = choice([0, 1, 2, 3, 4])
            else:
                y_direction = choice([1, -1])
                y_distance = choice([0, 1, 2, 3, 4])
                y_step = y_direction * y_distance

            next_x = self.x_val[-1] + x_step
            next_y = self.y_val[-1] + y_step

            self.x_val.append(next_x)
            self.y_val.append(next_y)
