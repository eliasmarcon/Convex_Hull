import tkinter as tk
import random
import time
import pandas as pd

from quickhull_folder.quickhull_performance import *
from giftwrapping_folder.giftwrapping_performance import *
from additional_files import modules

from tkinter.scrolledtext import ScrolledText  # Import ScrolledText for multi-line text display
from tkinter.font import Font
from tkinter import ttk, filedialog


points = [] # Initialize an empty list to store points
initial_time = 0.0000

# Variables to store the elapsed times of each algorithm
giftwrapping_time = initial_time
quickhull_time = initial_time

def add_random_points():

    num_points_str = num_points_entry.get()
    num_points = int(num_points_str)
    # try:
    #     if num_points < 1:
    #         return
    #     for _ in range(num_points):
    #         x = random.uniform(-500.0, 500.0)  # Adjust the range as needed
    #         y = random.uniform(-500.0, 500.0)  # Adjust the range as needed
    #         points.append((x, y))
    #         display_point_count()

    # except ValueError:
    #     pass

    global points
    points = modules.generate_points(num_points, points)
    display_point_count()

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
    giftwrapping_run() # change to algo number 2


# Function to update the faster_algorithm_label
def update_faster_algorithm_label():
    
    global giftwrapping_time, quickhull_time

    if giftwrapping_time < quickhull_time:

        faster_algorithm_label.config(text=f"WINNER: Giftwrapping Algorithm with {giftwrapping_time:.4f} seconds")

    elif giftwrapping_time == quickhull_time:

        faster_algorithm_label.config(text=f"Both Algorithms are equally fast with {giftwrapping_time:.4f} seconds")
    
    else:

        faster_algorithm_label.config(text=f"WINNER: Quickhall Algorithm with {quickhull_time:.4f} seconds")


# Function that does nothing when the button is clicked
def do_nothing():
    pass


def center_window(root):
    
    window_width = 1000 # int(root.winfo_screenwidth() * 0.5) 
    window_height = 1000 # int(root.winfo_screenwidth() * 0.5)

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
# Giftwrapping Methods
def giftwrapping_run():
    
    global giftwrapping_time

    # Record the start time
    start_time = time.time()

    #Giftwrapping algo
    gift_wrapping(points)

    end_time = time.time()

    # Calculate the elapsed time
    giftwrapping_time = end_time - start_time

    # Update the elapsed time label
    dac_elapsed_time_label.config(text=f"Elapsed Time Giftwrapping Algorithm: {giftwrapping_time:.4f} seconds")
    
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

upper_frame = tk.Frame(root)
upper_frame.pack(fill = "both", expand = True) 

# Create GUI elements


# Input field for specifying the number of random points
num_points_label = ttk.Label(upper_frame, text="Enter the number of random points:")
num_points_label.grid(row=0, column=0, padx=(40, 100), pady=10)

num_points_entry = ttk.Entry(upper_frame)
num_points_entry.grid(row=1, column=0, padx=(40, 100), pady=10)
num_points_entry.bind("<Return>", add_random_points_on_enter)  # Bind the Enter key to add_random_points

add_random_button = ttk.Button(upper_frame, text="Add Random Points", command=add_random_points)
add_random_button.grid(row=2, column=0, padx=(40, 100), pady=10)

###################################################################################################################################

ttk.Button(upper_frame, text="Clear Points", command=clear_points).grid(row=0, column=1, padx=(100, 100), pady=10)  # Button to clear points
# Create a button to trigger file upload
upload_button = ttk.Button(upper_frame, text="Upload File", command=open_file)
upload_button.grid(row=1, column=1, padx=(100, 100), pady=10)
ttk.Button(upper_frame, text="Compare both Algorithms", command=run_both_commands).grid(row=2, column=1, padx=(100, 100), pady=10)

###################################################################################################################################

ttk.Button(upper_frame, text="Quickhull Algorithm", command=quickhull_run).grid(row=0, column=2, padx=(100, 10), pady=10)
ttk.Button(upper_frame, text="Giftwrapping Algorithm", command=giftwrapping_run).grid(row=1, column=2, padx=(100, 10), pady=10)
tk.Button(upper_frame, text="Quit Window", command=lambda:modules.close_window(root)).grid(row=2, column=2, padx=(100, 10), pady=10)


# Create a label to display the point count
point_count_label = ttk.Label(upper_frame, text="Number of Points: 0")
point_count_label.grid(row=3, column=1, padx=(100, 100), pady=(10, 40))


###################################################################################################################################

# Create a custom bold font
bold_font = Font(family="Helvetica", size=10, weight="bold")
font_standard = Font(family="Helvetica", size=10)

# Create a label to display the elapsed time
dac_elapsed_time_label = ttk.Label(upper_frame, text="Elapsed Time Giftwrapping: 0.0000 seconds", font = font_standard)
dac_elapsed_time_label.grid(row=4, column=1, padx=10, pady=10)

# Create a label to display the elapsed time
elapsed_time_label = ttk.Label(upper_frame, text="Elapsed Time Quickhull: 0.0000 seconds", font=font_standard)
elapsed_time_label.grid(row=5, column=1, padx=10, pady=10)

# Create a label to display the faster algorithm
faster_algorithm_label = ttk.Label(upper_frame, text="Faster Algorithm in this Test Case: N/A", font=bold_font)
faster_algorithm_label.grid(row=6, column=1, padx=10, pady=(10, 40))


###################################################################################################################################
############################################## Dataframes for Test Cases ##########################################################
###################################################################################################################################

lower_frame = tk.Frame(root)
lower_frame.pack(fill = "both", expand = True) 

# Create a label to display the faster algorithm
dataframes_general_label = ttk.Label(lower_frame, text="Dataframes of Test Cases for Quickhull and Giftwrapping Algorithm", font=bold_font)
dataframes_general_label.grid(row=0, column=0, padx=(300, 300), pady=10)#.pack(fill="both", expand = True, anchor="e")

###################################################################################################################################

# Create a label to display the faster algorithm
quickhull_dataframe_label = ttk.Label(lower_frame, text="Quickhull Dataframe of Test Cases", font=font_standard)
quickhull_dataframe_label.grid(row=1, column=0, padx=(300, 300), pady=10)#.pack(side = tk.LEFT, fill="both", expand = True, anchor="e")

# Read the DataFrame from a CSV file
df_quickhull = pd.read_csv(r'C:\Users\User\OneDrive - FH Technikum Wien\1_Semester\Advanced_Programming\Convex_Hull\prod_files\test_csv_files\Testfile_Quickhull.csv', sep = ",")
df_quickhull['Number_of_Points'] = df_quickhull['Number_of_Points'].astype(int)
df_quickhull = df_quickhull.sort_values(by='Number_of_Points', ascending=False)

lower_frame_tree1 = tk.Frame(root)
lower_frame_tree1.pack(fill = "both", expand = True) 


# Create a Treeview widget to display the DataFrame
tree_quickhull = ttk.Treeview(lower_frame_tree1, columns=list(df_quickhull.columns), show='headings')

# Add column headings
for col in df_quickhull.columns:
    tree_quickhull.heading(col, text=col)
    tree_quickhull.column(col, width=150)  # Adjust the width as needed

# Insert DataFrame rows into the Treeview
for i, row in df_quickhull.iterrows():
    tree_quickhull.insert('', 'end', values=row.tolist())

# Create a scrollbar
scrollbar = ttk.Scrollbar(lower_frame_tree1, orient='vertical', command=tree_quickhull.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand = True)
tree_quickhull.configure(yscroll=scrollbar.set)
tree_quickhull.pack(side=tk.LEFT, fill=tk.Y, expand = True, pady=20, padx=10)

# Pack the Treeview and scrollbar into the window
# tree.grid(row=10, column=0, columnspan=8, padx=10, pady=(10, 30))
# scrollbar.grid(row=10, column=8, columnspan=8, padx=10, pady=(10, 30))

# ###################################################################################################################################
lower_frame2 = tk.Frame(root)
lower_frame2.pack(fill = "both", expand = True) 

# Create a label to display the faster algorithm
giftwrapping_dataframe_label = ttk.Label(lower_frame2, text="Giftwrapping Dataframe of Test Cases", font=font_standard)
giftwrapping_dataframe_label.grid(row=0, column=0, padx=(400, 400), pady=10)#.pack(fill="both", expand = True, anchor="center")

# Read the DataFrame from a CSV file
df_giftwrapping = pd.read_csv(r'C:\Users\User\OneDrive - FH Technikum Wien\1_Semester\Advanced_Programming\Convex_Hull\prod_files\test_csv_files\Testfile_Giftwrapping.csv', sep = ",")
df_giftwrapping['Number_of_Points'] = df_giftwrapping['Number_of_Points'].astype(int)
df_giftwrapping = df_giftwrapping.sort_values(by='Number_of_Points', ascending=False)


lower_frame2_tree2 = tk.Frame(root)
lower_frame2_tree2.pack(fill = "both", expand = True) 

# Create a Treeview widget to display the DataFrame
tree_giftwrapping = ttk.Treeview(lower_frame2_tree2, columns=list(df_giftwrapping.columns), show='headings')

# Add column headings
for col in df_giftwrapping.columns:
    tree_giftwrapping.heading(col, text=col)
    tree_giftwrapping.column(col, width=150)  # Adjust the width as needed

# Insert DataFrame rows into the Treeview
for i, row in df_giftwrapping.iterrows():
    tree_giftwrapping.insert('', 'end', values=row.tolist())

# Create a scrollbar
scrollbar = ttk.Scrollbar(lower_frame2_tree2, orient='vertical', command=tree_giftwrapping.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand = True)
tree_giftwrapping.configure(yscroll=scrollbar.set)
tree_giftwrapping.pack(side=tk.LEFT, fill=tk.Y, expand = True, pady=20, padx=10)

# # Pack the Treeview and scrollbar into the window
# tree.grid(row=11, column=0, columnspan=8, padx=10, pady=(10, 30))
# scrollbar.grid(row=11, column=8, columnspan=8, padx=10, pady=(10,30))
###################################################################################################################################
# lower_frame3 = tk.Frame(root)
# lower_frame3.pack(fill = "both", expand = True) 


# # Create a label to display the faster algorithm
# generell_faster_label = ttk.Label(lower_frame3, text="Overall faster Algorithm", font=font_standard)
# generell_faster_label.grid(row=0, column=0, padx=(400, 400), pady=10)

# # Berechnungen


###################################################################################################################################
###################################################################################################################################
###################################################################################################################################


# Run the Tkinter main loop for the performance optimized mode
root.mainloop()
