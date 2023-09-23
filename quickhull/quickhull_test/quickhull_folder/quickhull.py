import time
import numpy as np
import math

from IPython.display import clear_output

##########################################################################################################################################
######################################################### Functions ######################################################################
##########################################################################################################################################


def time_sleep(integer):
    
    time.sleep(integer)
    
def initial_plot_updated(fig, ax, canvas, convex_hull):

    time_sleep(1)

    # draw Convex Hull points
    ax.scatter([x[0] for x in convex_hull], [y[1] for y in convex_hull], c = 'r', marker='o', label='Highlighted Points')

    # Draw a line between the highlighted points
    ax.plot([x[0] for x in convex_hull], [y[1] for y in convex_hull], 'k--', linewidth=1, label='Line between Highlighted Points')

    clear_output(wait=True)

    canvas.draw()
    
    return fig, ax, canvas


def update_plot_internally(fig, ax, p1, p2, farthest_point, canvas):

    time_sleep(1)

    # draw Convex Hull points
    ax.scatter(farthest_point[0], farthest_point[1], c = 'r', marker='o')

    # Draw a line between the highlighted points
    ax.plot([farthest_point[0], p1[0]], [farthest_point[1], p1[1]], 'k--', linewidth=1)
    ax.plot([farthest_point[0], p2[0]], [farthest_point[1], p2[1]], 'k--', linewidth=1)


    clear_output(wait=True)

    canvas.draw()

    return fig, ax, canvas


def final_plot(fig, ax, convex_hull, canvas):

    time_sleep(1)

    # Convert convex_hull to numpy array for easier manipulation
    convex_hull = np.array(convex_hull)
    
    if len(convex_hull) > 2:

        # Calculate polar coordinates (angle and radius) with respect to the center
        center = np.mean(convex_hull, axis=0)
        angles = np.arctan2(convex_hull[:, 1] - center[1], convex_hull[:, 0] - center[0])
        # radii = np.sqrt((convex_hull[:, 0] - center[0])**2 + (convex_hull[:, 1] - center[1])**2)

        # Sort convex_hull based on angles
        sorted_indices = np.argsort(angles)
        sorted_convex_hull = convex_hull[sorted_indices]

        # Create a plot and add the sorted convex_hull
        x_coords = sorted_convex_hull[:, 0]
        y_coords = sorted_convex_hull[:, 1]
        # ax.scatter(x_coords, y_coords, c='b', marker='o', label='Sorted convex_hull')

        # Connect the convex_hull to form the circular shape
        ax.plot(np.append(x_coords, x_coords[0]), np.append(y_coords, y_coords[0]), 'r-',  linewidth=2)


    else:
        
        # Extract x and y coordinates from the points array
        x = convex_hull[:, 0]
        y = convex_hull[:, 1]

        ax.plot(x, y, 'r-',  linewidth=2)
    
    clear_output(wait=True)

    canvas.draw()



def find_distance(p1, p2, p3):

    # using the formula ax + by + c = 0
    a = p1[1] - p2[1]
    b = p2[0] - p1[0]
    c = p1[0] * p2[1] - p2[0] * p1[1]

    # use dot product to find the distance between a line and a point
    return abs( a * p3[0] + b * p3[1] + c) / math.sqrt(a * a + b * b)



def create_segment(p1, p2, v):

    above = []
    below = []

    if p2[0] - p1[0] == 0:
        return above, below
    
    #calculate m and o from y = mx + o
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = -m * p1[0] + p1[1]

    #loop through each coordinate and place it into the correct list
    for coordinate in v:

        #y > mx + o means it is above the line
        if coordinate[1] > m * (coordinate[0]) + c:
            above.append(coordinate)
        #y < mx + o means it is below the line
        elif coordinate[1] < m * (coordinate[0]) + c:
            below.append(coordinate)


    return above, below



def upper_lower_hull(fig, ax, p1, p2, segment, flag, canvas, root):

    if segment == [] or p1 is None or p2 is None:
        return []

    convex_hull = []

    # calculate the distance of every point from the line to find the farthest point
    farthest_distance = -1
    farthest_point = None

    for point in segment:

        distance = find_distance(p1, p2, point)

        if distance > farthest_distance:
            
            farthest_distance = distance
            farthest_point = point


    #update Plot 
    if farthest_point:
        
        convex_hull = convex_hull + [farthest_point]

        fig, ax, canvas = update_plot_internally(fig, ax, p1, p2, farthest_point, canvas)
        root.update()  # Update the GUI



    # point is now in the convex hull so remove it from the segment
    segment.remove(farthest_point)

    # determine the segments formed from two lines p1-farthest_point and p2-farthest_point
    point1above, point1below = create_segment(p1, farthest_point, segment)
    point2above, point2below = create_segment(p2, farthest_point, segment)


    # only use the segmetns in the same direction, the opposite direction is contained in the convex hull
    if flag == "above":

        convex_hull = convex_hull + upper_lower_hull(fig, ax, p1, farthest_point, point1above, "above", canvas, root)
        convex_hull = convex_hull + upper_lower_hull(fig, ax, farthest_point, p2, point2above, "above", canvas, root)

    else:

        convex_hull = convex_hull + upper_lower_hull(fig, ax, p1, farthest_point, point1below, "below", canvas, root)
        convex_hull = convex_hull + upper_lower_hull(fig, ax, farthest_point, p2, point2below, "below", canvas, root)

    # print("Convex Hull in upper_lower_hull", convex_hull)

    return convex_hull


def quickhull(fig, ax, canvas, root, v):

    if len(v) <= 1:

        raise ValueError("Es braucht mindestens 2 Punkte um eine Convexe Huelle zu erstellen")  
    
    if len(v) > 2:
        
        convex_hull = []

        sort = sorted(v, key = lambda x : x[0])

        p1 = sort[0]
        p2 = sort[-1]

        convex_hull = convex_hull + [p1, p2]
        
        if len(v) == 2:

            fig, ax, canvas = initial_plot_updated(fig, ax, canvas, convex_hull)

            return fig, ax, v

        # remove from the list as they are now in the convex hull
        sort.pop(0)
        sort.pop(-1)

        fig, ax, canvas = initial_plot_updated(fig, ax, canvas, convex_hull)
        root.update()  # Update the GUI

        
        #determine points above and below the line
        above, below = create_segment(p1, p2, sort)
        
        convex_hull = convex_hull + upper_lower_hull(fig, ax, p1, p2, above, "above", canvas, root)
        
        convex_hull = convex_hull + upper_lower_hull(fig, ax, p1, p2, below, "below", canvas, root)

        final_plot(fig, ax, convex_hull, canvas)

        return convex_hull
    
    else:

        final_plot(fig, ax, v, canvas)

        return v
