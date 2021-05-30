# Usage
# python color_correction.py -r ../../Data/Input/Color_Correction/reference.jpg -i ../../Data/Input/Color_Correction/examples/01.jpg

# Import libraries
from imutils.perspective import four_point_transform
import imutils
import cv2
import argparse
import numpy as np
from skimage import exposure
import sys

# Define function to find color card


def find_color_card(image):
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
    aruco_params = cv2.aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(
        image, aruco_dict, parameters=aruco_params)

    # for markerCorner, markerID in zip(corners, ids):
    #     print(markerID, markerCorner)

    # print(type(corners))
    # print(ids.shape)
    try:
        ids = ids.flatten()

        # Extract top_left corner
        id_ = np.squeeze(np.where(ids == 923))
        top_left = np.squeeze(corners[id_])[0]

        # Extract top_right corner
        id_ = np.squeeze(np.where(ids == 1001))
        top_right = np.squeeze(corners[id_])[1]

        # Extract bottom_right corner
        id_ = np.squeeze(np.where(ids == 241))
        bottom_right = np.squeeze(corners[id_])[2]

        # Extract bottom_left corner
        id_ = np.squeeze(np.where(ids == 1007))
        bottom_left = np.squeeze(corners[id_])[3]

        # Get the birds-eye view using corner co-ordinates
        card_coordinates = np.array(
            [top_left, top_right, bottom_right, bottom_left])
        card = four_point_transform(image, card_coordinates)
        return card
    except:
        return None


# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--reference", type=str, required=True,
                help="Reference card image path")
ap.add_argument("-i", "--input", type=str,
                required=True, help="Input image path")
args = vars(ap.parse_args())

# Load the images
image = cv2.imread(args["input"])
ref = cv2.imread(args["reference"])

image = imutils.resize(image, width=600)
ref = imutils.resize(ref, width=600)

cv2.imshow("Original image", image)
cv2.imshow("Reference image", ref)
# cv2.waitKey(0)

# Find color cards birds-eye view for image and reference card
ref_card = find_color_card(ref)
image_card = find_color_card(image)

if ref_card is None or image_card is None:
    print("[WARN] Image or Reference cards weren't found")
    sys.exit(0)

# Match histograms using skimage.exposure.match_histograms from reference card onto image card
matched = exposure.match_histograms(image_card, ref_card, multichannel=True)

cv2.imshow("Image card", image_card)
cv2.imshow("Reference card", ref_card)
cv2.imshow("Result", matched)

cv2.waitKey(0)
cv2.destroyAllWindows()
