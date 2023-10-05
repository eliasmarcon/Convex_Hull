
def find_distance(p1, p2, p3):
    """
    Calculates the distance between a line defined by two points (p1 and p2) and a third point (p3).
    
    Args:
    p1 (tuple): A tuple representing the (x, y) coordinates of the first point.
    p2 (tuple): A tuple representing the (x, y) coordinates of the second point.
    p3 (tuple): A tuple representing the (x, y) coordinates of the third point.
    
    Returns:
    float: The distance between the line defined by p1 and p2 and the point p3.
    """
    
    # Calculate coefficients for the line equation ax + by + c = 0
    a = p1[1] - p2[1]
    b = p2[0] - p1[0]
    c = p1[0] * p2[1] - p2[0] * p1[1]
    
    # Use the dot product formula to find the distance between the line and a point
    return abs(a * p3[0] + b * p3[1] + c) / (a * a + b * b)


# Function to create segments above and below a line defined by two points
def create_segment(p1, p2, v):
    """
    Given two points p1 and p2 and a set of points v, this function creates a segment between p1 and p2 and returns two lists:
    above - containing all the points in v that are above the line formed by p1 and p2
    below - containing all the points in v that are below the line formed by p1 and p2

    Args:
        p1 (tuple): A tuple representing the (x, y) coordinates of the first point of the line.
        p2 (tuple): A tuple representing the (x, y) coordinates of the second point of the line.
        v (list): A list of tuples representing the (x, y) coordinates of the points.

    Returns:
        above (list): A list of tuples representing the (x, y) coordinates of the points above the line.
        below (list): A list of tuples representing the (x, y) coordinates of the points below the line.
    """
    
    above = []
    below = []

    if p2[0] - p1[0] == 0:
    
        return above, below
    
    # Calculate the slope (m) and y-intercept (c) for the line equation y = mx + c
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = -m * p1[0] + p1[1]

    # Loop through each coordinate and place it into the correct list (above or below the line)
    for coordinate in v:
    
        # y > mx + c means it is above the line
        if coordinate[1] > m * coordinate[0] + c:
    
            above.append(coordinate)
    
        # y < mx + c means it is below the line
        elif coordinate[1] < m * coordinate[0] + c:
    
            below.append(coordinate)

    return above, below


