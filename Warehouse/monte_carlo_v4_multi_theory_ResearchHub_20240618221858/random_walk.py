'''
This file contains the implementation of the multi-trajectories Monte Carlo random walk.
'''
import random
class MultiTrajectoriesRandomWalk:
    def __init__(self, num_trajectories):
        self.num_trajectories = num_trajectories
    def run(self):
        trajectories = []
        for _ in range(self.num_trajectories):
            trajectory = self.generate_trajectory()
            trajectories.append(trajectory)
        return trajectories
    def generate_trajectory(self):
        trajectory = [(0, 0)]
        while True:
            x, y = trajectory[-1]
            direction = random.choice(["up", "down", "left", "right"])
            if direction == "up":
                y += 1
            elif direction == "down":
                y -= 1
            elif direction == "left":
                x -= 1
            elif direction == "right":
                x += 1
            trajectory.append((x, y))
            if self.is_out_of_bounds(x, y):
                break
        return trajectory
    def is_out_of_bounds(self, x, y):
        return abs(x) > 10 or abs(y) > 10