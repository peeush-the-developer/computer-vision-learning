# Usage
# python morphological_hats.py -i ../../Data/Input/car.png

# Import libraries
import cv2
import argparse

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
# convert BGR to Gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Show grayscale image
cv2.imshow("Grayscale", gray)

# Perform TopHat or WhiteHat operation
# Top hat or White Hat is the difference between grayscale image and opening of image.
# This highlights the bright parts in an image on dark background.
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
white_hat = cv2.morphologyEx(gray.copy(), cv2.MORPH_TOPHAT, kernel)
cv2.imshow("WhiteHat", white_hat)

# Perform Black Hat operation
# Black hat is the difference between grayscale image and closing of image.
# This highlights the dark parts in an image on light background.
black_hat = cv2.morphologyEx(gray.copy(), cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat", black_hat)


cv2.waitKey(0)
