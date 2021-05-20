# Usage
# python opencv_sobel_scharr.py -i ../../Data/Input/bricks.png

# Import libraries
import cv2
import argparse

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
ap.add_argument("-s", "--scharr", type=bool, default=False,
                help="Set True if Scharr operator applied")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
cv2.imshow("Original", image)

# Convert to grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Set kernel size based on Sobel or Scharr operator
ksize = -1 if args["scharr"] else 3

# Apply Sobel to get Gradient in X and Y directions
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

# gX and gY have been in floating space, we need to convert them back to 8-bit unsigned integer space
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# Combined gradients into 1 image
combined = cv2.addWeighted(gX, alpha=0.5, src2=gY, beta=0.5, gamma=0)

# Show gX, gY gradient images
cv2.imshow("Gradient X", gX)
cv2.imshow("Gradient Y", gY)
cv2.imshow("Combined", combined)


cv2.waitKey(0)
cv2.destroyAllWindows()
