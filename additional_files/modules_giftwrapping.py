# Function to check if we have a counter-clockwise turn
def is_counter_clockwise(p1, p2, p3):
    """This function checks if three points (p1, p2, p3) make a counter-clockwise turn.

    Args:
        p1: point 1
        p2: point 2
        p3: point 3

    Returns:
        bool: True if the points make a counter-clockwise turn, False otherwise
    """
    
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0])


