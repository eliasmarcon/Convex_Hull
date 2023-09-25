import numpy as np

# Function to check if we have a counter-clockwise turn
def is_counter_clockwise(p1, p2, p3):

    return (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0])

# Main function:
def gift_wrapping_calculation(points):

    index = 0
    num_points = len(points)
    points = np.array(points)
    convex_hull_points = [None] * num_points
    current_hull_point = points[np.argmin(points[:, 0])]
    i = 0
    
    while True:
        
        convex_hull_points[i] = current_hull_point
        next_endpoint = points[0]
        
        for j in range(1, num_points):
            if (next_endpoint[0] == current_hull_point[0] and next_endpoint[1] == current_hull_point[1]) or not is_counter_clockwise(points[j], convex_hull_points[i], next_endpoint):
                next_endpoint = points[j]
        
        i += 1
        current_hull_point = next_endpoint
        current_hull = np.array([convex_hull_points[k] for k in range(num_points) if convex_hull_points[k] is not None])

        
        index += 1
        if next_endpoint[0] == convex_hull_points[0][0] and next_endpoint[1] == convex_hull_points[0][1]:
            break
    
    for i in range(num_points):
        if convex_hull_points[-1] is None:
            del convex_hull_points[-1]
    
    convex_hull_points = np.array(convex_hull_points)
    
    return convex_hull_points

    

def gift_wrapping(points):
    
    convex_hull_points = gift_wrapping_calculation(points)

    # return convex_hull_points
