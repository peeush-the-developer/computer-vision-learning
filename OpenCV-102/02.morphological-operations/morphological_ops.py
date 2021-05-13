# Usage
# python morphological_ops.py -i ../../Data/Input/pyimagesearch_logo.png

# Load the libraries
import cv2
import argparse

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load image into memory
image = cv2.imread(args["input"])
# Convert BGR to Gray scale image (as we need binary image to work with morphological operations)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Display original and gray images
cv2.imshow("Original", image)
cv2.imshow("Gray", gray)

# Morphological operations
# 1. Erode - Erodes pixels from foreground
for i in range(3):
    eroded = cv2.erode(gray.copy(), None, iterations=i+1)
    cv2.imshow(f'Eroded: {i+1} times', eroded)

# 2. Dilation - Dilates pixels in foreground
for i in range(3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
    cv2.imshow(f'Dilated: {i+1} times', dilated)

kernel_sizes = [(3, 3), (5, 5), (7, 7)]
# 3. Opening - Erosion followed by Dilation
# It helps in removing the noise in the binary image

for kernel_size in kernel_sizes:
    # Get the structuring element i.e. kernel to apply morpholigical operation on the binary image.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    opened = cv2.morphologyEx(gray.copy(), cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Opened: ({kernel_size[0]},{kernel_size[1]})", opened)

# 4. Closing - Dilation followed by Erosion
# It helps in closing holes

for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    closed = cv2.morphologyEx(gray.copy(), cv2.MORPH_CLOSE, kernel)
    cv2.imshow(f"Closed: ({kernel_size[0]}, {kernel_size[1]})", closed)

# 5. Gradient - Difference between Dilation and Erosion
# It helps in outlining the objects in an image
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    grad = cv2.morphologyEx(gray.copy(), cv2.MORPH_GRADIENT, kernel)
    cv2.imshow(f"Gradient: ({kernel_size[0]}, {kernel_size[1]})", grad)

cv2.waitKey(0)
