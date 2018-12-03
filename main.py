import segment_hand
import generate_histogram
import process_seg_image
import cv2

if __name__ == "__main__":
    # demo: after aligning your hand with the rectangles, press space to capture + generate histogram and then press
    # any key to close picture
    histogram = generate_histogram.generate_histogram_from_webcam()
    draw_points = []
    draw_length = 20
    point_radius = 10
    connectivity = 8
    CCL_threshold = 30000
    webcam = cv2.VideoCapture(0)
    while True:
        ret_val, img = webcam.read()
        # img = cv2.resize(img, (0,0), fx=0.5, fy=0.25)

        # Performs image segmentation via histogram generation
        segmented_img = segment_hand.segment_hand(histogram, img)
        segmented_img = process_seg_image.noise_filter_CCL(segmented_img, connectivity, CCL_threshold)
        # Finds point on finger using findContours, convexHull, convexityDefects functions from cv2
        point = process_seg_image.find_finger_point(segmented_img)

        if point != (-1, -1):
            draw_points.append(point)

        # Draw points
        if len(draw_points) > draw_length:
            draw_points.remove(draw_points[0])
        for i in range(len(draw_points)):
            cv2.circle(img, draw_points[i], point_radius, (0, 0, 255), -1)
        cv2.imshow('output', img)
        # cv2.imshow('seg', segmented_img)
        if cv2.waitKey(1) == 32:
            break
    cv2.destroyAllWindows()
