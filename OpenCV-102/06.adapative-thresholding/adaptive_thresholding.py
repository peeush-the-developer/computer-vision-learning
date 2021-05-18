# Usage
# python adaptive_thresholding.py -i ../../Data/Input/steve_jobs_vcard.png

# Import libraries
import cv2
import argparse

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

# Apply Grayscale and blurring
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Gray", gray)
cv2.imshow("Blurred", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Blurred", blurred)

# Global Thresholding
# 1. Basic Binary inv thresholding
_, thresh = cv2.threshold(blurred, 230, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Binary Inv Threshold", thresh)

# 2. Otsu's thresholding
T, thresh = cv2.threshold(
    blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow(f"OTSU threshold {T}", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Local thresholding

# thresh_sizes = range(5, 36, 4)
thresh_sizes = [21]
# 1. Mean adaptive thresholding
for thresh_size in thresh_sizes:
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, thresh_size, 10)
    cv2.imshow(f"Mean Adaptive Threshold {thresh_size}", thresh)

    cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Gaussian mean adaptive thresholding
# Note: We should prefer Gaussian adaptive thresholding first and if it not works then go for Mean adaptive threshold.
for thresh_size in thresh_sizes:
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, thresh_size, 4)
    cv2.imshow(f"Gaussian Adaptive Threshold {thresh_size}", thresh)
    cv2.waitKey(0)

cv2.destroyAllWindows()
