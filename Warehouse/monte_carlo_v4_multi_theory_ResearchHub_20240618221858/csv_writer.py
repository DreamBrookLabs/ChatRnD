'''
This file handles the generation of the CSV output file.
'''
import csv
from tkinter import filedialog
class CSVWriter:
    def write(self, trajectories):
        filename = filedialog.asksaveasfilename(defaultextension=".csv")
        if not filename:  # Check if the user cancels the file dialog
            return
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["x", "y"])
            for trajectory in trajectories:
                for x, y in trajectory:
                    writer.writerow([x, y])