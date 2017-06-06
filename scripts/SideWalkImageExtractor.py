import cv2
import numpy as np




def get_color_range(threshold):
    return np.array([threshold, threshold, threshold], dtype=np.uint8)

if __name__ == "__main__":
    img = cv2.imread('path/to/original/image', 1)

    # color threshold for detecting just major roads.
    lower_range = get_color_range(70)
    upper_range = get_color_range(255)

    blurred_img = cv2.GaussianBlur(img, (1, 1), 1, 1)

    # filter based on threshold for larger roads.
    mask = cv2.inRange(blurred_img, lower_range, upper_range)

    # erode to get rid of noise
    eroded_mask = cv2.erode(mask, (1, 1), iterations=1)

    # dilate to fill in holes
    dilated_mask = cv2.dilate(eroded_mask, (1, 1), iterations=1)

    result = cv2.bitwise_and(img, img, mask=dilated_mask)

    # subtract major roads
    major_roads_removed = cv2.absdiff(result, img)

    # color threshold for detecting sidewalks.
    lower_range = get_color_range(35)
    upper_range = get_color_range(70)

    # filter based on threshold for smaller roads.
    mask = cv2.inRange(major_roads_removed, lower_range, upper_range)

    result = cv2.bitwise_and(img, img, mask=mask)

    eroded_result = cv2.erode(result, (10, 10), iterations=1)

    dilated_result = cv2.dilate(eroded_result, (10, 10), iterations=1)

    # detect edges for final result
    end_result = cv2.Canny(dilated_result, 50, 150, apertureSize=3)
