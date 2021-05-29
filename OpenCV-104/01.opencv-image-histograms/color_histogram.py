# Usage
# python color_histogram.py -i ../../Data/Input/png/beach.png

# Import libraries
import cv2
import argparse
import matplotlib.pyplot as plt
import imutils

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
                required=True, help="Input image path")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args['input'])

# Plot the actual image, histogram
plt.figure()
plt.axis('off')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# Split channels into B,G,R
channels = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title('Image histogram normalized')
plt.xlabel("Bins")
plt.ylabel("Frequency (Normalized)")

for channel, color in zip(channels, colors):
    # Calculate histogram
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    hist /= hist.sum()

    plt.plot(hist, color=color)

# Plot 2D Histograms
fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([channels[1], channels[0]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title('2D Hist G and B channels')
plt.colorbar(p)


ax = fig.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]],
                    [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Hist G abd R channels")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([channel[0], channel[2]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Hist B and R channels")
plt.colorbar(p)

# finally, let's examine the dimensionality of one of the 2D
# histograms
print("2D histogram shape: {}, with {} values".format(
    hist.shape, hist.flatten().shape[0]))

# our 2D histogram could only take into account 2 out of the 3
# channels in the image so now let's build a 3D color histogram
# (utilizing all channels) with 8 bins in each direction -- we
# can't plot the 3D histogram, but the theory is exactly like
# that of a 2D histogram, so we'll just show the shape of the
# histogram
hist = cv2.calcHist([image], [0, 1, 2],
	None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
	hist.shape, hist.flatten().shape[0]))

# display the original input image
plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(image))

plt.show()
