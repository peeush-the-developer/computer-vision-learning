# Usage
# python morphological_str_elemts.py -i ../../Data/Input/pyimagesearch_logo.png

# Import libraries
import cv2
import argparse

# Add Command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

# Convert to gray scale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

# Kernel size
kernel_size = (5, 5)
# Let's define our structuring element types
str_elemts_types = [cv2.MORPH_RECT, cv2.MORPH_CROSS, cv2.MORPH_ELLIPSE]

# Let's apply these types one by one on Opening operation
for type_ in str_elemts_types:
    kernel = cv2.getStructuringElement(type_, kernel_size)
    opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Opened: {type_}", opened)

# From the output, it looks like RECT (8-neighborhood) works best to reduce noise in the image.

cv2.waitKey(0)
