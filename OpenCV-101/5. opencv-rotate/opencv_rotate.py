# Load the libraries
import argparse
import cv2
import imutils

# Add arguments from command line
ap = argparse.ArgumentParser()
ap.add_argument(
    "-i", "--image", type=str, default="opencv_logo.png", help="Input image"
)
args = vars(ap.parse_args())

# Load the image and display original
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Compute center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)


# Now, rotate the image from center of image towards counter-clockwise direction
# +ve angle rotates the image in counter-clockwise direction
# scale scales the image.
# Step 1: Get rotation matrix from cv2 method for particular rotation degree and the point co-ordinates
# Step 2: Apply the rotation matrix using cv2.warpAffine method on the image
M = cv2.getRotationMatrix2D(center=(cX, cY), angle=45, scale=1.0)
rotated_1 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated[45]", rotated_1)

# Rotate the image by 90 degrees towards counter-clockwise direction
M = cv2.getRotationMatrix2D(center=(cX, cY), angle=90, scale=1.0)
rotated_2 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Roated[90]", rotated_2)

# Rotate image by 90 clockwise and scale to twice
M = cv2.getRotationMatrix2D(center=(cX, cY), angle=-90, scale=2.0)
rotated_3 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated[-90], Scaled[2.0]", rotated_3)


# Using imutils.rotate function which is just a single line of code
rotated_4 = imutils.rotate(image, angle=90)
cv2.imshow("imutils.Rotated[90]", rotated_4)


# Drawback of both the above methods is that when image is rotated, it is cropped off from areas outside image actual area.
# To fix that, we can use imutils.rotate_bound method
rotated_Fixed = imutils.rotate_bound(image, angle=90)
cv2.imshow("imutils.Rotated[90] bound", rotated_Fixed)
cv2.waitKey(0)
