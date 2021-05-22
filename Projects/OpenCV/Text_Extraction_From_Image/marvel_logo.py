# Usage
# python marvel_logo.py -i Data/Input/marvel_logo.jpg -o Data/Output/marvel_logo/

# Import libraries
import cv2
import argparse
import numpy as np

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
                required=True, help="Input image path")
ap.add_argument("-o", "--output", type=str,
                required=True, help="Output folder path")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

# We need to invert the colors because we need marvel logo chars in white
# To inverse, we can do bitwise_not
image_inv = cv2.bitwise_not(image)
cv2.imshow("Inverted", image_inv)

erosion = False
opening = False
if erosion:
    # As we can see logo characters are attached to each other, so we need to disconnect them before applying Connected component analysis.
    # To disconnect, let's try Erosion method
    iters = range(3, 10)

    for i in iters:
        eroded = cv2.erode(image_inv.copy(), None, iterations=i)
        cv2.imshow(f"Eroded:{i} times", eroded)
        cv2.waitKey(0)
    # Erosion doesn't help because on 7th iteration character itself erodes, but R and V charas are still connected.
    cv2.destroyAllWindows()

if opening:
    # Let's try with Opening operation
    kernel_sizes = range(7, 21, 2)
    for kernel_size in kernel_sizes:
        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT, (kernel_size, kernel_size))
        opened = cv2.morphologyEx(
            image_inv.copy(), cv2.MORPH_OPEN, kernel)
        cv2.imshow(f"Opened:{kernel_size}", opened)
        cv2.waitKey(0)
    # Opening operation doesn't work either as it destroys "R" character after applying some kernel_size
    cv2.destroyAllWindows()

# Let's apply Opening for kernel_size (13, 13) and then apply erosion
kernel_size = (13, 13)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
opened = cv2.morphologyEx(
    image_inv.copy(), cv2.MORPH_OPEN, kernel)
cv2.imshow("Opened", opened)
# Now apply erosion to see if we can disconnect R and V chars.
iters = range(1, 15)
for i in iters:
    eroded = cv2.erode(opened.copy(), None, cv2.CV_32F, iterations=i)
    cv2.imshow(f"Eroded:{i} times", eroded)
    cv2.waitKey(0)

# cv2.waitKey(0)
cv2.destroyAllWindows()
