import random
import os
import pandas as pd
import csv
import time
import sys
from tkinter import messagebox

# Add the project root to the Python path
# Determine the project root directory and add it to the sys.path
giftwrapping_root = os.path.dirname(os.path.dirname(os.path.abspath("./giftwrapping_folder/")))
sys.path.append(giftwrapping_root)

quickhull_root = os.path.dirname(os.path.dirname(os.path.abspath("./quickhull_folder/")))
sys.path.append(quickhull_root)

from giftwrapping_folder import giftwrapping_performance
from quickhull_folder import quickhull_performance


# Define constants for the range of x and y coordinates
RANGE_X = -500.0
RANGE_Y = 500.0

# Define a function to close the Tkinter window
def close_window(root):

    """
    Args:
        root: The Tkinter window to close.
    """
    root.destroy()

# Define a function to check if input is a digit
def check_input(input):

    """
    Checks if the input is a digit.
    Args:
        input: The input to check.
    """
    
    if not input.isdigit():
    
        messagebox.showerror("Error", "Incorrect input, the input has to be a number")

# Define a function to check if input for points is in the correct format
def check_input_point(input):
    """
    Checks if the input is in the correct format.
    Args:
        input: The input to check.
    """
    if "," not in input:
    
        messagebox.showerror("Error", "Incorrect input, the input has to contain a ',' to separate the x- and y-coordinate")
    
    elif input.count(",") > 1:
    
        messagebox.showerror("Error", "Incorrect input, the input has to contain max 1. ',' to separate the x- and y-coordinate")
    
    else:
    
        try:
    
            x, y = map(float, input.split(","))
    
        except ValueError:
    
            messagebox.showerror("Error", "Incorrect input, the input has to be a number for the x- and y-coordinate")



def generate_points(num_points, points_array=None, x_range=(-500.0, 500.0), y_range=(-500.0, 500.0)):
    """
    Generate a list of random points within the specified ranges.
    
    args:
        num_points: number of points to generate
        points_array: optional array of points to append to
        x_range: range of x coordinates
        y_range: range of y coordinates
    """
    
    # Check if a custom points_array is provided; if not, initialize an empty list
    if points_array is None:
    
        points = []
    
    else:
    
        points = points_array

    unique_points = set()  # Create an empty set to store unique points

    # Generate random points until the desired number of unique points is reached
    while len(unique_points) < num_points:
    
        # Generate random x and y coordinates within the specified ranges
        x = random.uniform(RANGE_X, RANGE_Y)
        y = random.uniform(RANGE_X, RANGE_Y)
        point = (x, y)

        # Check if the generated point is unique; if so, add it to the points list and the unique_points set
        if point not in unique_points:
    
            unique_points.add(point)
            points.append(point)

    return points

# Create an empty DataFrame
# Get the current working directory
def check_existense(algorithm_name):
    """
    Checks if the file exists.
    
    args:
        algorithm_name: name of the algorithm to check if the file exists
    """

    # Get the current working directory
    current_directory = os.getcwd()

    # Navigate to the parent directory (move one folder back)
    parent_directory = os.path.dirname(current_directory)

    # Create the file path by joining parent_directory, "test_csv_files," and a file name based on algorithm_name
    filepath = os.path.join(parent_directory, "test_csv_files", f"Testfile_{algorithm_name}.csv")

    # Check if the file exists
    if os.path.exists(filepath):
    
        print(f"The file exists; it will be updated.")
    
    else:
        # Create an empty DataFrame with specified column names
        df = pd.DataFrame(columns=["Test_Case", "Number_of_Points", "Execution Time"])
        # Save the DataFrame as a CSV file at the specified filepath
        df.to_csv(f"{filepath}", index=False)
        print(f"The file does not exist; it will be created and filled.")

    return filepath

def get_last_number(filepath):
    """
    Gets the last run number +1 of the file.

    args:
        filepath: path to the file
    """
    
    # Open and read the CSV file
    with open(filepath, 'r') as csvfile:
    
        reader = csv.DictReader(csvfile)
        
        # Initialize a list to store the run numbers
        run_numbers = []
        
        # Iterate through the rows and extract the run numbers
        for row in reader:
    
            run_number = int(row['Test_Case'])
            run_numbers.append(run_number)

    if len(run_numbers) == 0:
    
        last_run_number = 1
    
    else:
        # Calculate the last run number as one greater than the maximum in the list
        last_run_number = run_numbers[-1] + 1

    return last_run_number


# Function to check if the csvs are there or not
def check_csv_exist(filepath):
    """
    Checks if the CSV file exists.
    
    args:
        filepath: path to the CSV file
    """

    if os.path.isfile(filepath):

        file_size = os.path.getsize(filepath)
        
        df = pd.read_csv(filepath, sep = ",")

        if file_size > 0:
         
            df['Number_of_Points'] = df['Number_of_Points'].astype(int)
            df = df.sort_values(by='Number_of_Points', ascending=False)

        return df
    
    else:

        # strings = filepath.split("\\")
        # filename = strings[-1].split(".")[0]
        # messagebox.showerror("Error", f"Please create the File {filename}")

        # Create an empty DataFrame with specified column names
        df = pd.DataFrame(columns=["Test_Case", "Number_of_Points", "Execution Time"])
        # Save the DataFrame as a CSV file at the specified filepath
        df.to_csv(f"{filepath}", index=False)


def get_preset_points_array():
    """
    Returns an array of preset numbers of points to test.
    """

    num_points_array = [

                        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,  # Basic Testing and boundary cases
                        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,  # Basic Testing
                        100, 200, 300, 400, 500, 600, 700, 800, 900, 1_000, # Performance Testing
                        2_000, 2_500, 3_000, 3_500, 4_000, 4_500, 5_000, 5_500, 6_000, 6_500, 7_000, 7_500, 8_000, 8_500, 9_000, 9_500, 10_000, # Performance Testing
                        15_000, 20_000, 30_000, 40_000, 50_000, 60_000, 70_000, 80_000, 90_000, 100_000, # Performance Testing
                        200_000, 300_000, 400_000, 500_000, 600_000, 700_000, 800_000, 900_000, 1_000_000, # Performance Testing
                        1_500_000, 2_000_000, 3_000_000, 4_000_000, 5_000_000, 6_000_000, 7_000_000, 8_000_000, 9_000_000, 10_000_000, # Performance Testing
                        # 20_000_000, 30_000_000, 40_000_000, 50_000_000, 60_000_000, 70_000_000, 80_000_000, 90_000_000, 100_000_000, # Performance Testing
                        # 110_000_000, 120_000_000, 130_000_000, 140_000_000, 150_000_000, 160_000_000, 170_000_000, 180_000_000, 190_000_000, 200_000_000, # Performance Testing
                        # 210_000_000, 220_000_000, 230_000_000, 240_000_000, 250_000_000, 260_000_000, 270_000_000, 280_000_000, 290_000_000, 300_000_000, # Performance Testing
                        # 310_000_000, 320_000_000, 330_000_000, 340_000_000, 350_000_000, 360_000_000, 370_000_000, 380_000_000, 390_000_000, 400_000_000, # Performance Testing
                        # 410_000_000, 420_000_000, 430_000_000, 440_000_000, 450_000_000, 460_000_000, 470_000_000, 480_000_000, 490_000_000, 500_000_000, # Performance Testing
                        # 510_000_000, 520_000_000, 530_000_000, 540_000_000, 550_000_000, 560_000_000, 570_000_000, 580_000_000, 590_000_000, 600_000_000, # Performance Testing
                        # 610_000_000, 620_000_000, 630_000_000, 640_000_000, 650_000_000, 660_000_000, 670_000_000, 680_000_000, 690_000_000, 700_000_000, # Performance Testing
                        # 710_000_000, 720_000_000, 730_000_000, 740_000_000, 750_000_000, 760_000_000, 770_000_000, 780_000_000, 790_000_000, 800_000_000, # Performance Testing
                        # 810_000_000, 820_000_000, 830_000_000, 840_000_000, 850_000_000, 860_000_000, 870_000_000, 880_000_000, 890_000_000, 900_000_000, # Performance Testing
                        # 910_000_000, 920_000_000, 930_000_000, 940_000_000, 950_000_000, 960_000_000, 970_000_000, 980_000_000, 990_000_000, 1_000_000_000, # Performance Testing
                        # 2_000_000_000, 3_000_000_000, 4_000_000_000, 5_000_000_000, 6_000_000_000, 7_000_000_000, 8_000_000_000, 9_000_000_000, 10_000_000_000, # Performance Testing
                        # 11_000_000_000, 12_000_000_000, 13_000_000_000, 14_000_000_000, 15_000_000_000, 16_000_000_000, 17_000_000_000, 18_000_000_000, 19_000_000_000, 20_000_000_000, # Performance Testing
                        # 21_000_000_000, 22_000_000_000, 23_000_000_000, 24_000_000_000, 25_000_000_000,26_000_000_000, 27_000_000_000, 28_000_000_000, 29_000_000_000, 30_000_000_000, # Performance Testing
                        # 31_000_000_000, 32_000_000_000, 33_000_000_000, 34_000_000_000, 35_000_000_000, 36_000_000_000, 37_000_000_000, 38_000_000_000, 39_000_000_000, 40_000_000_000, # Performance Testing
                        # 41_000_000_000, 42_000_000_000, 43_000_000_000, 44_000_000_000, 45_000_000_000, 46_000_000_000, 47_000_000_000, 48_000_000_000, 49_000_000_000, 50_000_000_000, # Performance Testing
                        # 51_000_000_000, 52_000_000_000, 53_000_000_000, 54_000_000_000, 55_000_000_000, 56_000_000_000, 57_000_000_000, 58_000_000_000, 59_000_000_000, 60_000_000_000, # Performance Testing
                        # 61_000_000_000, 62_000_000_000, 63_000_000_000, 64_000_000_000, 65_000_000_000, 66_000_000_000, 67_000_000_000, 68_000_000_000, 69_000_000_000, 70_000_000_000, # Performance Testing
                        # 71_000_000_000, 72_000_000_000, 73_000_000_000, 74_000_000_000, 75_000_000_000, 76_000_000_000, 77_000_000_000, 78_000_000_000, 79_000_000_000, 80_000_000_000, # Performance Testing
                        # 81_000_000_000, 82_000_000_000, 83_000_000_000, 84_000_000_000, 85_000_000_000, 86_000_000_000, 87_000_000_000, 88_000_000_000, 89_000_000_000, 90_000_000_000, # Performance Testing
                        # 91_000_000_000, 92_000_000_000, 93_000_000_000, 94_000_000_000, 95_000_000_000, 96_000_000_000, 97_000_000_000, 98_000_000_000, 99_000_000_000, 100_000_000_000 #  Performance Testing
                    ]
    
    return num_points_array


def open_csv_file(filepath, algorithm_name, num_points):
    """
    Opens the CSV file and writes the test results to it.
    
    args:
        filepath: path to the CSV file
        algorithm_name: name of the algorithm to check if the file exists
        num_points: number of points to generate
    """

    # Get the last run number from the existing CSV file
    run_number = get_last_number(filepath)

    # Create and open a CSV file for logging (appending mode) and specify newline handling
    with open(filepath, 'a', newline='') as csvfile:
    
        # Define the fieldnames for the CSV file
        fieldnames = ["Test_Case", "Number_of_Points", "Execution Time"]

        # Create a CSV DictWriter object with the specified fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Generate a list of random points based on the given num_points
        points = generate_points(num_points)

        # Record the start time of the execution
        start_time = time.time()

        # Check the algorithm_name to determine which algorithm to execute
        if algorithm_name == "Quickhull":
    
            # Execute the Quickhull algorithm on the generated points
            quickhull_performance.quickhull(points)
    
        elif algorithm_name == "Giftwrapping":
    
            # Execute the Giftwrapping algorithm on the generated points
            giftwrapping_performance.gift_wrapping(points)
    
        else:
    
            # If the algorithm_name is not recognized, exit the program
            exit()

        # Record the end time of the execution
        end_time = time.time()

        # Calculate the execution time by subtracting start_time from end_time
        execution_time = end_time - start_time

        # Write a row with execution results to the CSV file
        writer.writerow({'Test_Case': run_number, 'Number_of_Points': num_points,
                         'Execution Time': f"{execution_time:.4f}"})

    # Manually close the CSV file
    csvfile.close()

    # Return the run number for reference
    return run_number
