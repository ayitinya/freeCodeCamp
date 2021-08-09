import copy
import random


class Hat:

    def __init__(self, **kwargs):
        self.contents = list()
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number_of_balls):
        choices = []
        if number_of_balls >= len(self.contents):
            return self.contents
        else:
            for _ in range(number_of_balls):
                ball = random.choice(self.contents)
                choices.append(ball)
                self.contents.remove(ball)

        return choices


def experiment(hat, expected_balls: dict, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        temp_list = hat_copy.draw(num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if temp_list.count(key) < value:
                success = False
                break
        if success:
            count += 1
    return count / num_experiments


if __name__ == "__main__":
    collection = Hat(blue=3, red=2, green=2)
    collection.draw(3)
