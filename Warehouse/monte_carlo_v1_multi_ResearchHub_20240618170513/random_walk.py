'''
This file contains the RandomWalk class which generates multiple trajectories.
'''
import random
class RandomWalk:
    def __init__(self):
        self.trajectories = []
    def generate_trajectories(self, num_trajectories):
        self.trajectories = []
        for _ in range(num_trajectories):
            trajectory = self.generate_trajectory()
            self.trajectories.append(trajectory)
    def generate_trajectory(self):
        '''
        Generate a single trajectory for the random walk.
        The trajectory will stay within the boundaries of -10 to 10 in both x and y directions.
        '''
        trajectory = []
        x = 0
        y = 0
        for _ in range(100):
            direction = random.choice(["up", "down", "left", "right"])
            if direction == "up" and y < 10:
                y += 1
            elif direction == "down" and y > -10:
                y -= 1
            elif direction == "left" and x > -10:
                x -= 1
            elif direction == "right" and x < 10:
                x += 1
            else:
                break  # Break out of the loop if the boundaries are reached
            trajectory.append((x, y))
        return trajectory