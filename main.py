import tkinter as tk
from tkinter import ttk
import subprocess  # Used to run external scripts

# Create a function to open the visual mode
def open_visual_mode():

    try:
        subprocess.run(["python", "visual_mode.py"])
    except FileNotFoundError:
        print("Visual mode script not found. Please create visual_mode.py.")

# Create a function to open the performance optimized mode
def open_optimized_mode():
    try:
        subprocess.run(["python", "performance_mode.py"])
    except FileNotFoundError:
        print("Optimized mode script not found. Please create optimized_mode.py.")

# Create the main Tkinter window for the home screen
root = tk.Tk()
root.title("Convex Hull Algorithm Home")

# Create labels to describe the options
visual_mode_label = ttk.Label(root, text="Visual Mode:")
optimized_mode_label = ttk.Label(root, text="Performance Optimized Mode:")

# Create buttons to open the respective modes
visual_mode_button = ttk.Button(root, text="Open Visual Mode", command=open_visual_mode)
optimized_mode_button = ttk.Button(root, text="Open Performance Optimized Mode", command=open_optimized_mode)

# Grid layout for labels and buttons
visual_mode_label.grid(row=0, column=0, padx=10, pady=10)
visual_mode_button.grid(row=0, column=1, padx=10, pady=10)
optimized_mode_label.grid(row=1, column=0, padx=10, pady=10)
optimized_mode_button.grid(row=1, column=1, padx=10, pady=10)

# Run the Tkinter main loop for the home screen
root.mainloop()