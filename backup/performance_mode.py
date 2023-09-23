# imports for the algorithms
# from divide_and_conquer_algorithm.divide_and_conquer import *


import tkinter as tk
import random
import time


from tkinter import ttk
from tkinter.scrolledtext import ScrolledText  # Import ScrolledText for multi-line text display
from tkinter.font import Font



## Create a list to store the convex hull points
convex_hull_points = []

points = [] # Initialize an empty list to store points

# Variables to store the elapsed times of each algorithm
divide_and_conquer_time = 0.0
algorithm2_time = 100.0


def add_point():
    
    point_str = point_entry.get()
    
    try:
        
        x, y = map(float, point_str.split(","))
        points.append((x, y))
        point_entry.delete(0, tk.END)  # Clear the input field after adding a point
        display_point_count()
    except ValueError:
        pass  # Handle invalid input

def add_random_points():

    num_points_str = num_points_entry.get()
    try:
        num_points = int(num_points_str)
        if num_points < 1:
            return
        for _ in range(num_points):
            x = random.uniform(-500.0, 500.0)  # Adjust the range as needed
            y = random.uniform(-500.0, 500.0)  # Adjust the range as needed
            points.append((x, y))
            display_point_count()

    except ValueError:
        pass

def add_point_on_enter(event):

    add_point()

def add_random_points_on_enter(event):

    add_random_points()    


def clear_points():
    
    global points
    points = []
    display_point_count()

# Create a function to display the current number of points
def display_point_count():
    point_count_label.config(text=f"Number of Points: {len(points)}")


# Function to run two commands
def run_both_commands():

    # Call the first command
    divide_and_conquer_convex_hull()

    # Call the second command
    divide_and_conquer_convex_hull() # change to algo number 2

# Function to update the faster_algorithm_label
def update_faster_algorithm_label():
    global divide_and_conquer_time, algorithm2_time
    
    if divide_and_conquer_time < algorithm2_time:
        faster_algorithm_label.config(text=f"Divide and Conquer Algorithm with {divide_and_conquer_time:.4f} seconds")
    else:
        faster_algorithm_label.config(text=f"Algorithm 2 with {algorithm2_time:.4f} seconds")

# Function that does nothing when the button is clicked
def do_nothing():
    pass


##########################################################################################################################
# Divide and Conquer Methods

## OPTIONL ? MERGESORT SELBER IMPLEMENTIEREN ODER EINFACH SORT() BENUTZEN?
def divide_and_conquer_convex_hull():
    
    # Record the start time
    start_time = time.time()

    points.sort()

    global convex_hull_points
    # convex_hull_points = divide(points)

    global divide_and_conquer_time 
    # Calculate the elapsed time
    divide_and_conquer_time = time.time() - start_time

    # Clear existing text in the Text widget
    dac_convex_hull_text.delete(1.0, tk.END)
    convex_hull_text.delete(1.0, tk.END)
    
    # Insert the convex hull points into the Text widget
    for point in convex_hull_points:

        dac_convex_hull_text.insert(tk.END, f"({point[0]}, {point[1]})\n")
        convex_hull_text.insert(tk.END, f"({point[0]}, {point[1]})\n")
    

    # Update the elapsed time label
    dac_elapsed_time_label.config(text=f"Elapsed Time Divide And Conquer Algorithm: {divide_and_conquer_time:.4f} seconds")
    
    # Determine the faster algorithm and update the label
    update_faster_algorithm_label()


    # Update the elapsed time label
    elapsed_time_label.config(text=f"Elapsed Time: {divide_and_conquer_time:.4f} seconds")



##########################################################################################################################
# Second Algorithm



##########################################################################################################################

# User Interface

# Create the main Tkinter window for the performance optimized mode
root = tk.Tk()
root.title("Performance Optimized Mode")

# Create GUI elements
point_label = ttk.Label(root, text="Enter Points (x.0, y.0):")
point_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

point_entry = ttk.Entry(root)
point_entry.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
point_entry.bind("<Return>", add_point)  # Bind the Enter key to add_point

ttk.Button(root, text="Add Point", command=add_point).grid(row=2, column=0, padx=5, pady=5, columnspan=2)

# Input field for specifying the number of random points
num_points_label = ttk.Label(root, text="Enter the number of random points:")
num_points_label.grid(row=0, column=2, padx=5, pady=5, columnspan=2)

num_points_entry = ttk.Entry(root)
num_points_entry.grid(row=1, column=2, padx=5, pady=5, columnspan=2)
num_points_entry.bind("<Return>", add_random_points)  # Bind the Enter key to add_random_points

add_random_button = ttk.Button(root, text="Add Random Points", command=add_random_points)
add_random_button.grid(row=2, column=2, padx=5, pady=5, columnspan=2)

ttk.Button(root, text="Divide and Conquer Algorithm", command=divide_and_conquer_convex_hull).grid(row=3, column=0, padx=5, pady=5)
ttk.Button(root, text="Algorithm 2", command=do_nothing).grid(row=3, column=1, padx=5, pady=5)
ttk.Button(root, text="Compare both Algorithms", command=run_both_commands).grid(row=3, column=2, padx=5, pady=5)
ttk.Button(root, text="Clear Points", command=clear_points).grid(row=3, column=3, padx=5, pady=5)  # Button to clear points

# Create a label to display the point count
point_count_label = ttk.Label(root, text="Number of Points: 0")
point_count_label.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Create a custom bold font
bold_font = Font(family="Helvetica", size=12, weight="bold")


# Create Text widgets to display the points from the convex hull
dac_convex_hull_label = ttk.Label(root, text="Divide And Conquer Convex Hull Points:")
dac_convex_hull_label.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

dac_convex_hull_text = ScrolledText(root, height=10, width=40)
dac_convex_hull_text.grid(row=6, column=0, columnspan=4, padx=10, pady=5)

# Create a label to display the elapsed time
dac_elapsed_time_label = ttk.Label(root, text="Elapsed Time: 0.0000 seconds", font=bold_font)
dac_elapsed_time_label.grid(row=7, column=0, columnspan=4, padx=10, pady=10)


# Create Text widgets to display the points from the convex hull
convex_hull_label = ttk.Label(root, text="Algorithm 2 Convex Hull Points:")
convex_hull_label.grid(row=8, column=0, columnspan=4, padx=10, pady=5)

convex_hull_text = ScrolledText(root, height=10, width=40)
convex_hull_text.grid(row=9, column=0, columnspan=4, padx=10, pady=5)

# Create a label to display the elapsed time
elapsed_time_label = ttk.Label(root, text="Elapsed Time: 0.0000 seconds", font=bold_font)
elapsed_time_label.grid(row=10, column=0, columnspan=4, padx=10, pady=10)

# Create a label to display the faster algorithm
faster_algorithm_label = ttk.Label(root, text="Faster Algorithm: N/A", font=bold_font)
faster_algorithm_label.grid(row=11, column=0, columnspan=4, padx=10, pady=10)


# Run the Tkinter main loop for the performance optimized mode
root.mainloop()
