# Usage
# python simple_thresholding.py -i ../../Data/Input/coins01.png

# Import libraries
import cv2
import argparse

# Add arguments from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

# To apply any thresholding, it is best practice to convert it to grayscale and blur it slightly
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow('Grayscale Blurred', blurred)

# Simple thresholding
# We are checking different threshold values to see the perfect value to define ROI for coins.
# And it looks like 200, 250 were the best to have ROI for coins.
# THRESH_BINARY_INV will set white (255) if pixel value < threshold_check value
# THRESH_BINARY will set white (255) if pixel value > threshold_check value
thresh_checks = [50, 100, 150, 200, 250]
for check in thresh_checks:
    (T, thresh) = cv2.threshold(blurred, check, 255, cv2.THRESH_BINARY_INV)
    print('Threshold Inv check={}'.format(check))
    cv2.imshow(f"Thresholded Inv {check}", thresh)
    cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Grayscale Blurred', blurred)

thresh_checks = [50, 100, 150, 200, 250]
for check in thresh_checks:
    (T, thresh) = cv2.threshold(blurred, check, 255, cv2.THRESH_BINARY)
    print('Threshold check={}'.format(check))
    cv2.imshow(f"Thresholded {check}", thresh)
    cv2.waitKey(0)

# We can use thresh_inv as a mask and then bitwise_and with original image to segment coins out
_, thresh_inv = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
result = cv2.bitwise_and(image, image, mask=thresh_inv)
cv2.imshow("Segmented", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
