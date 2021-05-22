# Usage
# python main.py -i Data/Input/Fire_exit.jpeg -c Data/Input/Fire_exit.json

# Import libraries
import cv2
import argparse
import numpy as np
import json

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="Input image")
ap.add_argument("-c", "--config", type=str, required=True, help="Config json")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["image"])
print(f'Original shape', image.shape)

# Load config
# Opening JSON file
with open(args["config"]) as json_file:
    config = json.load(json_file)

roi = config["roi"]

# Guess the top-left corner and width, height for rectangle to crop only text
x, y, w, h = roi["x"], roi["y"], roi["w"], roi["h"]
cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow("Original", image)

# Now, we have the rectangle, we can crop the image with text.
text_image = image[y:y+h, x:x+w]
# print(f'Text image shape', text_image.shape)
cv2.imshow("Text image", text_image)

# Convert to gray scale and threshold with OTSU
gray = cv2.cvtColor(text_image, cv2.COLOR_BGR2GRAY)
T, thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow("Thresholded", thresh)
cv2.waitKey(0)

# # As we can see there is noise in the top left corner, we'll try to apply opening to reduce noise
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
# thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# cv2.imshow("Thresholded", thresh)

# Get Connected components in the binary image
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
    thresh, 4, cv2.CV_32S)

# Create mask to contain characters
mask = np.zeros(gray.shape, dtype="uint8")

chars_stats = config["chars_stats"]

# Filter connected components
for i in range(1, num_labels):
    # print(f'{i+1}/{num_labels}')
    # Get stats
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    a = stats[i, cv2.CC_STAT_AREA]

    compMask = (labels == i).astype("uint8") * 255
    # cv2.imshow("CompMask", compMask)
    # cv2.waitKey(0)

    keepWidth = w > chars_stats["width"]["min"] and w < chars_stats["width"]["max"]
    keepHeight = h > chars_stats["height"]["min"] and h < chars_stats["height"]["max"]
    keepArea = a > chars_stats["area"]["min"] and a < chars_stats["area"]["max"]
    if config["verbose"]:
        print(f'{i+1}/{num_labels}', x, y, w, h, a)
    if all((keepWidth, keepHeight, keepArea)):
        compMask = (labels == i).astype("uint8") * 255
        mask = cv2.bitwise_or(mask, compMask)

cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
