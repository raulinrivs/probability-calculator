import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, amount in kwargs.items():
            for x in range(amount):
                self.contents.append(color)

    def draw(self, amount):
        sorted_balls = []
        for x in range(amount):
            balls_count = len(self.contents)
            if balls_count > 0:
                index = random.randint(0, balls_count - 1)
                sorted_balls.append(self.contents[index])
                self.contents.pop(index)
        return sorted_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_attempts = 0
    for attempt in range(num_experiments):  # Loop experiment
        flag = True
        aux_hat = copy.deepcopy(hat)
        sorted_balls = aux_hat.draw(num_balls_drawn)
        for color, amount in expected_balls.items():  # Loop draw
            if flag:
                for x in range(amount):  # Loop color
                    if color in sorted_balls:
                        sorted_balls.remove(color)
                    else:
                        flag = False
                        break
        if flag:
            successful_attempts += 1
    teste = successful_attempts / num_experiments
    return teste








