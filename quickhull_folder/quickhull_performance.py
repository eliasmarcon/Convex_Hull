import additional_files.modules_quickhull as modules_quickhull

# Recursive function to compute the upper or lower hull
def upper_lower_hull(p1, p2, segment, flag):
    """
    This function calculates the upper or lower hull of a set of points using the Quickhull algorithm.
    Args:
        p1 (tuple): A tuple representing the (x, y) coordinates of the first point of the line.
        p2 (tuple): A tuple representing the (x, y) coordinates of the second point of the line.
        segment (list): A list of tuples representing the (x, y) coordinates of the points.
        flag (str): A string to indicate whether the upper or lower hull is being calculated.
    Returns:
        convex_hull (list): A list of tuples representing the (x, y) coordinates of the points in the convex hull.
    """
    
    if segment == [] or p1 is None or p2 is None:
    
        return []

    convex_hull = []

    # Calculate the distance of every point from the line to find the farthest point
    farthest_distance = -1
    farthest_point = None

    for point in segment:
    
        distance = modules_quickhull.find_distance(p1, p2, point)
    
        if distance > farthest_distance:
    
            farthest_distance = distance
            farthest_point = point
            
    convex_hull = convex_hull + [farthest_point]

    # Point is now in the convex hull, so remove it from the segment
    segment.remove(farthest_point)

    # Determine the segments formed from two lines: p1-farthest_point and p2-farthest_point
    point1above, point1below = modules_quickhull.create_segment(p1, farthest_point, segment)
    point2above, point2below = modules_quickhull.create_segment(p2, farthest_point, segment)

    # Only use the segments in the same direction; the opposite direction is contained in the convex hull
    if flag == "above":
    
        convex_hull = convex_hull + upper_lower_hull(p1, farthest_point, point1above, "above")
        convex_hull = convex_hull + upper_lower_hull(farthest_point, p2, point2above, "above")
    
    else:
    
        convex_hull = convex_hull + upper_lower_hull(p1, farthest_point, point1below, "below")
        convex_hull = convex_hull + upper_lower_hull(farthest_point, p2, point2below, "below")

    return convex_hull

# Main function to compute the convex hull using the Quickhull algorithm
def quickhull(points):
    """Main function to compute the convex hull using the Quickhull algorithm.

    Args:
        points (list): A list of tuples representing the (x, y) coordinates of the points.

    Returns:
        convex_hull (list): A list of tuples representing the (x, y) coordinates of the points in the convex hull.
    """
    
    if len(points) <= 2:
    
        return points
        
    convex_hull = []

    p1 = min(points, key=lambda point: point[0])
    p2 = max(points, key=lambda point: point[0])

    # Remove the leftmost and rightmost points from the array
    points.remove(p1)
    points.remove(p2)

    # # Sort the input points based on their x-coordinates
    # sort = sorted(points, key=lambda x: x[0])

    # p1 = sort[0]
    # p2 = sort[-1]

    # convex_hull = convex_hull + [p1, p2]

    # # Remove the first and last points from the list as they are now in the convex hull
    # sort.pop(0)
    # sort.pop(-1)

    # Determine points above and below the line formed by p1 and p2
    above, below = modules_quickhull.create_segment(p1, p2, points)
    
    # Recursively compute the upper and lower hulls
    convex_hull = convex_hull + upper_lower_hull(p1, p2, above, "above")
    convex_hull = convex_hull + upper_lower_hull(p1, p2, below, "below")

    # Return the computed convex hull points
    return convex_hull
