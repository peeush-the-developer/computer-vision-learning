# Usage
# python opencv_masking.py -i ../../Data/Dog.jpg

# Load the libraries
import cv2
import argparse
import numpy as np

# Load the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

# Create rectangular mask for showing only dog's body
M = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(M, (2000, 350), (2900, 2100), 255, -1)
cv2.imshow("Rectangular Mask", M)

# Perform Bitwise and to remove background from image
masked = cv2.bitwise_and(image, image, mask=M)
cv2.imshow("Masked", masked)

# Circular mask
M = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(M, (2450, 650), 300, 255, -1)
cv2.imshow("Circular mask", M)

# Perform Bitwise and to remove background from image and only fetch dog's face
masked = cv2.bitwise_and(image, image, mask=M)
cv2.imshow("Masked face", masked)

cv2.waitKey(0)
