'''
This file serves as the entry point for the software and contains the GUI implementation.
'''
import tkinter as tk
from tkinter import filedialog
from random_walk import MultiTrajectoriesRandomWalk
from csv_writer import CSVWriter
from plotter import Plotter
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Trajectories Monte Carlo Random Walk")
        self.geometry("400x200")
        self.num_trajectories_label = tk.Label(self, text="Number of Trajectories:")
        self.num_trajectories_label.pack()
        self.num_trajectories_entry = tk.Entry(self)
        self.num_trajectories_entry.pack()
        self.run_button = tk.Button(self, text="Run Experiment", command=self.run_experiment)
        self.run_button.pack()
    def run_experiment(self):
        num_trajectories = int(self.num_trajectories_entry.get())
        random_walk = MultiTrajectoriesRandomWalk(num_trajectories)
        trajectories = random_walk.run()
        csv_writer = CSVWriter()
        csv_writer.write(trajectories)
        plotter = Plotter()
        plotter.plot(trajectories)
        plotter.save_image()
        self.show_success_message()
    def show_success_message(self):
        success_message = tk.Label(self, text="Experiment completed successfully!")
        success_message.pack()
if __name__ == "__main__":
    app = Application()
    app.mainloop()