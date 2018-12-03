import cv2  # import OpenCV
import matplotlib
# matplotlib.use("TkAgg")
import numpy
import copy
from matplotlib import pyplot as plt


def segment_hand(histogram, img):
    img_hsv = cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
    dst = cv2.calcBackProject([img_hsv], [1, 2], histogram, [0, 179, 0, 255], 1)

    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))
    cv2.filter2D(dst, -1, disc, dst)

    ret, thresh = cv2.threshold(dst, 150, 255, cv2.THRESH_BINARY)

    thresh = cv2.merge((thresh, thresh, thresh))

    return cv2.bitwise_and(img, thresh)



