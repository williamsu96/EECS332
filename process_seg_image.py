import cv2
import numpy
from scipy.spatial import distance

def max_contour(contours):
    # Iterates through a list of contours and return an index with the largest number of vertices (longest contour)
    max_contour_index = 0
    max_contour_len = 0
    if len(contours) == 0:
        raise Exception('Invalid/empty list of contours')
    else:
        for i in range(0, len(contours)):
            if (len(contours[i]) > max_contour_len):
                max_contour_index = i
        return max_contour_index

def furthest_vertex(defects, contour, centroid):
    # Takes in a defect object via cv2.convexityDefect, a contour via cv2.findContours, and the centroid of the contour
    # Returns the index to the vertex with greatest distance from the centroid
    max_vertex_dist = 0
    max_vertex_index = 0
    for i in range(0, defects.shape[0]):
        start, _, _, _ = defects[i,0] #only need start vertex index
        dist = distance.euclidean(centroid, contour[start])
        if dist > max_vertex_dist:
            max_vertex_dist = dist
            max_vertex_index = start

    return max_vertex_index



def find_finger_point(frame):
    # takes in a segmented frame (hand-only) and returns a cartesian coordinate (x,y)

    # TODO: Find contour of image
    cv2.findContours()
    # TODO: Find centroid of image
    # TODO: Find point on the contour furthest from image
