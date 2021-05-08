# Load the libraries
import numpy as np
import cv2
import argparse
import imutils

# add arguments from Command line
ap = argparse.ArgumentParser()
ap.add_argument(
    "-i", "--image", type=str, default="opencv_logo.png", help="input image"
)
args = vars(ap.parse_args())

# By translate operation, we mean to move image pixels up, down, left or right.
# for opencv translate operation, we need to define a 2-d matrix as 2x3 as following:
# M = [
#       [1 0 shiftX]        # shiftX: +ve value translates into right, -ve value translates into left
#       [0 1 shiftY]        # shiftY: +ve value translates into down, -ve value translates into up
#   ]

# Input image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Let's translate input image in 25 pixels right and 50 pixels down
# 1. Define a translation matrix, M
# 2. Apply warpAffine operation from cv2 to apply translation to image
(right, down) = (25, 50)
M = np.float32([[1, 0, right], [0, 1, down]])
shift_1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Right(25) and Down(50)", shift_1)

# Let's translate input image 50 pixels left and 75 pixels up
# 1. Define a translation matrix, M
# 2. Apply warpAffine operation from cv2 to apply translation to image
(right, down) = (-50, -75)
M = np.float32([[1, 0, right], [0, 1, down]])
shift_2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Left(-50) and Up(-75)", shift_2)


# Use imutils package to apply translation easily
# Shift 10 right and 80 down
shift_3 = imutils.translate(image, 10, 80)
cv2.imshow("Shifted Right(10) and Down(80)", shift_3)
cv2.waitKey(0)
