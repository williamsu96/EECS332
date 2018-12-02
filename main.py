import segment_hand
import generate_histogram
import process_seg_image
import cv2

if __name__ == "__main__":
    # demo: after aligning your hand with the rectangles, press space to capture + generate histogram and then press
    # any key to close picture
    histogram = generate_histogram.generate_histogram_from_webcam()
    draw_points = []
    draw_length = 100
    point_radius = 10
    webcam = cv2.VideoCapture(0)
    while True:
        ret_val, img = webcam.read()

        segmented_img = segment_hand.segment_hand(histogram,
                                                  img)

        # TODO: function that identifies the finger tip as a cartesian coordinate
        draw_points.append(process_seg_image.find_finger_point(segmented_img))
        if len(draw_points) > draw_length:
            del(draw_points[0])
        for i in range(len(draw_points)):
            cv2.circle(img, draw_points[i], point_radius, (0, 0, 255), -1)
        cv2.imshow('webcam', img)
        if cv2.waitKey(1) == 32:
            break
    cv2.destroyAllWindows()
