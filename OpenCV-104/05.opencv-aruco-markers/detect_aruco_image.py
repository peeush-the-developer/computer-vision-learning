# Usage
# python detect_aruco_image.py -i ../../Data/Input/png/ArUco_markers.png -t DICT_5X5_100

# Import libraries
import cv2
import argparse
import sys
import imutils

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True,
                help="Input image path containing aruco markers")
ap.add_argument("-t", "--type", type=str, default="DICT_5X5_100",
                help="ArUco dictionary to use to detect markers")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
image = imutils.resize(image, width=600)

# Define aruco dictionary
ARUCO_DICT = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
    "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
    "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
    "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
    "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
    "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
    "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
    "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
    "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
    "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
    "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
    "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
    "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
    "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
    "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
    "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
    "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
    "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
    "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
    "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
    "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

# Get the aruco dictionary
type_ = args["type"]
try:
    aruco_dict = cv2.aruco.Dictionary_get(ARUCO_DICT[type_])
except:
    print(f"[WARN] The ArUco marker of type={type_} is not supported.")
    sys.exit(0)

# Grab the aruco parameters and detect markers in the input image
aruco_params = cv2.aruco.DetectorParameters_create()
(corners, ids, rejected) = cv2.aruco.detectMarkers(
    image, aruco_dict, parameters=aruco_params)

green = (0, 255, 0)

# Detect if atleast one marker was detected
if len(corners) > 0:
    ids = ids.flatten()

    for (markerCorner, markerID) in zip(corners, ids):
        (top_left, top_right, bottom_right,
         bottom_left) = markerCorner.reshape((4, 2))

        top_left = (int(top_left[0]), int(top_left[1]))
        top_right = (int(top_right[0]), int(top_right[1]))
        bottom_left = (int(bottom_left[0]), int(bottom_left[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

        # Draw bouding box over the detected marker
        cv2.line(image, top_left, top_right, green, 2)
        cv2.line(image, top_right, bottom_right, green, 2)
        cv2.line(image, bottom_right, bottom_left, green, 2)
        cv2.line(image, bottom_left, top_left, green, 2)

        # Find the center in the marker
        cX = int((top_left[0] + bottom_right[0]) / 2.0)
        cY = int((top_left[1] + bottom_right[1]) / 2.0)
        cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)

        # Add text for marker id
        cv2.putText(image, str(
            markerID), (top_left[0], top_left[1]-15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

        cv2.imshow("Image", image)
        cv2.waitKey(0)
