# Usage
# python blurring.py -i ../../Data/Input/Dog.jpg

# Import the libraries
import cv2
import argparse

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the input image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

cv2.waitKey(0)

kernel_sizes = [(3, 3), (9, 9), (15, 15)]

# Apply average blurring technique
for kernel_size in kernel_sizes:
    blurred = cv2.blur(image, kernel_size)
    cv2.imshow(f"Blurred ({kernel_size[0]}, {kernel_size[1]})", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Original", image)

# Apply Gaussian blur
for kernel_size in kernel_sizes:
    blurred_g = cv2.GaussianBlur(image, kernel_size, 0)
    cv2.imshow(
        f"Gaussian Blurred ({kernel_size[0]}, {kernel_size[1]})", blurred_g)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Original", image)

# Apply median blur
for kernel_size in [3, 9, 15]:
    blurred_m = cv2.medianBlur(image, kernel_size)
    cv2.imshow(
        f"Median Blurred ({kernel_size})", blurred_m)

cv2.waitKey(0)
cv2.destroyAllWindows()
