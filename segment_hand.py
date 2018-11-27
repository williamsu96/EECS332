import cv2 #import OpenCV
import matplotlib
# matplotlib.use("TkAgg")
import numpy
import copy
from matplotlib import pyplot as plt

def segment_hand():
    # plt.switch_backend('QT4agg')

    img = cv2.imread('finger.png')
    img_out = copy.deepcopy(img)

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # # Displaying original image
    # cv2.imshow('figure: original',img)
    # cv2.imshow('figure: grayscale', img_gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Image dimensions
    rows = img.shape[0]
    cols = img.shape[1]

    box_rows = int(rows / 10 / 2)
    box_cols = int(cols / 10 / 2)
    rect_centers = numpy.array([[rows / 3, cols / 3], [rows * 2 / 3, cols / 3], [rows / 3, cols * 2 / 3], [rows * 2 / 3, cols * 2 / 3]])
    sub_img = [0] * 4;
    for i in range(0, 4):
        x = int(numpy.round(rect_centers[i, 0]))
        y = int(numpy.round(rect_centers[i, 1]))
        sub_img[i] = img_hsv[(y - box_rows):(y + box_rows), (x - box_cols):(x + box_cols), :]
            #coordinates of the sections of the images we want to take
        cv2.rectangle(img_out, (y - box_rows, x - box_cols), (y + box_rows, x + box_cols), (255, 0, 0), 1) #drawing squares
    cv2.imwrite("finger_sq_overlay.png", img_out) # write-image-to-file

    hist_ = cv2.calcHist([sub_img[0], sub_img[1], sub_img[2], sub_img[3]], [1, 2], None, [10,10], [0, 256, 0, 256])
        # test histogram: calculates a histogram based on the sub-sections of the image
    hist = cv2.calcHist([img_hsv], [0, 1], None, [50, 50], [0, 256, 0, 256])
        # test histogram: calculates a histogram based on the entire image

    # cv2.imshow('figure: Histogram', hist)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    plt.imshow(hist, interpolation='nearest')
    plt.savefig('histogram.png') # saving the histogram as a 2D-plot
    # plt.plot(hist) #backend doesn't work - not sure why

    # plt.show()
