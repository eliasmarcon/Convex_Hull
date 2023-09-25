import os
import sys
import random

from quickhull_performance import *

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath("./additional_files/")))
sys.path.append(project_root)

from additional_files import modules


def main():

    num_points_array = modules.get_preset_points_array()
    algorithm_name = "Quickhull"

    if len(sys.argv) > 1:
        
        num_points = int(sys.argv[1])

    else:

        num_points = random.choice(num_points_array)


    filepath = modules.check_existense(algorithm_name)
    
    run_number = modules.open_csv_file(filepath, algorithm_name, num_points)
      
        
    print(f"Test Run {run_number} with {num_points} random points is finished")


if __name__ == "__main__":
    
    main()
















