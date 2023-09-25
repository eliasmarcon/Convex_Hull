import pandas as pd
import time
import csv
import os
import sys

from giftwrapping_performance import *

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath("./additional_files/")))
sys.path.append(project_root)

from additional_files.modules import *


def main():

    num_points_array = generate_num_points_array()

    if len(sys.argv) > 1:
        
        num_points = int(sys.argv[1])

    else:

        num_points = random.choice(num_points_array)


    filepath = check_existense("Giftwrapping")
    run_number = get_last_number(filepath)

    # Create and open a CSV file for logging
    with open(filepath, 'a', newline='') as csvfile:

        fieldnames = ["Test_Case", "Number_of_Points", "Execution Time", "Execution Time on CPU"]
        
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        points = generate_points(num_points)

        start_time = time.time()
        process_start_time = time.process_time()

        gift_wrapping(points)

        process_end_time = time.process_time()
        end_time = time.time()  # Record the end time
        
        process_execution_time = process_end_time - process_start_time
        execution_time = end_time - start_time  # Calculate the execution time

        # Write the execution time to the CSV file
        writer.writerow({'Test_Case' : run_number, 'Number_of_Points': num_points, 
                         'Execution Time': f":{execution_time:.4f}",
                         'Execution Time on CPU' : f":{process_execution_time:.4f}"})
    
    # Manually close the CSV file
    csvfile.close()
        
    print(f"Test Run {run_number} with {num_points} random points is finished")


if __name__ == "__main__":
    
    main()