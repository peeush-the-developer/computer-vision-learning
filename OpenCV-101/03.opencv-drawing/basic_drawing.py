# Load numpy and cv2 libraries
import numpy as np
import cv2
import argparse

# Add arguments from CommandLine for width and height
ap = argparse.ArgumentParser()
ap.add_argument("-img_w", "--width", type=int, default=300, help="width of the image")
ap.add_argument("-img_h", "--height", type=int, default=300, help="Height of the image")
args = vars(ap.parse_args())

# Fetch width and height from arguments
img_w = args["width"]
img_h = args["height"]

# Fetch ratio of width is to height
ratio = img_w / img_h

# Create an empty canvas of size=600x600 pixels with black background
canvas = np.zeros((img_h, img_w, 3), dtype="uint8")

# Note: Co-ordinate in line or other shapes is (x, y) => x = img_w, y = img_H
# Draw a green line from top-left to bottom-right
green = (0, 255, 0)
line1 = cv2.line(canvas, (0, 0), (img_w, img_h), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a thick red line from top-right to bottom-left
red = (0, 0, 255)
line2 = cv2.line(canvas, (img_w, 0), (0, img_h), red, 2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Find center of canvas
(centerX, centerY) = (img_w // 2, img_h // 2)

# Draw a rectangle on line1 of width=50
rect1_X1 = centerX - 50
rect1_Y1 = int(rect1_X1 / ratio)
rect1 = cv2.rectangle(canvas, (rect1_X1, rect1_Y1), (centerX, centerY), red)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a solid rectangle on line2 of width=100
rect2_Y2 = centerY - 100
rect2_X2 = int(rect2_Y2 * ratio) + centerX
rect2 = cv2.rectangle(canvas, (centerX, centerY), (rect2_X2, rect2_Y2), green, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a solid circle of radius=50 from center of canvas
blue = (255, 0, 0)
circle1 = cv2.circle(canvas, (centerX, centerY), 25, blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a circle of radius=75 from center of canvas
circle2 = cv2.circle(canvas, (centerX, centerY), 75, red, 2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
