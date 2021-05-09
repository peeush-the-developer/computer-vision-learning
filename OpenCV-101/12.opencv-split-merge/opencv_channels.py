# Usage
# python opencv_channels.py -i ../../Data/Input/opencv_logo.png

# Load the libraries
import cv2
import argparse
import numpy as np

# Add arguments from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

# Split the channels into tuple
(b, g, r) = cv2.split(image)
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.imshow("Blue", b)


# Merge individual channels back
merged = cv2.merge((b, g, r))
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Visualize each channel in color
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, r]))
cv2.imshow("Green", cv2.merge([zeros, g, zeros]))
cv2.imshow("Blue", cv2.merge([b, zeros, zeros]))


cv2.waitKey(0)
