'''
This file contains the RandomWalk class which represents a Monte Carlo random walk.
'''
import random
class RandomWalk:
    def __init__(self):
        self.points = [(250, 250)]
    def walk(self):
        x, y = self.points[-1]
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        new_x = x + dx
        new_y = y + dy
        self.points.append((new_x, new_y))
    def reset(self):
        self.points = [(250, 250)]