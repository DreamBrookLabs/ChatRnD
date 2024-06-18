# Theory Review: Multi-Trajectories Monte Carlo Random Walk
## Introduction
The multi-trajectories Monte Carlo random walk is a simulation technique used to model the movement of a particle in a random environment. It is commonly used in various fields, including physics, chemistry, finance, and computer science, to study and analyze complex systems.
## Random Walk
A random walk is a mathematical model that describes a path consisting of a sequence of random steps. In a 2D random walk, each step can be in one of four directions: up, down, left, or right. The direction of each step is chosen randomly, and the particle moves one unit in that direction.
## Multi-Trajectories Monte Carlo
The multi-trajectories Monte Carlo method extends the concept of a random walk to multiple particles or trajectories. It involves generating and simulating multiple random walks to obtain statistical information about the system being modeled.
## Implementation
The provided code implements the multi-trajectories Monte Carlo random walk experiment. Here's an overview of the code structure and functionality:
- `main.py`: This file contains the main application class that creates a GUI for the user to select an output file and run the experiment.
- `random_walk.py`: This file contains the `RandomWalk` class that generates and saves the trajectories. It uses the random module to choose the direction of each step and saves the trajectories to a CSV file.
## Usage
To run the multi-trajectories Monte Carlo random walk experiment, follow these steps:
1. Execute the `main.py` file using a Python interpreter.
2. The GUI window will appear, showing the "Select Output File" and "Run Experiment" buttons.
3. Click the "Select Output File" button to choose a location and name for the output CSV file.
4. The selected file path will be displayed below the button.
5. Click the "Run Experiment" button to generate and save the trajectories to the selected file.
6. The program will print a message indicating the completion of the experiment and the file path where the trajectories are saved.
## Conclusion
The multi-trajectories Monte Carlo random walk is a powerful simulation technique that allows for the analysis of complex systems. The provided code implements this technique by generating and saving multiple trajectories in a CSV file. By running the experiment multiple times and analyzing the results, valuable insights can be gained into the behavior of the system under study.