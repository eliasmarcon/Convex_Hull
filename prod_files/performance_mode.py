import tkinter as tk
import random
import time
import pandas as pd

from quickhull_folder.quickhull_performance import *
from additional_files.modules import *

from tkinter.scrolledtext import ScrolledText  # Import ScrolledText for multi-line text display
from tkinter.font import Font
from tkinter import ttk, filedialog


points = [] # Initialize an empty list to store points
initial_time = 0.0000

# Variables to store the elapsed times of each algorithm
divide_and_conquer_time = initial_time
quickhull_time = initial_time

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

def add_random_points_on_enter(event):

    add_random_points()    


def clear_points():
    
    global points
    points = []
    display_point_count()

# Create a function to display the current number of points
def display_point_count():
    point_count_label.config(text=f"Number of Points: {len(points):,.0f}")


# Function to run two commands
def run_both_commands():

    # Call the first command
    quickhull_run()

    # Call the second command
    divide_and_conquer_run() # change to algo number 2


# Function to update the faster_algorithm_label
def update_faster_algorithm_label():
    
    global divide_and_conquer_time, quickhull_time
    
    print(divide_and_conquer_time, quickhull_time)

    if divide_and_conquer_time < quickhull_time:

        faster_algorithm_label.config(text=f"WINNER: Divide and Conquer Algorithm with {divide_and_conquer_time:.4f} seconds")

    elif divide_and_conquer_time == quickhull_time:

        faster_algorithm_label.config(text=f"Both Algorithms are equally fast with {divide_and_conquer_time:.4f} seconds")
    
    else:

        faster_algorithm_label.config(text=f"WINNER: Quickhall Algorithm with {quickhull_time:.4f} seconds")


# Function that does nothing when the button is clicked
def do_nothing():
    pass


def center_window(root):
    
    window_width = int(root.winfo_screenwidth() * 0.5) 
    window_height = int(root.winfo_screenwidth() * 0.5)

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
                        points.append((x, y))
                    
                except ValueError:
                    num_points_label.config(text="Invalid file format")
            else:
                num_points_label.config(text="Invalid file format")

            display_point_count()


##########################################################################################################################
# Divide and Conquer Methods
def divide_and_conquer_run():
    
    global divide_and_conquer_time

    # Record the start time
    start_time = time.time()

    points_sorted = sorted(points, key = lambda x : x[0])
    #divide and conquer algo

    end_time = time.time()

    # Calculate the elapsed time
    divide_and_conquer_time = end_time - start_time

    # Update the elapsed time label
    dac_elapsed_time_label.config(text=f"Elapsed Time Divide And Conquer Algorithm: {divide_and_conquer_time:.4f} seconds")
    
    # Determine the faster algorithm and update the label
    update_faster_algorithm_label()



##########################################################################################################################
# Quickhull
def quickhull_run():

    global quickhull_time

    start_time = time.time()

    quickhull(points)

    end_time = time.time()  # Record the end time
    
    quickhull_time = end_time - start_time  # Calculate the execution time

    # Update the elapsed time label
    elapsed_time_label.config(text=f"Elapsed Time Quickhull Algorithm: {quickhull_time:.4f} seconds")

    # Determine the faster algorithm and update the label
    update_faster_algorithm_label()

    

##########################################################################################################################

# User Interface

# Create the main Tkinter window for the performance optimized mode
root = tk.Tk()
root.title("Performance Optimized Mode")

center_window(root)  # Center the main window

# Create GUI elements

# Create a label to display the point count
point_count_label = ttk.Label(root, text="Number of Points: 0")
point_count_label.grid(row=0, column=0, columnspan=8, padx=10, pady=10)

# Input field for specifying the number of random points
num_points_label = ttk.Label(root, text="Enter the number of random points:")
num_points_label.grid(row=1, column=0, padx=5, pady=5, columnspan=4)

num_points_entry = ttk.Entry(root)
num_points_entry.grid(row=1, column=4, padx=5, pady=5, columnspan=4)
num_points_entry.bind("<Return>", add_random_points_on_enter)  # Bind the Enter key to add_random_points


ttk.Button(root, text="Clear Points", command=clear_points).grid(row=2, column=0, columnspan=3, padx=5, pady=(5, 20))  # Button to clear points

# Create a button to trigger file upload
upload_button = ttk.Button(root, text="Upload File", command=open_file)
upload_button.grid(row=2, column=3, columnspan=2, padx=5, pady=5)

add_random_button = ttk.Button(root, text="Add Random Points", command=add_random_points)
add_random_button.grid(row=2, column=6, padx=5, pady=(5, 20), columnspan=3)




ttk.Button(root, text="Quickhull Algorithm", command=quickhull_run).grid(row=3, column=0, padx=5, pady=5)
ttk.Button(root, text="Divide and Conquer Algorithm", command=divide_and_conquer_run).grid(row=3, column=3, padx=5, pady=5)
ttk.Button(root, text="Compare both Algorithms", command=run_both_commands).grid(row=3, column=6, padx=5, pady=5)


###################################################################################################################################
###################################################################################################################################
###################################################################################################################################

# Create a custom bold font
bold_font = Font(family="Helvetica", size=10, weight="bold")
font_standard = Font(family="Helvetica", size=10)

# Create a label to display the elapsed time
dac_elapsed_time_label = ttk.Label(root, text="Elapsed Time Divide and Conquer: 0.0000 seconds", font = font_standard)
dac_elapsed_time_label.grid(row=5, column=0, columnspan=8, padx=10, pady=10)

# Create a label to display the elapsed time
elapsed_time_label = ttk.Label(root, text="Elapsed Time Quickhull: 0.0000 seconds", font=font_standard)
elapsed_time_label.grid(row=6, column=0, columnspan=8, padx=10, pady=10)

# Create a label to display the faster algorithm
faster_algorithm_label = ttk.Label(root, text="Faster Algorithm in this Test Case: N/A", font=bold_font)
faster_algorithm_label.grid(row=7, column=0, columnspan=8, padx=10, pady=(10, 40))


###################################################################################################################################
############################################## Dataframes for Test Cases ##########################################################
###################################################################################################################################

# Create a label to display the faster algorithm
dataframes_general_label = ttk.Label(root, text="Dataframes of Test Cases for Quickhull and Divide and Conquer Algorithm", font=bold_font)
dataframes_general_label.grid(row=8, column=0, padx=10, columnspan=8, pady=(10, 20))

###################################################################################################################################

# Create a label to display the faster algorithm
quickhull_dataframe_label = ttk.Label(root, text="Quickhull Dataframe of Test Cases", font=font_standard)
quickhull_dataframe_label.grid(row=9, column=0, columnspan=8, padx=5, pady=5)

# Read the DataFrame from a CSV file
df = pd.read_csv(r'C:\Users\User\OneDrive - FH Technikum Wien\1_Semester\Advanced_Programming\Convex_Hull\prod_files\quickhull_folder\quickhull_performance_testing\Testfile_Quickhull.csv', sep = ",")
df = df.sort_values(by='Number_of_Points', ascending=False)

# Create a Treeview widget to display the DataFrame
tree = ttk.Treeview(root, columns=list(df.columns), show='headings')

# Add column headings
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)  # Adjust the width as needed

# Insert DataFrame rows into the Treeview
for i, row in df.iterrows():
    tree.insert('', 'end', values=row.tolist())

# Create a scrollbar
scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)

# Pack the Treeview and scrollbar into the window
tree.grid(row=10, column=0, columnspan=8, padx=10, pady=(10, 30))
scrollbar.grid(row=10, column=8, columnspan=8, padx=10, pady=(10, 30))

###################################################################################################################################

# Create a label to display the faster algorithm
divide_and_conquer_dataframe_label = ttk.Label(root, text="Divide and Conquer Dataframe of Test Cases", font=font_standard)
divide_and_conquer_dataframe_label.grid(row=11, column=0, columnspan=8, padx=5, pady=5)

# Read the DataFrame from a CSV file
df_divide_and_conquer = pd.read_csv(r'C:\Users\User\OneDrive - FH Technikum Wien\1_Semester\Advanced_Programming\Convex_Hull\prod_files\quickhull_folder\quickhull_performance_testing\Testfile_Quickhull.csv', sep = ",")
df_divide_and_conquer = df_divide_and_conquer.sort_values(by='Number_of_Points', ascending=False)

# Create a Treeview widget to display the DataFrame
tree = ttk.Treeview(root, columns=list(df_divide_and_conquer.columns), show='headings')

# Add column headings
for col in df_divide_and_conquer.columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)  # Adjust the width as needed

# Insert DataFrame rows into the Treeview
for i, row in df_divide_and_conquer.iterrows():
    tree.insert('', 'end', values=row.tolist())

# Create a scrollbar
scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)

# Pack the Treeview and scrollbar into the window
tree.grid(row=10, column=0, columnspan=8, padx=10, pady=(10, 30))
scrollbar.grid(row=10, column=8, columnspan=8, padx=10, pady=(10,30))
###################################################################################################################################

# Create a label to display the faster algorithm
generell_faster_label = ttk.Label(root, text="Overall faster Algorithm", font=font_standard)
generell_faster_label.grid(row=15, column=0, columnspan=8, padx=5, pady=5)

# Berechnungen


###################################################################################################################################
###################################################################################################################################
###################################################################################################################################


# Run the Tkinter main loop for the performance optimized mode
root.mainloop()
