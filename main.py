import segment_hand
import generate_histogram
import cv2

if __name__ == "__main__":
    # demo: after aligning your hand with the rectangles, press space to capture + generate histogram and then press
    # any key to close picture
    histogram = generate_histogram.generate_histogram_from_webcam()

    webcam = cv2.VideoCapture(0)
    while True:
        ret_val, img = webcam.read()
        cv2.imshow('webcam', img)

        segmented_img = segment_hand.segment_hand(histogram,
                                                  img)  # TODO: takes histogram and current webcam img and returns segmented output

        # TODO: function that identifies the finger tip as a cartesian coordinate

        # TODO: function that stores fingertip positions and draws each one onto img

        if cv2.waitKey(0):
            break
    cv2.destroyAllWindows()
