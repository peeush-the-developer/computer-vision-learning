# Usage
# python image_arithmetic.py -i ../../Data/Input/grand_canyon.png

# import libraries
import cv2
import numpy as np
import argparse

# Add arguments from command line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

# OpenCV provides "add", "subtract" operations to perform image arithmetic operations.
# Adding values to image will make the image lighter. cv2.add operation maximizes the pixel values till 255 if we set above 255.
# Subtracting values from image will make the image darker. cv2.subtract operation minimizes the pixel values to 0 if we set below 0.
added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
print("cv2.add maximizes to 255 (if > 255): {}".format(added))
print("cv2.subtract minimizes to 0 (if < 0): {}".format(subtracted))

# Similarly we can add or subtract array to/from image
M = np.ones(image.shape, dtype=np.uint8) * 100
added = cv2.add(image, M)
cv2.imshow("Lighter", added)

# Darker image
M = np.ones(image.shape, dtype=np.uint8) * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Darker", subtracted)


cv2.waitKey(0)
