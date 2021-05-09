# Usage
# python opencv_crop.py -i ../../Data/Input/Dog.jpg

# Load the libraries
import cv2
import argparse

# Add arguments from command line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
ap.add_argument("-o", "--output", type=str, required=True,
                help="Output image folder path")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

(h, w) = image.shape[:2]

# Fetch dog face from the image
face = image[350:900, 2200:2700]
cv2.imshow("Cropped Face", face)

# Fetch other part from the image
other = image[900:, 2700:]
cv2.imshow("Cropped Other", other)

cv2.waitKey(0)
