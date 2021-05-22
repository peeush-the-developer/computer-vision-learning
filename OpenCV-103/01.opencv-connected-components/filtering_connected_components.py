# Usage
# python filtering_connected_components.py -i ../../Data/Input/png/coins01.png

# Import libraries
import cv2
import argparse
import numpy as np

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
T, thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
print('Threshold value: ', T)

cv2.imshow("Thresholded", thresh)

# Calculate connected components
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
    thresh, 4, cv2.CV_32S)

# Create a mask that contains characters from license plate
mask = np.zeros(gray.shape, dtype="uint8")

# We are starting with 1 and not 0 because we don't want to analyse background in the image.
for i in range(1, num_labels):
    # Get stats and centroid
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    a = stats[i, cv2.CC_STAT_AREA]
    (cX, cY) = centroids[i]

    keepWidth = (w > 10) and (w < 50)
    keepHeight = (h > 45) and (h < 65)
    keepArea = (a > 450) and (a < 1500)
    print(f'{i+1}/{num_labels} ', w, h, a)
    if all((keepWidth, keepHeight, keepArea)):
        print(f'x={x},y={y},w={w},h={h},a={a}')

        # Mask
        compMask = (labels == i).astype("uint8") * 255
        mask = cv2.bitwise_or(mask, compMask)


cv2.imshow("Original", image)
cv2.imshow("Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
