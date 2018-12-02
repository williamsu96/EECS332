import cv2
import numpy

def find_finger_point(frame):
    # takes in a segmented frame (hand-only) and returns a cartesian coordinate (x,y)

    # TODO: Find contour of image
    cv2.findContours()
    # TODO: Find centroid of image
    # TODO: Find point on the contour furthest from image
