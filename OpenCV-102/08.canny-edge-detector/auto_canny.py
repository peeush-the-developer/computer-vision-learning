# Usage
# python auto_canny.py -i ../Data/Input/jpg

# Import libraries
import cv2
import argparse
import numpy as np
from glob import glob


# Auto canny function to provide edge map without manual lower and upper thresholds
def auto_canny(image, sigma=0.33):
    '''
    Canny edge detector with automatic thresholding values (T_lower, T_upper).

    Arguments:
        image: grayscale, blurred image array
        sigma: Tunable hyperparameter (default value: 0.33)

    Returns:
        edged: edge map from Canny algorithm
        t_lower: lower threshold value detected
        t_upper: upper threshold value detected
    '''
    # Get the median pixel value from the image
    med = np.median(image)

    # Calculate lower and upper threshold values
    lower = int(max(0, (1.00 - sigma) * med))
    upper = int(min(255, (1.00 + sigma) * med))
    # Apply canny algorithm on image with upper and lower values
    edged = cv2.Canny(image, lower, upper)

    return edged, lower, upper


# Add commond-line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
                help="Path to folder of images")
ap.add_argument("-t", "--type", type=str, default='jpg',
                help="jpg or png files in image folder")
args = vars(ap.parse_args())

# Detect edges for each image
for imagePath in glob(args["images"] + "/*." + args["type"]):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply wide, tight, auto canny functions
    wide = cv2.Canny(image, 10, 200)
    tight = cv2.Canny(image, 225, 250)
    auto, lower, upper = auto_canny(image)
    print(f'{imagePath}: {lower},{upper}')

    cv2.imshow("Grayscale, blurred", blurred)
    cv2.imshow("Result Stack", np.hstack([wide, tight, auto]))

    cv2.waitKey(0)
