# Usage
# python simple_equalization.py -i ../../Data/Input/dog.png

# Import libraries
import argparse
import cv2
import matplotlib.pyplot as plt


# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
                required=True, help="Input image path")
args = vars(ap.parse_args())


def plot_histogram(image, title):
    # Calculate histogram for image
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist /= hist.sum()
    plt.figure()
    plt.plot(hist)
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")


# Load the image
image = cv2.imread(args["input"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
plot_histogram(gray, "Histogram for the grayscale image")

# Equalize the pixel intensities
equalized = cv2.equalizeHist(gray)
cv2.imshow("Equalized", equalized)
plot_histogram(equalized, "Histogram for the equalized image")

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.show()
