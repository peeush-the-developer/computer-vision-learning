# Usage
# python bilateral.py -i ../../Data/Input/car.png

# Import the libraries
import cv2
import argparse

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
                required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

cv2.waitKey(0)

# Bilateral blurring parameters
# - Diameter    - similar to kernel size
# - sigma color - Intensity of the color distribution
# - sigma space - How far the space to be computed

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for (dia, sc, ss) in params:
    blurred = cv2.bilateralFilter(image, dia, sc, ss)
    cv2.imshow(f"Blurred: d={dia},sc={sc},ss={ss}", blurred)
    cv2.waitKey(0)
