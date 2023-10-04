import sys
import os
import random
import modules

def write_points_to_file(points, file_name):
    '''
    Write a list of points to a text file.
    
    args:
        points: list of points to write to the file
        file_name: name of the file to write to
    '''

    # Get the current working directory
    current_directory = os.getcwd()

    # Navigate to the parent directory (move one folder back)
    parent_directory = os.path.dirname(current_directory)
    
    # Create the full file path by joining the parent directory, "test_text_files", and the specified file name
    filepath = os.path.join(parent_directory, "test_text_files", file_name)

    # Check if the file does not exist, and create the necessary directory structure if it doesn't
    if not os.path.exists(filepath):
    
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Open the file in write mode ('w')
    with open(filepath, 'w') as file:
    
        # Write the length of the points array as the first line in the file
        file.write(f"{len(points)}\n")

        # Write each point as x, y coordinates on separate lines
        for point in points:
    
            file.write(f"{point[0]}, {point[1]}\n")

def main():
    """
    Generate a list of random points and write them to a text file.    
    """

    # Check if command-line arguments were provided
    if len(sys.argv) > 1:
    
        # Get the number of points as a command-line argument
        num_points = int(sys.argv[1])
    
    else:
    
        # If no command-line argument is provided, randomly select a number of points from the preset array
        num_points = random.choice(modules.get_preset_points_array())

    # Generate a list of random points based on the specified number of points
    points = modules.generate_points(num_points)

    # Specify the output file name
    output_file = f"file_import_{num_points}.txt"

    # Write the generated points to the text file
    write_points_to_file(points, output_file)

    # Print a message confirming the number of points written to the file
    print(f"{num_points} points written to {output_file}")

if __name__ == "__main__":
    
    # Execute the main function when this script is run
    main()
    