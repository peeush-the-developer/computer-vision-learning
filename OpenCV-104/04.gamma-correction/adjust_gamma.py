# Usage
# python adjust_gamma.py -i ../../Data/Input/png/dog_shadow.png

# Import libraries
import cv2
import argparse
import numpy as np


def adjust_gamma(image, gamma=1.0):
    '''
    Function to adjust gamma
    Power Law transform: O = I ^ (1/G)

    Arguments:
        image: numpy ndarray rep for image
        gamma: Gamma value for adjustment, default=1.0

    Returns:
        Lookup table for each pixel value in the image.
    '''
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) *
                     255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)


# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
                required=True, help="Input image path")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])

# Loop over different gamma values to show impact on image
for gamma in np.arange(0.0, 3.5, 0.5):
    # Continue for gamma=1.0 as it will not impact the image
    if gamma == 1.0:
        continue

    # Adjust gamma value to avoid "divide by zero"
    gamma = gamma if gamma > 0.0 else 0.1
    output = adjust_gamma(image, gamma=gamma)
    cv2.putText(output, f"gamma={gamma}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

    cv2.imshow("Original vs Adjusted", np.hstack([image, output]))
    cv2.waitKey(0)
