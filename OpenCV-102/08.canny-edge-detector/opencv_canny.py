# Usage
# python opencv_canny.py -i ../../Data/Input/coins01.png

# Import libraries
import cv2
import argparse

# Add command-line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Grayscale", blurred)

# Apply canny edge detectors in 3 ranges
wide = cv2.Canny(blurred, 10, 200)
medium = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)

# Show all images with edge detected
cv2.imshow('Canny wide', wide)
cv2.imshow('Canny medium', medium)
cv2.imshow('Canny tight', tight)

cv2.waitKey(0)
cv2.destroyAllWindows()
