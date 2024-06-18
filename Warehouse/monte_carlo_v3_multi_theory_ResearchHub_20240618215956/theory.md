# Multi-Trajectories Monte Carlo Random Walk

## Introduction

The multi-trajectories Monte Carlo random walk is a simulation technique used to model the movement of particles in a random environment. It is an extension of the random walk concept, where multiple particles or trajectories are generated and simulated to obtain statistical information about the system being modeled. This technique is commonly used in various fields, including physics, chemistry, finance, and computer science, to study and analyze complex systems.

## Random Walk

A random walk is a mathematical model that describes a path consisting of a sequence of random steps. In a 2D random walk, each step can be in one of four directions: up, down, left, or right. The direction of each step is chosen randomly, and the particle moves one unit in that direction. Random walks are used to model diffusion processes, such as the movement of molecules in a fluid, the foraging patterns of animals, and the spread of diseases.

## Monte Carlo Method

The Monte Carlo method is a computational technique that uses random sampling to obtain numerical results. It is based on the principle of statistical sampling, where random samples are generated from a probability distribution to estimate properties of a system. In the context of the multi-trajectories Monte Carlo random walk, the Monte Carlo method is used to generate and simulate multiple random walks to obtain statistical information about the system being modeled.

## Implementation

The provided code implements the multi-trajectories Monte Carlo random walk experiment. The `RandomWalk` class in the `random_walk.py` file is responsible for generating and saving the trajectories. The `generate_trajectories` method generates multiple trajectories by calling the `generate_trajectory` method for each trajectory. The `generate_trajectory` method generates a single trajectory by randomly choosing the direction of each step. The `save_trajectories` method saves the trajectories to a CSV file.

The `Application` class in the `main.py` file creates a GUI for the user to select an output file and run the experiment. The `select_output_file` method uses the `filedialog` module to open a file dialog for the user to select an output file. The selected file path is then displayed in the GUI. The `run_experiment` method checks if an output file has been selected and calls the `generate_trajectories` and `save_trajectories` methods of the `RandomWalk` class to generate and save the trajectories.

## Usage

To run the multi-trajectories Monte Carlo random walk experiment, follow these steps:

1. Execute the `main.py` file using a Python interpreter.
2. The GUI window will appear, showing the "Select Output File" and "Run Experiment" buttons.
3. Click the "Select Output File" button to choose a location and name for the output CSV file.
4. The selected file path will be displayed below the button.
5. Click the "Run Experiment" button to generate and save the trajectories to the selected file.
6. The program will print a message indicating the completion of the experiment and the file path where the trajectories are saved.

By running the experiment multiple times and analyzing the results, valuable insights can be gained into the behavior of the system under study.

## Conclusion

The multi-trajectories Monte Carlo random walk is a powerful simulation technique that allows for the analysis of complex systems. The provided code implements this technique by generating and saving multiple trajectories in a CSV file. By running the experiment multiple times and analyzing the results, valuable insights can be gained into the behavior of the system under study. The code structure and functionality are well-designed, providing a user-friendly interface for selecting the output file and running the experiment.