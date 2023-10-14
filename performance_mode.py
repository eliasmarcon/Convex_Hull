import tkinter as tk
import time

from quickhull_folder.quickhull_performance import *
from giftwrapping_folder.giftwrapping_performance import *
from additional_files import modules

from tkinter.font import Font
from tkinter import ttk, filedialog, Grid


# Initialize an empty list to store points
points = []

# Initialize variables for elapsed times
initial_time = 0.0000
giftwrapping_time = initial_time
quickhull_time = initial_time

# Function to add random points
def add_random_points():
    """Function to add random points"""
    num_points_str = num_points_entry.get()
    modules.check_input(num_points_str)  # Validate input
    num_points = int(num_points_str)
    
    global points
    
    points = modules.generate_points(num_points, points)  # Generate random points
    display_point_count()  # Update point count

# Function to add random points on pressing Enter
def add_random_points_on_enter(event):
    """Function to add random points on pressing Enter"""
    add_random_points()

# Function to clear all points
def clear_points():
    """Function to clear all points"""
    global points
    points = []  # Clear the list of points
    display_point_count()  # Reset the point count label

# Function to display the current number of points
def display_point_count():
    """Function to display the current number of points"""
    point_count_label.config(text=f"Number of Points: {len(points):,.0f}")

# Function to run both algorithms
def run_both_commands():
    """Function to run both algorithms"""
    quickhull_run()  # Call the Quickhull algorithm
    giftwrapping_run()  # Call the Giftwrapping algorithm

# Function to update the label showing the faster algorithm
def update_faster_algorithm_label():
    """Function to update the label showing the faster algorithm"""
    global giftwrapping_time, quickhull_time
    
    if giftwrapping_time < quickhull_time:
    
        faster_algorithm_label.config(text=f"WINNER: Giftwrapping Algorithm with {giftwrapping_time:.4f} seconds")
    
    elif giftwrapping_time == quickhull_time:
    
        faster_algorithm_label.config(text=f"BOTH Algorithms are equally fast with {giftwrapping_time:.4f} seconds")
    
    else:
    
        faster_algorithm_label.config(text=f"WINNER: Quickhull Algorithm with {quickhull_time:.4f} seconds")

# Function to center the main window
def center_window(root):
    """Function to center the main window
    
    Args:
        root: Tkinter root
    """
    window_width = 1000 #int(root.winfo_screenwidth() * 0.5) 
    window_height = 850 #int(root.winfo_screenheight() * 0.7)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = ( screen_width / 2 ) - ( window_width / 2 )
    y = ( screen_height / 2 ) - ( window_height / 2 )


    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')


# Function to handle file selection and reading
def open_file():
    """Function to handle file selection and reading"""
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if file_path:

        with open(file_path, 'r') as file:
            
            lines = file.readlines()
            
            if len(lines) >= 2:

                try:
                    
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
# Giftwrapping Algorithm
def giftwrapping_run():
    """Function to run the Giftwrapping algorithm"""
    
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

    modules.update_csv_file("Giftwrapping", len(points) + 2, giftwrapping_time)
    
    # Determine the faster algorithm and update the label
    update_faster_algorithm_label()



##########################################################################################################################
# Quickhull
def quickhull_run():
    """Function to run the Quickhull algorithm"""
    global quickhull_time

    start_time = time.time()

    quickhull(points)

    end_time = time.time()  # Record the end time
    
    quickhull_time = end_time - start_time  # Calculate the execution time

    # Update the elapsed time label
    elapsed_time_label.config(text=f"Elapsed Time Quickhull Algorithm: {quickhull_time:.4f} seconds")

    modules.update_csv_file("Quickhull", len(points) + 2, quickhull_time)

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

###################################################################################################################################

# Input field for specifying the number of random points
num_points_label = ttk.Label(upper_frame, text="Enter the number of random points:")
num_points_label.grid(row=0, column=0, padx=(40, 100), pady=10, sticky="NSEW")

num_points_entry = ttk.Entry(upper_frame)
num_points_entry.grid(row=1, column=0, padx=(40, 100), pady=10, sticky="NSEW")
num_points_entry.bind("<Return>", add_random_points_on_enter)  # Bind the Enter key to add_random_points

add_random_button = ttk.Button(upper_frame, text="Add Random Points", command=add_random_points)
add_random_button.grid(row=2, column=0, padx=(40, 100), pady=10, sticky="NSEW")

###################################################################################################################################

ttk.Button(upper_frame, text="Clear Points", command=clear_points).grid(row=0, column=1, padx=(100, 100), pady=10, sticky="NSEW")  # Button to clear points
# Create a button to trigger file upload
upload_button = ttk.Button(upper_frame, text="Upload File", command=open_file)
upload_button.grid(row=1, column=1, padx=(100, 100), pady=10, sticky="NSEW")
ttk.Button(upper_frame, text="Compare both Algorithms", command=run_both_commands).grid(row=2, column=1, padx=(100, 100), pady=10, sticky="NSEW") #command=lambda : (run_both_commands(), update_treeview_quickhull(), update_treeview_giftwrapping())

###################################################################################################################################

ttk.Button(upper_frame, text="Quickhull Algorithm", command=quickhull_run).grid(row=0, column=2, padx=(100, 10), pady=10, sticky="NSEW")
ttk.Button(upper_frame, text="Giftwrapping Algorithm", command=giftwrapping_run).grid(row=1, column=2, padx=(100, 10), pady=10, sticky="NSEW")
tk.Button(upper_frame, text="Quit Window", command=lambda:modules.close_window(root)).grid(row=2, column=2, padx=(100, 10), pady=10, sticky="NSEW")


# Create a label to display the point count
point_count_label = ttk.Label(upper_frame, text="Number of Points: 0")
point_count_label.grid(row=3, column=1, padx=(100, 100), pady=(10, 20), sticky=tk.N+tk.S)


###################################################################################################################################

# Create a custom bold font
bold_font = Font(family="Helvetica", size=12, weight="bold")
font_standard = Font(family="Helvetica", size=12)

# Create a label to display the elapsed time
dac_elapsed_time_label = ttk.Label(upper_frame, text="Elapsed Time Giftwrapping: 0.0000 seconds", font = font_standard)
dac_elapsed_time_label.grid(row=4, column=1, pady = 10, sticky=tk.N+tk.S)

# Create a label to display the elapsed time
elapsed_time_label = ttk.Label(upper_frame, text="Elapsed Time Quickhull: 0.0000 seconds", font=font_standard)
elapsed_time_label.grid(row=5, column=1, pady = 10, sticky=tk.N+tk.S)

# Create a label to display the faster algorithm
faster_algorithm_label = ttk.Label(upper_frame, text="Faster Algorithm in this Test Case: N/A", font=bold_font)
faster_algorithm_label.grid(row=6, column=1, pady = (10, 20), sticky=tk.N+tk.S)

###################################################################################################################################

# Row and Column configuration to position the elements better
Grid.rowconfigure(upper_frame,0,weight=1)
Grid.rowconfigure(upper_frame,1,weight=1)
Grid.rowconfigure(upper_frame,2,weight=1)
Grid.rowconfigure(upper_frame,3,weight=1)
Grid.rowconfigure(upper_frame,4,weight=1)
Grid.rowconfigure(upper_frame,5,weight=1)
Grid.rowconfigure(upper_frame,6,weight=1)

Grid.columnconfigure(upper_frame,0,weight=1)
Grid.columnconfigure(upper_frame,1,weight=1)
Grid.columnconfigure(upper_frame,2,weight=1)



###################################################################################################################################
############################################## Dataframes for Test Cases ##########################################################
###################################################################################################################################

lower_frame = tk.Frame(root)
lower_frame.pack(fill = "both", expand = True) 

# Create a label to display the faster algorithm
dataframes_general_label = ttk.Label(lower_frame, text="Dataframes of Test Cases for Quickhull and Giftwrapping Algorithm", font=bold_font)
dataframes_general_label.grid(row=0, column=0, sticky=tk.N+tk.S)#.pack(fill="both", expand = True, anchor="e")

###################################################################################################################################

# Create a label to display the faster algorithm
quickhull_dataframe_label = ttk.Label(lower_frame, text="Quickhull Dataframe of Test Cases", font=font_standard)
quickhull_dataframe_label.grid(row=1, column=0, sticky=tk.N+tk.S)#.pack(side = tk.LEFT, fill="both", expand = True, anchor="e")

###################################################################################################################################

Grid.rowconfigure(lower_frame,0,weight=1)
Grid.rowconfigure(lower_frame,1,weight=1)
Grid.columnconfigure(lower_frame,0,weight=1)

###################################################################################################################################

# Read the DataFrame from a CSV file

filepath_quickhull = r'test_csv_files\Testfile_Quickhull.csv'
df_quickhull = modules.check_csv_exist(filepath_quickhull)

lower_frame_tree1 = tk.Frame(root)
lower_frame_tree1.pack(fill = "both", expand = True) 

# Create a Treeview widget to display the DataFrame
tree_quickhull = ttk.Treeview(lower_frame_tree1, columns=list(df_quickhull.columns), show='headings')

# Add column headings
for col in df_quickhull.columns:
    
    if "Execution Time" in col:

        col_text = "Execution Time in Seconds"
        tree_quickhull.heading(col, text=col_text)

    else:

        tree_quickhull.heading(col, text=col)

    tree_quickhull.column(col)

# Insert DataFrame rows into the Treeview
for i, row in df_quickhull.iterrows():
    numeric_columns = ['Test_Case', 'Number_of_Points']
    formatted_row = [int(value) if col in numeric_columns else value for col, value in row.items()]
    tree_quickhull.insert('', 'end', values=formatted_row)

# def update_treeview_quickhull():

#     filepath_quickhull = r'test_csv_files\Testfile_Quickhull.csv'
#     df_quickhull = modules.check_csv_exist(filepath_quickhull)

#     lower_frame_tree1 = tk.Frame(root)
#     lower_frame_tree1.pack(fill = "both", expand = True) 

#     # Create a Treeview widget to display the DataFrame
#     tree_quickhull = ttk.Treeview(lower_frame_tree1, columns=list(df_quickhull.columns), show='headings')

#     # Add column headings
#     for col in df_quickhull.columns:
        
#         if "Execution Time" in col:

#             col_text = "Execution Time in Seconds"
#             tree_quickhull.heading(col, text=col_text)

#         else:

#             tree_quickhull.heading(col, text=col)

#         tree_quickhull.column(col)

#     # Insert DataFrame rows into the Treeview
#     for i, row in df_quickhull.iterrows():
#         numeric_columns = ['Test_Case', 'Number_of_Points']
#         formatted_row = [int(value) if col in numeric_columns else value for col, value in row.items()]
#         tree_quickhull.insert('', 'end', values=formatted_row)


# Create a scrollbar
scrollbar = ttk.Scrollbar(lower_frame_tree1, orient='vertical', command=tree_quickhull.yview)
scrollbar.pack(side="right", fill="y")
tree_quickhull.configure(yscroll=scrollbar.set)
tree_quickhull.pack(side="left", expand=True, fill="both", pady=20, padx=10)

# ###################################################################################################################################
lower_frame2 = tk.Frame(root)
lower_frame2.pack(fill = "both", expand = True) 

# Create a label to display the faster algorithm
giftwrapping_dataframe_label = ttk.Label(lower_frame2, text="Giftwrapping Dataframe of Test Cases", font=font_standard)
giftwrapping_dataframe_label.grid(row=0, column=0, sticky=tk.N+tk.S)

# Read the DataFrame from a CSV file
filepath_giftwrapping = r'test_csv_files\Testfile_Giftwrapping.csv'
df_giftwrapping = modules.check_csv_exist(filepath_giftwrapping)

###################################################################################################################################

Grid.rowconfigure(lower_frame2,0,weight=1)
Grid.columnconfigure(lower_frame2,0,weight=1)

###################################################################################################################################

lower_frame2_tree2 = tk.Frame(root)
lower_frame2_tree2.pack(fill = "both", expand = True) 

# Create a Treeview widget to display the DataFrame
tree_giftwrapping = ttk.Treeview(lower_frame2_tree2, columns=list(df_giftwrapping.columns), show='headings')

# Add column headings
for col in df_giftwrapping.columns:

    if "Execution Time" in col:
        
        col_text = "Execution Time in Seconds"
        tree_giftwrapping.heading(col, text=col_text)

    else:

        tree_giftwrapping.heading(col, text=col)

    tree_giftwrapping.column(col)

# Insert DataFrame rows into the Treeview
for i, row in df_giftwrapping.iterrows():
    numeric_columns = ['Test_Case', 'Number_of_Points']
    formatted_row = [int(value) if col in numeric_columns else value for col, value in row.items()]
    tree_giftwrapping.insert('', 'end', values=formatted_row)


# Create a scrollbar
scrollbar = ttk.Scrollbar(lower_frame2_tree2, orient='vertical', command=tree_giftwrapping.yview)
scrollbar.pack(side="right", fill="y")
tree_giftwrapping.configure(yscroll=scrollbar.set)
tree_giftwrapping.pack(side="left", expand=True, fill="both", pady=20, padx=10)


# Run the Tkinter main loop
root.mainloop()

