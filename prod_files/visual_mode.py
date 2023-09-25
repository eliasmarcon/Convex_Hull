import tkinter as tk
import matplotlib.pyplot as plt

from quickhull_folder.quickhull import *
from giftwrapping_folder.giftwrapping import *
from additional_files import modules

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, filedialog

## Create a list to store the convex hull points
CONVEX_HULL_POINTS = []
POINTS = [] # Initialize an empty list to store points


def add_point():

    point_str = point_entry.get()
    
    try:
        
        x, y = map(float, point_str.split(","))
        POINTS.append((x, y))
        update_plot()
        display_point_count()
        point_entry.delete(0, tk.END)  # Clear the input field after adding a point

    except ValueError:
        pass  # Handle invalid input

def add_random_points():

    num_points_str = num_points_entry.get()
    num_points = int(num_points_str)
    
    global POINTS
    POINTS = modules.generate_points(num_points, POINTS)

    update_plot()
    display_point_count()

    return POINTS

def add_point_on_enter(event):

    add_point()

def add_random_points_on_enter(event):

    add_random_points()    


def clear_points():

    global POINTS
    
    POINTS = []
    update_plot()
    display_point_count()


def update_plot():

    ax.clear()

    if POINTS:
        
        x, y = zip(*POINTS)
        ax.scatter(x, y, c='b', marker='o', label='Points', s = 4)

    canvas.draw()

# Function that does nothing when the button is clicked
def do_nothing():
    pass

# Create a function to display the current number of points
def display_point_count():
    point_count_label.config(text=f"Number of Points: {len(POINTS)}")

# QUICKHULL ALGORITHM
def quickhull_run(fig, ax, canvas, root, POINTS):

    convex_hull = quickhull(fig, ax, canvas, root, POINTS)

    # print(convex_hull)

# GIFTWRAPPING ALGORITHM
def giftwrapping_run(ax, canvas, root, POINTS):

    convex_hull = gift_wrapping(ax, canvas, root, POINTS)

    # print(convex_hull)
    

def center_window(root):
    
    window_width = 1000 #int(root.winfo_screenwidth() * 0.3) 
    window_height = 1000 #int(root.winfo_screenwidth() * 0.3)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = ( screen_width / 2 ) - ( window_width / 2 )
    y = ( screen_height / 2 ) - ( window_height / 2 )

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
point_label.grid(row=0, column=0, padx=(10, 60), pady = 5)

point_entry = ttk.Entry(upper_frame)
point_entry.grid(row=1, column=0, padx=(10, 60), pady = 5)
point_entry.bind("<Return>", add_point_on_enter)  # Bind the Enter key to add_point

ttk.Button(upper_frame, text="Add Point", command=add_point).grid(row=2, column=0, padx=(10, 60), pady = 5)
ttk.Button(upper_frame, text="Clear Points", command=clear_points).grid(row=3, column=0, padx=(10, 60), pady = 5)  # Button to clear points

#########################################################################################

# Input field for specifying the number of random points
num_points_label = ttk.Label(upper_frame, text="Enter the number of random points:")
num_points_label.grid(row=0, column=1, padx=(60, 60), pady=5)

num_points_entry = ttk.Entry(upper_frame)
num_points_entry.grid(row=1, column=1, padx=(60, 60), pady=5)
num_points_entry.bind("<Return>", add_random_points_on_enter)  # Bind the Enter key to add_point

ttk.Button(upper_frame, text="Add Random Points", command=add_random_points).grid(row=2, column=1, padx=(60, 60), pady=5)
ttk.Button(upper_frame, text="Clear Points", command=clear_points).grid(row=3, column=1, padx=(60, 60), pady=5)  # Button to clear points

# Create a label to display the point count
point_count_label = ttk.Label(upper_frame, text="Number of Points: 0")
point_count_label.grid(row=4, column=0, padx=(60, 60), pady = 5, columnspan=2)

###########################################################################################

# Create a button to trigger file upload
ttk.Button(upper_frame, text="Quickhull Algorithm", command=lambda:quickhull_run(fig, ax, canvas, upper_frame, POINTS)).grid(row=1, column=2, padx=(60, 60), pady=5)
ttk.Button(upper_frame, text="Giftwrapping Algorithm", command=lambda:giftwrapping_run(ax, canvas, upper_frame, POINTS)).grid(row=2, column=2, padx=(60, 60), pady=5)
ttk.Button(upper_frame, text="Clear Algorithm Run", command=update_plot).grid(row=3, column=2, padx=(60, 60), pady=5)

##########################################################################################

ttk.Button(upper_frame, text="Upload File", command=open_file).grid(row=1, column=3, padx=(60, 10), pady=5)
ttk.Button(upper_frame, text="Quit Window", command=lambda:modules.close_window(root)).grid(row=2, column=3, padx=(60, 10), pady=5)

##########################################################################################

lower_frame = tk.Frame(root)
lower_frame.pack(fill = "both", expand = True) 

# Create a Matplotlib plot in the Tkinter window
fig, ax = plt.subplots(figsize=(8, 8))

# Plot Figure
canvas = FigureCanvasTkAgg(fig, master=lower_frame)
canvas.draw()
canvas.get_tk_widget().pack(side="left", fill="both", expand = True)


root.mainloop()



# # Create GUI elements
# single_point_label = tk.Label(upper_frame, text="Enter Points (x.0, y.0):")
# single_point_label.pack(fill=tk.BOTH, padx=10, pady=5, side=tk.LEFT)

# # Use pack to arrange widgets in separate rows
# num_points_label = tk.Label(upper_frame, text="Enter the number of random points:")
# num_points_label.pack(fill=tk.BOTH, padx=10, pady=5, side=tk.RIGHT)



# point_entry = tk.Entry(upper_frame)
# point_entry.bind("<Return>", add_point_on_enter)  # Bind the Enter key to add_point
# point_entry.pack(fill=tk.BOTH, padx=10, pady=5)

# num_points_entry = tk.Entry(upper_frame)
# num_points_entry.bind("<Return>", add_random_points_on_enter)  # Bind the Enter key to add_point
# num_points_entry.pack(fill=tk.BOTH, padx=10, pady=5, side=tk.RIGHT)


# # Input field for specifying the number of random points
# add_single_point_button = tk.Button(upper_frame, text="Add Point", command=add_point)
# add_single_point_button.pack(fill=tk.BOTH, padx=10, pady=5, side=tk.LEFT)

# add_random_point_button = tk.Button(upper_frame, text="Add Random Points", command=add_random_points)
# add_random_point_button.pack(fill=tk.BOTH, padx=10, pady=5, side=tk.LEFT)


# clear_points_button = tk.Button(upper_frame, text="Clear Points", command=clear_points)  # Button to clear points
# clear_points_button.pack(fill=tk.BOTH, padx=10, pady=5, side=tk.LEFT)




