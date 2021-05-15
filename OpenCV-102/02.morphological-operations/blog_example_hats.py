# Usage
# python blog_example_hats.py

# Import libraries
import cv2
import argparse
import imutils

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, help="Input image",
                default='../../Data/Input/car_dark_bg.jpg')
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
# Resize image to 600x400
resized = imutils.resize(image, width=600)
# Convert to grayscale image
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# Show original and grayscale images
cv2.imshow(
    f"Original: ({image.shape[1]},{image.shape[0]})", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Grayscale", gray)
cv2.imshow(f"Resized: ({resized.shape[1]},{resized.shape[0]})", resized)

# Kernel size has been several hit and trial to get almost perfect.
# Idea behind kernel is tha license plates are usually in 4:1 ratio (width:height)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 5))

# Perform TopHat: Difference between grayscale image and opening. This will give bright foreground over dark background
top_hat = cv2.morphologyEx(gray.copy(), cv2.MORPH_TOPHAT, kernel)
cv2.imshow("TopHat", top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Grayscale", gray)
cv2.imshow(f"Resized: ({resized.shape[1]},{resized.shape[0]})", resized)

# Perform BlackHat: Difference between grayscale image and closing. This will give dark foreground over light background
black_hat = cv2.morphologyEx(gray.copy(), cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
