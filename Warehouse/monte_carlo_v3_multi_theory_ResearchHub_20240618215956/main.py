'''
This is the main file that will be executed to run the multi-trajectories Monte Carlo random walk experiment.
'''
import tkinter as tk
from tkinter import filedialog
from random_walk import RandomWalk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Trajectories Monte Carlo Random Walk")
        self.geometry("400x200")
        self.output_file_path = ""
        self.create_widgets()
    def create_widgets(self):
        self.output_label = tk.Label(self, text="Output File:")
        self.output_label.pack()
        self.selected_file_label = tk.Label(self, text="")
        self.selected_file_label.pack()
        self.output_button = tk.Button(self, text="Select Output File", command=self.select_output_file)
        self.output_button.pack()
        self.run_button = tk.Button(self, text="Run Experiment", command=self.run_experiment)
        self.run_button.pack()
    def select_output_file(self):
        self.output_file_path = filedialog.asksaveasfilename(defaultextension=".csv")
        self.selected_file_label.config(text=self.output_file_path)
    def run_experiment(self):
        if self.output_file_path:
            random_walk = RandomWalk()
            random_walk.generate_trajectories()
            random_walk.save_trajectories(self.output_file_path)
            print("Experiment completed and trajectories saved.")
        else:
            print("Please select an output file.")
if __name__ == "__main__":
    app = Application()
    app.mainloop()