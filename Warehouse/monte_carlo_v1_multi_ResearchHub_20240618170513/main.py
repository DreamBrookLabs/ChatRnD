'''
This is the main file of the application. It contains the entry point and the GUI implementation.
'''
import tkinter as tk
from random_walk import RandomWalk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi Trajectories Monte Carlo Random Walk")
        self.geometry("400x300")
        self.random_walk = RandomWalk()
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self, text="Number of Trajectories:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Start", command=self.start_random_walk)
        self.button.pack()
    def start_random_walk(self):
        num_trajectories = int(self.entry.get())
        self.random_walk.generate_trajectories(num_trajectories)
        # Display the results or perform any other necessary actions
if __name__ == "__main__":
    app = Application()
    app.mainloop()