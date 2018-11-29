import cv2  # import OpenCV
import matplotlib
# matplotlib.use("TkAgg")
import numpy
import copy
from matplotlib import pyplot as plt


def segment_hand(histogram, img):
    img_hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    

