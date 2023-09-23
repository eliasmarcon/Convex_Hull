import math

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



def upper_lower_hull(p1, p2, segment, flag):

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
            
    convex_hull = convex_hull + [farthest_point]

    # point is now in the convex hull so remove it from the segment
    segment.remove(farthest_point)

    # determine the segments formed from two lines p1-farthest_point and p2-farthest_point
    point1above, point1below = create_segment(p1, farthest_point, segment)
    point2above, point2below = create_segment(p2, farthest_point, segment)

    # only use the segmetns in the same direction, the opposite direction is contained in the convex hull
    if flag == "above":

        convex_hull = convex_hull + upper_lower_hull(p1, farthest_point, point1above, "above")
        convex_hull = convex_hull + upper_lower_hull(farthest_point, p2, point2above, "above")

    else:

        convex_hull = convex_hull + upper_lower_hull(p1, farthest_point, point1below, "below")
        convex_hull = convex_hull + upper_lower_hull(farthest_point, p2, point2below, "below")

    return convex_hull


def quickhull(v):

    if len(v) <= 2:
        
        return v
        
    convex_hull = []

    sort = sorted(v, key = lambda x : x[0])

    p1 = sort[0]
    p2 = sort[-1]

    convex_hull = convex_hull + [p1, p2]
    
    # remove from the list as they are now in the convex hull
    sort.pop(0)
    sort.pop(-1)

    #determine points above and below the line
    above, below = create_segment(p1, p2, sort)
    
    convex_hull = convex_hull + upper_lower_hull(p1, p2, above, "above")
    
    convex_hull = convex_hull + upper_lower_hull(p1, p2, below, "below")

    # return convex_hull
