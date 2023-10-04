import tkinter as tk
from tkinter import ttk, Grid
import subprocess  # Used to run external scripts

# Function to center the Tkinter window on the screen
def center_window(root):
    """Function to center the Tkinter window on the screen

    Args:
        root: root object (Tkinter main window)
    """
    
    window_width = 450  # Width of the window
    window_height = 175  # Height of the window

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)  # Calculate the X coordinate
    y = (screen_height / 2) - (window_height / 2)  # Calculate the Y coordinate

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')  # Set the window size and position


# Function to start a subprocess for the visual mode
def start_subprocess_visual_mode():
    """Function to start a subprocess for the visual mode
    """
    global subprocess1
    subprocess1 = subprocess.Popen(['python', 'visual_mode.py'])

# Function to start a subprocess for the performance optimized mode
def start_subprocess_performance_mode():
    """Function to start a subprocess for the performance optimized mode"""
    global subprocess2
    subprocess2 = subprocess.Popen(['python', 'performance_mode.py'])

# Function to restart the subprocess for the visual mode
def restart_subprocess_visual_mode():
    
    if 'subprocess1' in globals():
    
        subprocess1.terminate()
        subprocess1.wait()
    
    start_subprocess_visual_mode()

# Function to restart the subprocess for the performance optimized mode
def restart_subprocess_performance_mode():
    """Function to restart the subprocess for the performance optimized mode"""
    if 'subprocess2' in globals():
    
        subprocess2.terminate()
        subprocess2.wait()
    
    start_subprocess_performance_mode()

# Function to quit the application and terminate subprocesses if running
def quit_application():
    """Function to quit the application and terminate subprocesses if running"""
    if 'subprocess1' in globals():

        subprocess1.terminate()
        subprocess1.wait()
    
    if 'subprocess2' in globals():
    
        subprocess2.terminate()
        subprocess2.wait()
    
    root.quit()


# Create the main Tkinter window for the home screen
root = tk.Tk()
root.title("Convex Hull Algorithm Home")

center_window(root)  # Center the main window

# Create labels to describe the options
visual_mode_label = ttk.Label(root, text="Visual Mode:")
optimized_mode_label = ttk.Label(root, text="Performance Optimized Mode:")
quit_label = ttk.Label(root, text="Quit Application:")

# Create buttons to open the respective modes
visual_mode_button = ttk.Button(root, text="Open Visual Mode", command=start_subprocess_visual_mode)
optimized_mode_button = ttk.Button(root, text="Open Performance Optimized Mode", command=start_subprocess_performance_mode)
quit_button = tk.Button(root, text="Quit", command=quit_application)

# Grid layout for labels and buttons
visual_mode_label.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
visual_mode_button.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")
optimized_mode_label.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")
optimized_mode_button.grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")
quit_label.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")
quit_button.grid(row=2, column=1, padx=10, pady=10, sticky="NSEW")

Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)

Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)

# Run the Tkinter main loop for the home screen
root.mainloop()