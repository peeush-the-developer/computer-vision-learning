# Usage
# python opencv_bitwise.py

# Load the libraries
import cv2
import numpy as np


# Draw a solid rectangle with white color
white = (255, 255, 255)
rect = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rect, (25, 25), (275, 275), white, -1)
cv2.imshow("Rectangle", rect)

# Draw a solid circle with white color
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, white, -1)
cv2.imshow("Circle", circle)

# Bitwise AND on rectangle and circle
bit_and = cv2.bitwise_and(rect, circle)
cv2.imshow("Bitwise AND", bit_and)

# Bitwise OR on rectangle and circle
bit_or = cv2.bitwise_or(rect, circle)
cv2.imshow("Bitwise OR", bit_or)

# Bitwise XOR on rectangle and circle
bit_xor = cv2.bitwise_xor(rect, circle)
cv2.imshow("Bitwise XOR", bit_xor)


# Bitwise NOT on rectangle
bit_not = cv2.bitwise_not(rect)
cv2.imshow("Bitwise NOT", bit_not)

cv2.waitKey(0)
