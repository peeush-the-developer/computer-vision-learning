# Usage
# python adaptive_equalization.py -i ../../Data/Input/png/Dog.png

# import libraries
import cv2
import argparse
import matplotlib.pyplot as plt

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
                required=True, help="Input image path")
ap.add_argument("-c", "--clip", type=float, default=2.0,
                help="Default thresholding paramter value")
ap.add_argument("-t", "--tile", type=int, default=8,
                help="Grid size (8x8) tiles for the image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

clahe = cv2.createCLAHE(clipLimit=args['clip'],
                        tileGridSize=(args["tile"], args["tile"]))
equalized = clahe.apply(gray)
cv2.imshow("Equalized", equalized)

cv2.waitKey(0)
