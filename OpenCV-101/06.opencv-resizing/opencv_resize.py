# Usage
# python opencv_resize.py -i ../../Data/Input/opencv_logo.png

# import the libraries
import cv2
import argparse
import imutils

# Add arguments from command line args
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, help="Input image", required=True)
args = vars(ap.parse_args())

# Load the image and display original
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Grab image width and height from its shape
(h, w) = image.shape[:2]

# Resizing an image to specific width or height requires maintaining the aspect ratio of the image.
# Resize the given image to width=150 pixels
# Compute aspect ratio of the image
r = 150.0 / w
new_shape = (150, int(h * r))
resized = cv2.resize(image, new_shape, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (W=150)", resized)

# Resize image with height=100 pixels
r = 100.0 / h
new_shape = (int(w * r), 100)
resized = cv2.resize(image, new_shape, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (H=100)", resized)


# Use imutils.resize method to resize image easily
resized = imutils.resize(image, width=150)
cv2.imshow("imutils.resized (W=150)", resized)

resized = imutils.resize(image, height=100)
cv2.imshow("imutils.resized (H=100)", resized)

cv2.waitKey(0)


# construct the list of interpolation methods in OpenCV
methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4),
]

for method in methods:
    # Resize the image width to three times
    print(f"Format={method}")
    resized = imutils.resize(image, width=w * 3, inter=method[1])
    cv2.imshow("Resized", resized)
    cv2.waitKey(0)

# When we resize image to higher, then CUBIC, LANCZOS4 works better
# When we resize image to lower, then NEAREST, LINEAR works better
