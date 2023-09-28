import time
import numpy as np

from IPython.display import clear_output

# Function to introduce a delay in seconds
def time_sleep(integer):

    time.sleep(integer)

# Function to check if we have a counter-clockwise turn
def is_counter_clockwise(p1, p2, p3):
    
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0])

# Function to update the plot by highlighting current hull points
def update_plot(ax, canvas, current_hull):
    
    # Scatter plot of current hull points
    ax.scatter([x[0] for x in current_hull], [y[1] for y in current_hull], c='r', marker='o', label='Highlighted Points')
    
    # Plot dashed lines connecting current hull points
    ax.plot(current_hull[:, 0], current_hull[:, 1], 'k--', picker=5, linewidth=1)
    
    clear_output(wait=True)  # Clear the current output
    
    canvas.draw()  # Redraw the canvas
    time_sleep(1)  # Introduce a 1-second delay
    
    return ax, canvas

# Function to add the last connection to the convex hull
def last_connection(ax, canvas, convex_hull_points):
    
    # Plot dashed line connecting the last and first points in the convex hull
    ax.plot([convex_hull_points[-1, 0], convex_hull_points[0, 0]], [convex_hull_points[-1, 1], convex_hull_points[0, 1]], 'k--', picker=5, linewidth=1)
    
    clear_output(wait=True)
    
    canvas.draw()
    time_sleep(1)
    
    return ax, canvas

# Function to finalize and plot the convex hull
def final_hull(ax, canvas, convex_hull_points):
    
    # Plot the final convex hull in red
    ax.plot(convex_hull_points[:, 0], convex_hull_points[:, 1], 'r-', picker=5, linewidth=2)
    
    # Plot the connection between the last and first points
    ax.plot([convex_hull_points[-1, 0], convex_hull_points[0, 0]], [convex_hull_points[-1, 1], convex_hull_points[0, 1]], 'r-', picker=5, linewidth=2)
    
    # Scatter plot of final convex hull points
    ax.scatter([x[0] for x in convex_hull_points], [y[1] for y in convex_hull_points], c='r', marker='o', label='Highlighted Points')
    
    clear_output(wait=True)
    
    canvas.draw()

# Main function to calculate the convex hull using the Gift Wrapping algorithm
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

# Function to initiate the Gift Wrapping algorithm
def gift_wrapping(ax, canvas, root, points):
    
    convex_hull_points = gift_wrapping_calculation(ax, canvas, root, points)
    
    return convex_hull_points
