import random
import sys
import os

from modules import *

def write_points_to_file(points, file_name):
    """
    Write the length of the array and each point to a text file.

    Args:
        file_path (str): The path to the output text file.
        points (list): A list of (x, y) coordinate tuples.

    Returns:
        None
    """
    # Get the current working directory
    current_directory = os.getcwd()

    # Navigate to the parent directory (move one folder back)
    parent_directory = os.path.dirname(current_directory)
    filepath = os.path.join(parent_directory, "test_text_files", file_name)

    # Check if the file exists, and create it if it doesn't
    if not os.path.exists(filepath):

        os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w') as file:

        # Write the length of the array as the first line
        file.write(f"{len(points)}\n")

        # Write each point as x, y coordinates on separate lines
        for point in points:

            file.write(f"{point[0]}, {point[1]}\n")

def main():
        
    num_points = int(sys.argv[1])

    points = generate_points(num_points)
    # Specify the output file path
    output_file = f"file_import_{num_points}.txt"

    # Write the points to the text file
    write_points_to_file(points, output_file)

    print(f"{num_points} points written to {output_file}")


if __name__ == "__main__":
    
    main()