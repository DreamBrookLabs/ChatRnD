'''
This file contains the RandomWalk class which handles the random walk simulation.
'''
import random
import tkinter as tk
from itertools import cycle

class RandomWalk:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 250
        self.y = 250
        self.colors = cycle(['red', 'green', 'blue', 'yellow', 'purple', 'orange'])

    def start(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for _ in range(1000):
            dx, dy = random.choice(directions)
            color = next(self.colors)
            self.canvas.create_line(self.x, self.y, self.x + dx, self.y + dy, fill=color)
            self.x += dx
            self.y += dy

    def reset(self):
        self.canvas.delete("all")
        self.x = 250
        self.y = 250

# Example usage with tkinter
def main():
    root = tk.Tk()
    root.title("Random Walk")
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    random_walk = RandomWalk(canvas)

    start_button = tk.Button(root, text="Start", command=random_walk.start)
    start_button.pack(side=tk.LEFT)

    reset_button = tk.Button(root, text="Reset", command=random_walk.reset)
    reset_button.pack(side=tk.RIGHT)

    root.mainloop()

if __name__ == "__main__":
    main()
