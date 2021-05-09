# Usage
# python opencv_flip.py -i ../../Data/Input/opencv_logo.png

# Load the libraries
import cv2
import argparse

# Add arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load an image from args
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

# Flip the image vertically (flipcode = 1)
flipped_v = cv2.flip(image, flipCode=1)
cv2.imshow("Flipped Vertically", flipped_v)

# Flip the image horizontally (flipCode = 0)
flipped_h = cv2.flip(image, flipCode=0)
cv2.imshow("Flipped horizontally", flipped_h)

# Flip the image on both the axes
flipped = cv2.flip(image, flipCode=-1)
cv2.imshow("Flipped Both", flipped)

cv2.waitKey(0)
