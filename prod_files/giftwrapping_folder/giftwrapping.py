import time
import numpy as np

from IPython.display import clear_output

def time_sleep(integer):
    
    time.sleep(integer)

# Function to check if we have a counter-clockwise turn
def is_counter_clockwise(p1, p2, p3):
    
    # Calculate the determinant of the 2x2 matrix [a, b; c, d]
    # ab = a[0] * b[1]
    # bc = b[0] * c[1]
    # ca = c[0] * a[1]

    # ba = a[1] * b[0]
    # cb = b[1] * c[0]
    # ac = c[1] * a[0]

    # det = (ab + bc + ca) - (ba + cb + ac)

    return (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0])


def update_plot(ax, canvas, current_hull):

    ax.scatter([x[0] for x in current_hull], [y[1] for y in current_hull], c = 'r', marker='o', label='Highlighted Points')
    # ax.plot(current_hull[:, 0], current_hull[:, 1], "r")  # Plot points
    ax.plot(current_hull[:, 0], current_hull[:, 1], 'k--', picker=5, linewidth=1)  # Plot lines
    
    clear_output(wait=True)
    canvas.draw()

    time_sleep(1)

    return ax, canvas

def last_connection(ax, canvas, convex_hull_points):

    ax.plot([convex_hull_points[-1, 0], convex_hull_points[0, 0]], [convex_hull_points[-1, 1], convex_hull_points[0, 1]], 'k--', picker=5, linewidth=1)
    clear_output(wait=True)
    canvas.draw()

    time_sleep(1)

    return ax, canvas

def final_hull(ax, canvas, convex_hull_points):

    # Plot final hull
    ax.plot(convex_hull_points[:, 0], convex_hull_points[:, 1], 'r-', picker=5, linewidth=2)
    ax.plot([convex_hull_points[-1, 0], convex_hull_points[0, 0]], [convex_hull_points[-1, 1], convex_hull_points[0, 1]], 'r-', picker=5, linewidth=2)
    ax.scatter([x[0] for x in convex_hull_points], [y[1] for y in convex_hull_points], c = 'r', marker='o', label='Highlighted Points')
    # ax.plot(convex_hull_points[:, 0], convex_hull_points[:, 1], ".r")
    
    clear_output(wait=True)
    canvas.draw()


# Main function:
def gift_wrapping_calculation(ax, canvas, root, points):

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

        ax, canvas = update_plot(ax, canvas, current_hull)
        root.update()  # Update the GUI
        
        index += 1
        if next_endpoint[0] == convex_hull_points[0][0] and next_endpoint[1] == convex_hull_points[0][1]:
            break
    
    for i in range(num_points):
        if convex_hull_points[-1] is None:
            del convex_hull_points[-1]
    
    convex_hull_points = np.array(convex_hull_points)
    
    ax, canvas = last_connection(ax, canvas, convex_hull_points)
    root.update()  # Update the GUI

    time_sleep(1)

    final_hull(ax, canvas, convex_hull_points)
    root.update()  # Update the GUI

    return convex_hull_points

    

def gift_wrapping(ax, canvas, root, points):
    
    convex_hull_points = gift_wrapping_calculation(ax, canvas, root, points)

    return convex_hull_points
