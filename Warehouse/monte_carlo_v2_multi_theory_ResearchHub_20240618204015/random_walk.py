import numpy as np
import matplotlib.pyplot as plt
class RandomWalk:
    def __init__(self, master):
        self.master = master
        self.num_trajectories = 10
        self.num_steps = 100
        self.step_size = 1
        self.plot()
    def generate_walk(self):
        walk = np.zeros((self.num_steps + 1, 2))
        for i in range(1, self.num_steps + 1):
            direction = np.random.randint(4)
            if direction == 0:
                walk[i] = walk[i - 1] + np.array([self.step_size, 0])
            elif direction == 1:
                walk[i] = walk[i - 1] + np.array([-self.step_size, 0])
            elif direction == 2:
                walk[i] = walk[i - 1] + np.array([0, self.step_size])
            else:
                walk[i] = walk[i - 1] + np.array([0, -self.step_size])
        return walk
    def plot(self):
        plt.figure(figsize=(8, 6))
        for _ in range(self.num_trajectories):
            walk = self.generate_walk()
            plt.plot(walk[:, 0], walk[:, 1])
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Multi-Trajectories Monte Carlo Random Walk")
        plt.grid(True)
        plt.show()