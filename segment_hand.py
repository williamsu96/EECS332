import cv2 #import OpenCV
import matplotlib
# matplotlib.use("TkAgg")
import numpy
from matplotlib import pyplot as plt

def segment_hand():
    # plt.switch_backend('QT4agg')

    img = cv2.imread('finger.png')
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # # Displaying original image
    # cv2.imshow('figure: original',img)
    # cv2.imshow('figure: grayscale', img_gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    rows = img.shape[0]
    cols = img.shape[1]
    box_rows = int(rows / 10 / 2)
    box_cols = int(cols / 10 / 2)
    rect_centers = numpy.array([[cols / 3, rows / 3], [cols / 3, rows * 2 / 3], [cols * 2 / 3, rows / 3], [cols * 2 / 3, rows * 2 / 3]])
    sub_img = [0] * 4;
    for i in range(0, 4):
        x = int(numpy.round(rect_centers[i, 0]))
        y = int(numpy.round(rect_centers[i, 1]))
        sub_img[i] = img_hsv[(y - box_rows):(y + box_rows), (x - box_cols):(x + box_cols), :]

    hist = cv2.calcHist([img_hsv], [0, 1], None, [50, 50], [0, 256, 0, 256])
    # cv2.imshow('figure: Histogram', hist)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    plt.imshow(hist, interpolation='nearest')
    plt.savefig('histogram.png')
    # plt.plot(hist) #backend doesn't work - not sure why

    # plt.show()
