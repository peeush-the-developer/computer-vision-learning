# Usage
# python image_drawing.py -i ../../Data/Input/Dog.jpg

# Load libraries cv2, argparse
import cv2
import argparse

# Add arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, help="Input image", required=True)
args = vars(ap.parse_args())

# Load original image
image = cv2.imread(args["image"])
print('Shape of image: ', image.shape)
cv2.imshow("Original", image)

# Draw rectangle, circle around face, eyes respectively
green = (0, 255, 0)
cv2.rectangle(image, (2200, 350), (2700, 900), green, 5)

red = (0, 0, 255)
cv2.circle(image, (2300, 600), 40, red, -1)
cv2.circle(image, (2600, 600), 40, red, -1)
cv2.imshow("Update", image)
cv2.waitKey(0)
