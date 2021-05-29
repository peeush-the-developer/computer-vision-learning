# Usage
# python histogram_with_mask.py

# Import the libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Define function to plot the image histogram's


def plot_histogram(image, title, mask=None):
    '''
    Plot the histogram for each channel in the image
    '''

    channels = cv2.split(image)
    colors = ('b', 'g', 'r')
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
    for chan, color in zip(channels, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])


# Load the image
image = cv2.imread("../../Data/Input/png/beach.png")
plot_histogram(image, "Histogram for original image")

# Build mask to show a region of interest
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (60, 290), (210, 390), 255, -1)
cv2.imshow("Mask", mask)

roi = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("ROI", roi)
plot_histogram(image, "Histogram for ROI image", mask=mask)

plt.show()
