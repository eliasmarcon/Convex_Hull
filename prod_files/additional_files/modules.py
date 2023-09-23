import random

def generate_points(num_points, x_range=(-500.0, 500.0), y_range=(-500.0, 500.0)):
    """
    Generate a list of random (x, y) coordinates.

    Args:
        num_points (int): The number of points to generate.
        x_range (tuple): The range of x coordinates (min_x, max_x).
        y_range (tuple): The range of y coordinates (min_y, max_y).

    Returns:
        list: A list of (x, y) coordinate tuples.
    """
    points = []
    
    for _ in range(num_points):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        points.append((x, y))
    
    return points