import tkinter as tk
from tkinter import ttk
import subprocess  # Used to run external scripts

def center_window(root):
    
    window_width = int(root.winfo_screenwidth() * 0.3) #450
    window_height = int(root.winfo_screenwidth() * 0.1) #175

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = ( screen_width / 2 ) - ( window_width / 2 )
    y = ( screen_height / 2 ) - ( window_height / 2 )

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')


def start_subprocess_visual_mode():
    global subprocess1
    subprocess1 = subprocess.Popen(['python', 'visual_mode.py'])

def start_subprocess_performance_mode():
    global subprocess2
    subprocess2 = subprocess.Popen(['python', 'performance_mode.py'])

def restart_subprocess_visual_mode():
    if 'subprocess1' in globals():
        subprocess1.terminate()
        subprocess1.wait()
    start_subprocess_visual_mode()

def restart_subprocess_performance_mode():
    if 'subprocess2' in globals():
        subprocess2.terminate()
        subprocess2.wait()
    start_subprocess_performance_mode()

def quit_application():
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

# Install packages from requirements.txt
# subprocess.run(["pip", "install", "-r", "requirements.txt"])


# Create labels to describe the options
visual_mode_label = ttk.Label(root, text="Visual Mode:")
optimized_mode_label = ttk.Label(root, text="Performance Optimized Mode:")
quit_label = ttk.Label(root, text="Quit Application:")


# Create buttons to open the respective modes
visual_mode_button = ttk.Button(root, text="Open Visual Mode", command=start_subprocess_visual_mode)
optimized_mode_button = ttk.Button(root, text="Open Performance Optimized Mode", command=start_subprocess_performance_mode)
quit_button = tk.Button(root, text="Quit", command=quit_application)

# Grid layout for labels and buttons
visual_mode_label.grid(row=0, column=0, padx=10, pady=10)
visual_mode_button.grid(row=0, column=1, padx=10, pady=10)
optimized_mode_label.grid(row=1, column=0, padx=10, pady=10)
optimized_mode_button.grid(row=1, column=1, padx=10, pady=10)
quit_label.grid(row=2, column=0, padx=10, pady=10)
quit_button.grid(row=2, column=1, padx=10, pady=10)

# Run the Tkinter main loop for the home screen
root.mainloop()