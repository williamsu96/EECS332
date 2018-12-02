import cv2
import numpy

def max_contour(contours):
    # Looks through a list of contours and return an index with the largest number of vertices (longest contour)
    max_contour_index = 0
    max_contour_len = 0
    if len(contours) == 0:
        raise Exception('Invalid/empty list of contours')
    else:
        for i in range(0, len(contours)):
            if (len(contours[i]) > max_contour_len):
                max_contour_index = i
        return max_contour_index

def find_finger_point(frame):
    # takes in a segmented frame (hand-only) and returns a cartesian coordinate (x,y)

    # TODO: Find contour of image
    cv2.findContours()
    # TODO: Find centroid of image
    # TODO: Find point on the contour furthest from image
