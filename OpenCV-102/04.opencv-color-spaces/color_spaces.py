# Usage
# python color_spaces.py -i ../../Data/Input/Dog.jpg

# Import libraries
import cv2
import argparse

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

# RGB Color space
# When we load the image, it is in BGR mode.
for name, chan in zip(('b', 'g', 'r'), cv2.split(image)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Display the original image again
cv2.imshow("Original", image)

# HSV Color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

for name, chan in zip(('h', 's', 'v'), cv2.split(hsv)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Display the original image again
cv2.imshow("Original", image)

# LAB color space
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

for name, chan in zip(('l', 'a', 'b'), cv2.split(lab)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Display the original image again
cv2.imshow("Original", image)

# Grayscale from bgr

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
