import time
import numpy as np
import additional_files.modules_giftwrapping as modules_giftwrapping

time_sleeping = 1.0

# Function to update the plot by highlighting current hull points
def update_plot(ax, canvas, current_hull):

    """Function to update the plot by highlighting current hull points

    Args:
        ax: point object
        canvas: canvas object / where the plot is drawn
        current_hull: current hull points

    Returns:
        ax: point object (scatter plot of current hull points)
        canvas: canvas object / where the plot is drawn
    """
    
    # Scatter plot of current hull points
    ax.scatter([x[0] for x in current_hull], [y[1] for y in current_hull], c='r', marker='o', label='Highlighted Points')
    
    # Plot dashed lines connecting current hull points
    ax.plot(current_hull[:, 0], current_hull[:, 1], 'k--', picker=5, linewidth=1)
    
    canvas.draw()  # Redraw the canvas
    time.sleep(time_sleeping)  # Introduce a 1-second delay
    
    return ax, canvas

# Function to add the last connection to the convex hull
def last_connection(ax, canvas, convex_hull_points):

    """Function to add the last connection to the convex hull

    Args:
        ax: point object (scatter plot of current hull points)
        canvas: canvas object / where the plot is drawn
        convex_hull_points: convex hull points

    Returns:
        ax: point object (scatter plot of current hull points)
        canvas: canvas object / where the plot is drawn
    """
    
    # Plot dashed line connecting the last and first points in the convex hull
    ax.plot([convex_hull_points[-1, 0], convex_hull_points[0, 0]], [convex_hull_points[-1, 1], convex_hull_points[0, 1]], 'k--', picker=5, linewidth=1)
    
    canvas.draw()
    time.sleep(time_sleeping)
    
    return ax, canvas

# Function to finalize and plot the convex hull
def final_hull(ax, canvas, convex_hull_points):
    """Function to finalize and plot the convex hull

    Args:
        ax: point object (scatter plot of current hull points)
        canvas: canvas object / where the plot is drawn
        convex_hull_points: convex hull points
    """
    
    # Plot the final convex hull in red
    ax.plot(convex_hull_points[:, 0], convex_hull_points[:, 1], 'r-', picker=5, linewidth=2)
    
    # Plot the connection between the last and first points
    ax.plot([convex_hull_points[-1, 0], convex_hull_points[0, 0]], [convex_hull_points[-1, 1], convex_hull_points[0, 1]], 'r-', picker=5, linewidth=2)
    
    # Scatter plot of final convex hull points
    ax.scatter([x[0] for x in convex_hull_points], [y[1] for y in convex_hull_points], c='r', marker='o', label='Highlighted Points')
    
    canvas.draw()


def draw_point_line(ax, canvas, current_hull_point, point):

    # Plot the connection between the last and first points
    new_line = ax.plot([current_hull_point[0], point[0]], [current_hull_point[1], point[1]], color = (255 / 255, 192 / 255, 128 / 255), linestyle = '--', picker=5, linewidth=1)

    canvas.draw()
    
    time.sleep(time_sleeping)
    
    return ax, canvas, new_line


def draw_next_endpoint(ax, canvas, next_endpoint):

    ax.scatter(next_endpoint[0], next_endpoint[1], c='green', marker='o', label='Points')  # Plot points

    canvas.draw()

    time.sleep(time_sleeping)
    
    return ax, canvas
    

# Main function to calculate the convex hull using the Gift Wrapping algorithm
def gift_wrapping_calculation(ax, canvas, root, points):
    """Main function to calculate the convex hull using the Gift Wrapping algorithm

    Args:
        ax: point object (scatter plot of current hull points)
        canvas: canvas object / where the plot is drawn
        root: root object (Tkinter) / main window
        points: list of points

    """
        
    points = np.array(points)
    
    current_hull_point = points[np.argmin(points[:, 0])]
    convex_hull_points = []
    
    while True:
    
        convex_hull_points.append(current_hull_point)
        next_endpoint = points[0]

        # Create a list to store the lines
        temporary_lines = []
   
        for current_point in points:

            ax, canvas, new_line = draw_point_line(ax, canvas, current_hull_point, current_point)
            root.update()  # Update the GUI

            temporary_lines.append(new_line[0])  # Add the new line to the list of lines
    
            if (next_endpoint[0] == current_hull_point[0] and next_endpoint[1] == current_hull_point[1]) or not modules_giftwrapping.is_counter_clockwise(current_point, current_hull_point, next_endpoint):
    
                next_endpoint = current_point

        current_hull_point = next_endpoint

        ax, canvas = update_plot(ax, canvas, np.array(convex_hull_points))
        ax, canvas = draw_next_endpoint(ax, canvas, next_endpoint)
        root.update()  # Update the GUI

        # Remove the temporary lines
        for temporary_line in temporary_lines:
    
            temporary_line.remove()

        if current_hull_point[0] == convex_hull_points[0][0] and current_hull_point[1] == convex_hull_points[0][1]:
        
            temporary_lines = []
            
            for current_point in points:

                ax, canvas, new_line = draw_point_line(ax, canvas, current_hull_point, current_point)
                root.update()  # Update the GUI
                temporary_lines.append(new_line[0])  # Add the new line to the list of lines

            # Remove the temporary lines
            for temporary_line in temporary_lines:
        
                temporary_line.remove()    

            break
    
        
    convex_hull_points = np.array(convex_hull_points)
    ax, canvas = last_connection(ax, canvas, convex_hull_points)
    
    root.update()  # Update the GUI
    time.sleep(time_sleeping)
    
    final_hull(ax, canvas, convex_hull_points)
    root.update()  # Update the GUI
    
    return convex_hull_points


# Function to initiate the Gift Wrapping algorithm
def gift_wrapping(ax, canvas, root, points, current_value):
    """Function to initiate the Gift Wrapping algorithm

    Args:
        ax: point object (scatter plot of current hull points)
        canvas: canvas object / where the plot is drawn
        root: root object (Tkinter) / main window
        points: list of points
        current_value: current value of the slider

    Returns:
        list: convex hull points
    """

    global time_sleeping
    time_sleeping = current_value
    
    convex_hull_points = gift_wrapping_calculation(ax, canvas, root, points)
    
    return convex_hull_points