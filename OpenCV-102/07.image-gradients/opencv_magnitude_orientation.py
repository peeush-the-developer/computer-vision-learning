# Usage
# python opencv_magnitude_orientation.py -i ../../Data/Input/coins01.png

# Import libraries
import cv2
import argparse
import matplotlib.pyplot as plt
import numpy as np

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grayscale", gray)

# Compute gradients
gX = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
gY = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

# Magnitude
magnitude = np.sqrt((gX ** 2) + (gY ** 2))

# Orientation
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

# Plot figures to see them together
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))

# Add plots
axs[0].imshow(gray, cmap="gray")
axs[1].imshow(magnitude, cmap="jet")
axs[2].imshow(orientation, cmap="jet")

# Add titles
axs[0].set_title("Grayscale image")
axs[1].set_title("Magnitude")
axs[2].set_title("Orientation")

# Remove ticks from x and y axis
for i in range(3):
    axs[i].get_xaxis().set_ticks([])
    axs[i].get_yaxis().set_ticks([])

# Show plots
plt.tight_layout()
plt.show()
