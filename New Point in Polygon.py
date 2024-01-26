'''
Code is working properly for the environment code, and it should be plug and play, as I have modified it to work with the coordinates of the golf ball and the bunker coordinates.
It returns true if the ball is in the bunker, and false if it is not.
The code has been tested to see if it works with a point in the polygon, and a point outside the polygon. But has not been 
tested to see if it is any faster or more efficient than the previous code.
'''


# Function to check if a point is inside a polygon
def point_in_polygon(ptc, polygon):
    # Get the x and y coordinates of the point
    x, y = ptc

    # Initialize a flag to check if the point is inside the polygon
    inside = False

    # Take the first point in the polygon
    p1 = polygon[0]

    # Loop through each side of the polygon
    for i in range(1, len(polygon) + 1):
        # Take the next point in the polygon
        p2 = polygon[i % len(polygon)]

        # Check if the point is roughly at the same height as the current side
        if y > min(p1[1], p2[1]):

            # Check if the point is not too high above the side or too low below the side
            if y <= max(p1[1], p2[1]):

                # Check if the point is to the left of the rightmost point of the side
                if x <= max(p1[0], p2[0]):

                    # Calculate the x-coordinate where a line from the point intersects with the side
                    x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]

                    # Check if the point is on or to the left of the calculated x-coordinate
                    if p1[0] == p2[0] or x <= x_intersection:

                        # Flip the inside flag, indicating that the point is inside the polygon
                        inside = not inside

        # Move to the next side of the polygon
        p1 = p2

    # Return whether the point is inside the polygon or not
    return inside