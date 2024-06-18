'''
This is the main file that initializes the application and creates the GUI window.
'''
import tkinter as tk
from random_walk import RandomWalk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Trajectories Monte Carlo Random Walk")
        self.geometry("400x300")
        self.random_walk = RandomWalk(self)
        self.random_walk.plot()
if __name__ == "__main__":
    app = Application()
    app.mainloop()