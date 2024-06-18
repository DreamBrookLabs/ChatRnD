'''
This file handles the plotting and saving of the result as an image.
'''
import matplotlib.pyplot as plt
from datetime import datetime
class Plotter:
    def plot(self, trajectories):
        plt.figure(figsize=(8, 8))
        for trajectory in trajectories:
            x_values = [x for x, _ in trajectory]
            y_values = [y for _, y in trajectory]
            plt.plot(x_values, y_values)
        plt.title("Multi-Trajectories Monte Carlo Random Walk")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
    def save_image(self):
        filename = f"image_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        plt.savefig(filename)