import tkinter as tk
from random_walk import RandomWalk
def main():
    # Create the GUI window
    window = tk.Tk()
    window.title("Monte Carlo Random Walk")
    # Create an instance of the RandomWalk class
    random_walk = RandomWalk()
    # Create a canvas to display the random walk
    canvas = tk.Canvas(window, width=500, height=500)
    canvas.pack()
    # Create a button to start the random walk
    start_button = tk.Button(window, text="Start", command=random_walk.walk)
    start_button.pack()
    # Create a button to reset the random walk
    reset_button = tk.Button(window, text="Reset", command=random_walk.reset)
    reset_button.pack()
    # Start the GUI event loop
    window.mainloop()
if __name__ == "__main__":
    main()