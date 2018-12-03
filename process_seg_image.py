import cv2
import numpy as np
from scipy.spatial import distance

def noise_filter_CCL(seg_img, connectivity, mask_threshold):
    seg_img_gray = cv2.cvtColor(seg_img, cv2.COLOR_BGR2GRAY)
    output = cv2.connectedComponentsWithStats(seg_img_gray, connectivity, cv2.CV_32S)
    labels = output[1]
    stats = output[2]
    delete_list = []
    for i in range(0, stats.shape[0]):
        if stats[i,4] < mask_threshold:
            delete_list.append(i)

    for i in delete_list:
        labels[labels == i] = 0

    labels[labels != 0] = 1
    # for i in range(3):
    #     labels[:, :, i] = labels.copy()
    mask = labels.astype(np.uint8)
    ret_ccl = cv2.bitwise_and(seg_img, seg_img, mask = mask)

    # while(1):
    #     cv2.imshow('ccl', ret_ccl)
    #     if cv2.waitKey(1) == 32:
    #         break
    return ret_ccl


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
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Find contour of image
    ret, thresh = cv2.threshold(frame, 80, 255, cv2.THRESH_BINARY)
    im, contours, hierarchy = cv2.findContours(thresh, 1, 2)

    # Find centroid of largest contour
    if contours is not None:
        try:
            max_contour_index = max_contour(contours)
        except:
            return(-1,-1)

        hand_contour = contours[max_contour_index]

        # Find point furthest away from centroid on contour perimeter
        M = cv2.moments(hand_contour)
        try:
            centroid_y = (M["m01"] / M["m00"])
            centroid_x = (M["m10"] / M["m00"])
        except:
            return(-1,-1)

        centroid_yx = (centroid_y, centroid_x)
        centroid_rowcol = (int(np.round(centroid_y)), int(np.round(centroid_x)))  # stored in row, col form
        hand_hull = cv2.convexHull(hand_contour, returnPoints=False)
        hand_defects = cv2.convexityDefects(hand_contour, hand_hull)
        # cv2.convexityDefects returns an object that contains the following attributes
            # start point of defect
            # end point of defect
            # furthest point from the convex hull within the defect
            # approximate distance of the defect
        try:
            hand_defects.shape[0]
        except:
            return (-1,-1)
        furthest_vertex_index = furthest_vertex(hand_defects, hand_contour, centroid_rowcol)
        finger_point = hand_contour[furthest_vertex_index]
        finger_point = (finger_point[0, 0], finger_point[0, 1])
        return finger_point
    else:
        return (-1,-1)

    ### show image for debug
    # cv2.circle(im_original, finger_point, 3, (255, 0, 0), 3)
    # cv2.circle(im_original, centroid_rowcol, 3, (0, 255, 0), 5)
    # while (1):
    #     cv2.imshow('original image', im_original)
    #     if cv2.waitKey(1) == 32:
    #         break
    # while (1):
    #     cv2.imshow('thresholded image', thresh)
    #     if cv2.waitKey(1) == 32:
    #         break
    # cv2.destroyAllWindows()