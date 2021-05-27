# Usage
# python grayscale_histogram.py -i ../../Data/Input/png/beach.png

# Import the libraries
import cv2
import argparse
import matplotlib.pyplot as plt

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
                required=True, help="Input image path")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args['input'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grayscale", gray)

# Calculate histogram for pixel intensities in the image
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Plot the image and histogram side by side using matplotlib
plt.figure()
plt.axis('off')
# Convert to RGB from grayscale because matplotlib expects image in RGB space
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB))

# Plot the histogram
plt.figure()
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.title("Grayscale histogram")
plt.plot(hist)

# We should normalize the histogram as the size of image can vary for 2 images
hist /= hist.sum()

plt.figure()
plt.title("Grascale histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("Frequency(Normalized)")
plt.plot(hist)
plt.show()
