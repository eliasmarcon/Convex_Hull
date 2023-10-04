import sys
import random

# Import custom modules
import modules

# Define the main function
def main():

    # Get an array of preset numbers of points from a module function
    num_points_array = modules.get_preset_points_array()

    # Specify the algorithm name
    algorithm_name = sys.argv[1] # options [Giftwrapping, Quickhull]

    # Check if command-line arguments were provided
    if len(sys.argv) > 2:
    
        # Parse the number of points from the first command-line argument
        num_points = int(sys.argv[2])
    
    else:
    
        # If no command-line argument is provided, randomly select a number of points from the preset array
        num_points = random.choice(num_points_array)

    # Check for the existence of a CSV file and create it if it doesn't exist
    filepath = modules.check_existense(algorithm_name)

    # Open the CSV file for logging and get the run number
    run_number = modules.open_csv_file(filepath, algorithm_name, num_points)

    # Print a message indicating the completion of the test run
    print(f"Test Run {run_number} with {num_points} random points is finished")

# Check if the script is being run as the main program
if __name__ == "__main__":
    
    # Call the main function when the script is executed
    main()
    