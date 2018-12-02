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

        segmented_img = segment_hand.segment_hand(histogram,
                                                  img)  # TODO: takes histogram and current webcam img and returns segmented output

        # TODO: function that identifies the finger tip as a cartesian coordinate

        # TODO: function that stores fingertip positions and draws each one onto img

        # cv2.imshow('webcam', img)
        cv2.imshow('webcam', segmented_img)
        if cv2.waitKey(1)==32:
            cv2.imwrite('hand.jpg', segmented_img)
            break
    cv2.destroyAllWindows()
