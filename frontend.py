# imports for the algorithms
from Divide_and_Conquer import *


import tkinter as tk
import random
import matplotlib.pyplot as plt
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# Create a list to store the convex hull points
convex_hull_points = []

points = []  # Initialize an empty list to store points

def add_point():
    
    point_str = point_entry.get()
    
    try:
        
        x, y = map(float, point_str.split(","))
        points.append((x, y))
        update_plot()
    
    except ValueError:
        pass  # Handle invalid input

def add_random_points():

    num_points_str = num_points_entry.get()
    try:
        num_points = int(num_points_str)
        if num_points < 1:
            return
        for _ in range(num_points):
            x = random.uniform(-10, 10)  # Adjust the range as needed
            y = random.uniform(-10, 10)  # Adjust the range as needed
            points.append((x, y))
        update_plot()
    except ValueError:
        pass


def clear_points():
    
    global points
    points = []
    update_plot()


def update_plot():

    ax.clear()

    if points:
        x, y = zip(*points)
        ax.scatter(x, y, c='b', marker='o', label='Points')

    if convex_hull_points:
        convex_hull_points.append(convex_hull_points[0])  # Close the convex hull polygon
        convex_hull_x, convex_hull_y = zip(*convex_hull_points)
        ax.plot(convex_hull_x, convex_hull_y, c='r', label='Convex Hull')
        print("Convex Hull Points:")
        for point in convex_hull_points:
            print(point)

    ax.legend()
    canvas.draw()


# Function that does nothing when the button is clicked
def do_nothing():
    pass



# User Interface

# Create the main Tkinter window
root = tk.Tk()
root.title("Convex Hull Visualization")

# Create GUI elements
point_label = ttk.Label(root, text="Enter Points (x, y):")
point_label.grid(row=0, column=0, padx=5, pady=5)

point_entry = ttk.Entry(root)
point_entry.grid(row=1, column=0, padx=5, pady=5)

ttk.Button(root, text="Add Point", command=add_point).grid(row=2, column=0, padx=5, pady=5)
ttk.Button(root, text="Clear Points", command=clear_points).grid(row=3, column=0, padx=5, pady=5)  # Button to clear points

# Input field for specifying the number of random points
num_points_label = ttk.Label(root, text="Enter the number of random points:")
num_points_label.grid(row=0, column=1, padx=5, pady=5)

num_points_entry = ttk.Entry(root)
num_points_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Button(root, text="Add Random Points", command=add_random_points).grid(row=2, column=1, padx=5, pady=5)
ttk.Button(root, text="Clear Points", command=clear_points).grid(row=3, column=1, padx=5, pady=5)  # Button to clear points

ttk.Button(root, text="Divide and Conquer Algorithm", command=do_nothing).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(root, text="Algorithm 2", command=do_nothing).grid(row=1, column=2, padx=5, pady=5)
ttk.Button(root, text="Compute Convex Hull", command=divide(points)).grid(row=2, column=2, padx=5, pady=5)

# Create a Matplotlib plot in the Tkinter window
fig, ax = plt.subplots(figsize=(6, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=4, column=0, columnspan=3, padx=5, pady=5)


fig, ax = plt.subplots(figsize=(12, 12))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()


