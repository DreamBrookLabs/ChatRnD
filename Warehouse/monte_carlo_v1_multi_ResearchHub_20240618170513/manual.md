# Multi Trajectories Monte Carlo Random Walk

## Introduction

The Multi Trajectories Monte Carlo Random Walk application is a Python-based program that generates multiple trajectories for a random walk. It uses the Monte Carlo method to simulate the movement of a particle in a 2D space. The application provides a graphical user interface (GUI) for easy interaction and visualization of the generated trajectories.

## Installation

To use the Multi Trajectories Monte Carlo Random Walk application, you need to follow these steps:

1. Install Python: Make sure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/downloads/).

2. Install dependencies: Open a terminal or command prompt and navigate to the directory where the application files are located. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary dependencies, including NumPy and pandas.

## Usage

Once you have installed the dependencies, you can run the application by executing the `main.py` file. This will launch the GUI window.

1. Number of Trajectories: Enter the desired number of trajectories in the text entry field.

2. Start: Click the "Start" button to generate the trajectories.

   - The trajectories will be generated using the Monte Carlo method and displayed in the GUI window.

   - Each trajectory consists of a series of points representing the movement of the particle in the 2D space.

   - The particle starts at the origin (0, 0) and can move up, down, left, or right within the boundaries of -10 to 10 in both x and y directions.

   - The trajectories will be stored in memory and can be accessed for further analysis or visualization.

3. Display the Results: You can perform any necessary actions with the generated trajectories, such as displaying them on a plot, analyzing statistical properties, or saving them to a file.

## Example

Here is an example of how to use the Multi Trajectories Monte Carlo Random Walk application:

1. Install Python and the required dependencies as described in the Installation section.

2. Run the `main.py` file.

3. In the GUI window, enter the number of trajectories you want to generate (e.g., 10).

4. Click the "Start" button.

5. The application will generate 10 trajectories using the Monte Carlo method.

6. Perform any necessary actions with the generated trajectories, such as plotting them using a library like Matplotlib or analyzing their statistical properties using NumPy and pandas.

## Conclusion

The Multi Trajectories Monte Carlo Random Walk application provides a convenient way to generate and visualize multiple trajectories for a random walk. It utilizes the Monte Carlo method to simulate the movement of a particle in a 2D space. By following the installation instructions and using the provided GUI, you can easily generate trajectories and perform further analysis or visualization.