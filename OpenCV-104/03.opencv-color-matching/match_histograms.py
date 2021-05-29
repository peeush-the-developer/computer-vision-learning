# Usage
# python match_histograms.py -s ../../Data/Input/png/empire_state_cloudy.png -r ../../Data/Input/png/empire_state_sunset.png

# Import libraries
from skimage import exposure
import cv2
import argparse
import matplotlib.pyplot as plt

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", type=str, required=True,
                help="Source image path to which color matching applied")
ap.add_argument("-r", "--reference", type=str, required=True,
                help="Reference image path which has to be applied on source image")
args = vars(ap.parse_args())

# Load the image
src = cv2.imread(args["source"])
ref = cv2.imread(args["reference"])

# Match histogram from ref image to src image
multi = True if src.shape[-1] > 1 else False
matched = exposure.match_histograms(src, ref, multichannel=multi)

cv2.imshow("Source", src)
cv2.imshow("Reference", ref)
cv2.imshow("Matched", matched)

cv2.waitKey(0)

(fig, axs) = plt.subplots(nrows=3, ncols=3,
                          sharex=True, sharey=True, figsize=(8, 8))

# Enumerate over 3 images (src, reference, matched)
for (i, image) in enumerate([src, ref, matched]):
    # Convert the color space from BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Enumerate over color channels in the image
    for (j, channel) in enumerate(["red", "green", "blue"]):
        # Compute the histogram for the channel in the image and plot it
        (hist, bins) = exposure.histogram(image[..., j], source_range="dtype")
        axs[j, i].plot(bins, hist / hist.max())

        # Compute the cumulative distribution function of the channel and plot it
        (cdf, bins) = exposure.cumulative_distribution(image[..., j])
        axs[j, i].plot(bins, cdf)

        axs[j, 0].set_ylabel(channel)

axs[0, 0].set_title('Source')
axs[0, 1].set_title('Reference')
axs[0, 2].set_title('Matched')

plt.tight_layout()
plt.show()
