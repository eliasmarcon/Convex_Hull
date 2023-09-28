import tkinter as tk
import matplotlib.pyplot as plt

from quickhull_folder.quickhull import *
from giftwrapping_folder.giftwrapping import *
from additional_files import modules

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, filedialog, Grid


POINTS = []  # Initialize an empty list to store points

# Function to add a point
def add_point():

    point_str = point_entry.get()
    modules.check_input_point(point_str)  # Validate input
    x, y = map(float, point_str.split(","))  # Convert input to float
    POINTS.append((x, y))  # Add point to the list
    update_plot()  # Update the plot with the new point
    display_point_count()  # Update the point count label
    point_entry.delete(0, tk.END)  # Clear the input field after adding a point

# Function to add random points
def add_random_points():

    num_points_str = num_points_entry.get()
    modules.check_input(num_points_str)  # Validate input
    num_points = int(num_points_str)
    global POINTS
    POINTS = modules.generate_points(num_points, POINTS)  # Generate random points
    update_plot()  # Update the plot with the new points
    display_point_count()  # Update the point count label

# Function to add a point on pressing Enter
def add_point_on_enter(event):

    add_point()

# Function to add random points on pressing Enter
def add_random_points_on_enter(event):

    add_random_points()

# Function to clear all points
def clear_points():

    global POINTS
    POINTS = []  # Clear the list of points
    update_plot()  # Clear the plot
    display_point_count()  # Reset the point count label

# Function to update the plot
def update_plot():
    
    ax.clear()
    if POINTS:
        x, y = zip(*POINTS)
        ax.scatter(x, y, c='b', marker='o', label='Points', s=4)  # Plot points
    canvas.draw()

# Function to display the current number of points
def display_point_count():

    point_count_label.config(text=f"Number of Points: {len(POINTS)}")  # Update the point count label

# Function to run the Quickhull algorithm
def quickhull_run(fig, ax, canvas, root, POINTS):

    convex_hull = quickhull(fig, ax, canvas, root, POINTS)  # Run Quickhull algorithm

# Function to run the Giftwrapping algorithm
def giftwrapping_run(ax, canvas, root, POINTS):

    convex_hull = gift_wrapping(ax, canvas, root, POINTS)  # Run Giftwrapping algorithm

# Function to center the main window
def center_window(root):

    window_width = int(root.winfo_screenwidth() * 0.4)
    window_height = int(root.winfo_screenheight() * 0.5)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# Function to handle file selection and reading
def open_file():

    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if file_path:

        with open(file_path, 'r') as file:

            lines = file.readlines()

            if len(lines) >= 2:

                try:
                    # Read the number of points from the first line
                    num_points = int(lines[0])
                    # Parse the following lines with x,y coordinates
                    for line in lines[1:]:
                        x, y = map(float, line.strip().split(','))
                        POINTS.append((x, y))
                except ValueError:

                    num_points_label.config(text="Invalid file format")
            else:

                num_points_label.config(text="Invalid file format")

        display_point_count()
        update_plot()

#####################################################################################################################
#####################################################################################################################

# User Interface

# Create the main Tkinter window
root = tk.Tk()
root.title("Convex Hull Visualization")

center_window(root)  # Center the main window

upper_frame = tk.Frame(root)
upper_frame.pack(fill = "both", expand = True) 


#########################################################################################

# Create GUI elements
point_label = ttk.Label(upper_frame, text="Enter Points (x.0, y.0):")
point_label.grid(row=0, column=0, padx=(20, 60), pady = 5, sticky="NSEW")

point_entry = ttk.Entry(upper_frame)
point_entry.grid(row=1, column=0, padx=(20, 60), pady = 5, sticky="NSEW")
point_entry.bind("<Return>", add_point_on_enter)  # Bind the Enter key to add_point

ttk.Button(upper_frame, text="Add Point", command=add_point).grid(row=2, column=0, padx=(20, 60), pady = 5, sticky="NSEW")
ttk.Button(upper_frame, text="Clear Points", command=clear_points).grid(row=3, column=0, padx=(20, 60), pady = 5, sticky="NSEW")  # Button to clear points

#########################################################################################

# Input field for specifying the number of random points
num_points_label = ttk.Label(upper_frame, text="Enter the number of random points:")
num_points_label.grid(row=0, column=1, padx=(60, 60), pady=5, sticky="NSEW")

num_points_entry = ttk.Entry(upper_frame)
num_points_entry.grid(row=1, column=1, padx=(60, 60), pady=5, sticky="NSEW")
num_points_entry.bind("<Return>", add_random_points_on_enter)  # Bind the Enter key to add_point

ttk.Button(upper_frame, text="Add Random Points", command=add_random_points).grid(row=2, column=1, padx=(60, 60), pady=5, sticky="NSEW")
ttk.Button(upper_frame, text="Clear Points", command=clear_points).grid(row=3, column=1, padx=(60, 60), pady=5, sticky="NSEW")  # Button to clear points

# Create a label to display the point count
point_count_label = ttk.Label(upper_frame, text="Number of Points: 0")
point_count_label.grid(row=4, column=1, sticky=tk.N+tk.S)

Grid.rowconfigure(upper_frame,4,weight=1)
Grid.columnconfigure(upper_frame,1,weight=1)


###########################################################################################

# GUI elements for adding random points
ttk.Button(upper_frame, text="Quickhull Algorithm", command=lambda:quickhull_run(fig, ax, canvas, upper_frame, POINTS)).grid(row=1, column=2, padx=(60, 60), pady=5, sticky="NSEW")
ttk.Button(upper_frame, text="Giftwrapping Algorithm", command=lambda:giftwrapping_run(ax, canvas, upper_frame, POINTS)).grid(row=2, column=2, padx=(60, 60), pady=5, sticky="NSEW")
ttk.Button(upper_frame, text="Clear Algorithm Run", command=update_plot).grid(row=3, column=2, padx=(60, 60), pady=5, sticky="NSEW")

##########################################################################################

# Create a button to trigger file upload
ttk.Button(upper_frame, text="Upload File", command=open_file).grid(row=1, column=3, padx=(60, 20), pady=5, sticky="NSEW")
ttk.Button(upper_frame, text="Quit Window", command=lambda:modules.close_window(root)).grid(row=2, column=3, padx=(60, 20), pady=5, sticky="NSEW")

##########################################################################################

# Configure row and column weights for the upper frame
Grid.rowconfigure(upper_frame,0,weight=1)
Grid.rowconfigure(upper_frame,1,weight=1)
Grid.rowconfigure(upper_frame,2,weight=1)
Grid.rowconfigure(upper_frame,3,weight=1)
Grid.rowconfigure(upper_frame,4,weight=1)

Grid.columnconfigure(upper_frame,0,weight=1)
Grid.columnconfigure(upper_frame,1,weight=1)
Grid.columnconfigure(upper_frame,2,weight=1)
Grid.columnconfigure(upper_frame,3,weight=1)

##########################################################################################

# Create a lower frame for the Matplotlib plot
lower_frame = tk.Frame(root)
lower_frame.pack(fill="both", expand=True)

# Create a Matplotlib plot in the Tkinter window
fig, ax = plt.subplots(figsize=(8, 8))

# Plot Figure
canvas = FigureCanvasTkAgg(fig, master=lower_frame)
canvas.draw()
canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

# Start the Tkinter main loop
root.mainloop()

