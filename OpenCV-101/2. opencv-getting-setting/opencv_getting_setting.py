# Load libraries
import argparse
import cv2

# Add argument to get input from CLI
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, help="Input image", required=True)
args = vars(ap.parse_args())

# Read the original image
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
print(f"Width, Height of the image: {w} x {h}")

# Show the original image
cv2.imshow("Original", image)
# cv2.waitKey(0)

# Grab the individual pixels by manipulating numpy ndarrays
(b, g, r) = image[0, 0]
print(f"Channels[ 0, 0]: Red={r}, Green={g}, Blue={b}")

# Grab channel values at x=50, y=20
(b, g, r) = image[
    20, 50
]  # Here y=20 goes first because that is row part, and then x=50 part
print(f"Channels[20,50]: Red={r}, Green={g}, Blue={b}")


# Set the pixel value of image at x=50, y=20
image[20, 50] = (0, 0, 255)  # Set red color
(b, g, r) = image[
    20, 50
]  # Here y=20 goes first because that is row part, and then x=50 part
print(f"Channels[20,50]: Red={r}, Green={g}, Blue={b}")

cv2.imshow("Updated[20,50]", image)
cv2.waitKey(0)
