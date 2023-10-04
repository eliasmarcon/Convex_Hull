import numpy as np

# Function to check if we have a counter-clockwise turn
# This function checks if three points (p1, p2, p3) make a counter-clockwise turn.
def is_counter_clockwise(p1, p2, p3):
    """This function checks if three points (p1, p2, p3) make a counter-clockwise turn.

    Args:
        p1: point 1
        p2: point 2
        p3: point 3

    Returns:
        bool: True if the points make a counter-clockwise turn, False otherwise
    """

    # Calculate the cross product of vectors (p3-p1) and (p2-p1)
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0])

# Main function:
# This function calculates the convex hull of a set of points using the gift wrapping 
# algorithm.
def gift_wrapping_calculation(points):
    """This function calculates the convex hull of a set of points using the gift wrapping
      algorithm.

    Args:
        points: list of points
    """
    
    index = 0
    num_points = len(points)
    
    # Convert the list of points to a NumPy array for efficient manipulation
    points = np.array(points)
    
    # Initialize an array to store the convex hull points
    convex_hull_points = [None] * num_points
    
    # Find the starting point of the convex hull (point with the lowest x-coordinate)
    current_hull_point = points[np.argmin(points[:, 0])]
    i = 0
    
    while True:
    
        # Add the current hull point to the convex hull
        convex_hull_points[i] = current_hull_point
        
        # Initialize the next endpoint as the first point in the list
        next_endpoint = points[0]
        
        # Iterate through the points to find the next endpoint of the convex hull
        for j in range(1, num_points):
    
            # Check if the current point is the same as the current hull point or if it is not counter-clockwise
            if (next_endpoint[0] == current_hull_point[0] and next_endpoint[1] == current_hull_point[1]) or not is_counter_clockwise(points[j], convex_hull_points[i], next_endpoint):
    
                next_endpoint = points[j]
        
        # Move to the next position in the convex hull
        i += 1
        current_hull_point = next_endpoint
        
        # Create a current hull containing all non-empty points
        current_hull = np.array([convex_hull_points[k] for k in range(num_points) if convex_hull_points[k] is not None])
        
        index += 1
        
        # Check if we have completed the convex hull by returning to the starting point
        if next_endpoint[0] == convex_hull_points[0][0] and next_endpoint[1] == convex_hull_points[0][1]:
    
            break
    
    # Remove any trailing 'None' values from the convex hull array
    for i in range(num_points):
    
        if convex_hull_points[-1] is None:
    
            del convex_hull_points[-1]
    
    # Convert the convex hull points to a NumPy array
    convex_hull_points = np.array(convex_hull_points)
    
    # Return the computed convex hull points
    return convex_hull_points

# Wrapper function for gift wrapping algorithm
# This function wraps the calculation function and returns the computed convex hull points.
def gift_wrapping(points):
    """This function wraps the calculation function and returns the computed convex 
    hull points.

    Args:
        points: list of points
    """

    convex_hull_points = gift_wrapping_calculation(points)

    return convex_hull_points
