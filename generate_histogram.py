import cv2
import numpy
import copy
from matplotlib import pyplot as plt


def histogram(img):  # takes in the picture from the webcam stream and returns its histogram
    img_out = copy.deepcopy(img)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    rows = img.shape[0]
    cols = img.shape[1]
    box_rows = int(rows / 10 / 2)
    box_cols = int(cols / 10 / 2)
    rect_centers = numpy.array(
        [[rows / 3, cols * 2 / 5], [rows * 2 / 3, cols * 2 / 5], [rows / 3, cols * 3 / 5], [rows * 2 / 3, cols * 3 / 5]])
    sub_img = [0] * 4
    for i in range(0, 4):
        x = int(numpy.round(rect_centers[i, 0]))
        y = int(numpy.round(rect_centers[i, 1]))
        sub_img[i] = img_hsv[(y - box_rows):(y + box_rows), (x - box_cols):(x + box_cols), :]
        cv2.rectangle(img_out, (y - box_rows, x - box_cols), (y + box_rows, x + box_cols), (255, 0, 0),
                      1)  # drawing squares

    hist_ = cv2.calcHist([sub_img[0], sub_img[1], sub_img[2], sub_img[3]], [1, 2], None, [10, 10], [0, 256, 0, 256])

    cv2.imshow('webcam', img_out)
    cv2.waitKey(0)
    # uncomment to imshow histogram
    # plt.imshow(hist_)
    # plt.show()]
    return hist_

    # plt.show()


def generate_histogram_from_webcam():
    # loops the webcam stream, draws boxes, then destroys everything after histogram is generated
    webcam = cv2.VideoCapture(0)
    while True:
        ret_val, img = webcam.read()
        rows = img.shape[0]
        cols = img.shape[1]
        box_rows = int(rows / 10 / 2)
        box_cols = int(cols / 10 / 2)
        # rect_centers = numpy.array(
        #     [[rows / 3, cols / 3], [rows * 2 / 3, cols / 3], [rows / 3, cols * 2 / 3], [rows * 2 / 3, cols * 2 / 3]])
        rect_centers = numpy.array(
            [[rows / 3, cols * 2 / 5], [rows * 2 / 3, cols * 2 / 5], [rows / 3, cols * 3 / 5], [rows * 2 / 3, cols * 3 / 5]])
        for i in range(0, 4):
            x = int(numpy.round(rect_centers[i, 0]))
            y = int(numpy.round(rect_centers[i, 1]))
            cv2.rectangle(img, (y - box_rows, x - box_cols), (y + box_rows, x + box_cols), (255, 0, 0),
                          1)  # drawing squares
        cv2.imshow('webcam', img)

        if cv2.waitKey(1) == 32:  # space
            webcam_histogram = histogram(img)
            break
    cv2.destroyAllWindows()
    webcam_histogram = cv2.normalize(webcam_histogram, webcam_histogram, 0, 255, cv2.NORM_MINMAX)
    return webcam_histogram

# if __name__ == "__main__":
#     histogram = generate_histogram_from_webcam()

# plt.imshow(histogram)
# plt.show()
