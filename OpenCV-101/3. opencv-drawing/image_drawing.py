# Load libraries cv2, argparse
import cv2
import argparse

# Add arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png", help="Image")
args = vars(ap.parse_args())

# Load original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Draw rectangle, circle around face, eyes respectively
green = (0, 255, 0)
cv2.rectangle(image, (100, 90), (225, 260), green, 2)

red = (0, 0, 255)
cv2.circle(image, (150, 160), 10, red, -1)
cv2.circle(image, (195, 170), 10, red, -1)
cv2.imshow("Update", image)
cv2.waitKey(0)
