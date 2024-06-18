'''
This file contains the RandomWalk class that generates and saves the trajectories.
'''
import random
import csv
class RandomWalk:
    def __init__(self):
        self.trajectories = []
    def generate_trajectories(self):
        # Generate multiple trajectories
        for _ in range(10):
            trajectory = self.generate_trajectory()
            self.trajectories.append(trajectory)
    def generate_trajectory(self):
        # Generate a single trajectory
        trajectory = []
        x = 0
        y = 0
        for _ in range(100):
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
        return trajectory
    def save_trajectories(self, file_path):
        # Save trajectories to a CSV file
        try:
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["x", "y"])
                for trajectory in self.trajectories:
                    writer.writerows(trajectory)
            print("Trajectories saved to", file_path)
        except IOError:
            print("Error: Failed to save trajectories to", file_path)