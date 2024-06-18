'''
This is the main file for the Monte Carlo Random Walk software.
It contains the GUI implementation using the tkinter framework.
'''
import tkinter as tk
from random_walk import RandomWalk
class MonteCarloRandomWalkApp:
    def __init__(self, master):
        self.master = master
        master.title("ResearchHub Monte Carlo Random Walk Test App")
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()
        self.start_button = tk.Button(master, text="Start", command=self.start_walk)
        self.start_button.pack()
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_walk)
        self.reset_button.pack()
        self.random_walk = RandomWalk(self.canvas)
    def start_walk(self):
        self.random_walk.start()
    def reset_walk(self):
        self.random_walk.reset()
if __name__ == "__main__":
    root = tk.Tk()
    app = MonteCarloRandomWalkApp(root)
    root.mainloop()
