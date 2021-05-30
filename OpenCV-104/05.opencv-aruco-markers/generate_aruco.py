# Usage
# python generate_aruco.py -o ../../Data/Output/aruco_marker.png -i 24 -t DICT_4x4_50

# Import libraries
import cv2
import argparse
import sys
import numpy as np

# Add command-line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, required=True,
                help="path to store the output aruco markers")
ap.add_argument("-i", "--id", type=int, required=True,
                help="ID of the ArUco marker from the dictionary")
ap.add_argument("-t", "--type", type=str, default="DICT_ARUCO_ORIGINAL",
                help="Type of ArUco marker to generate")
args = vars(ap.parse_args())

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

# Get dictionary from opencv
type_ = args["type"]
try:
    aruco_dict = cv2.aruco.Dictionary_get(ARUCO_DICT[type_])
except:
    print(f"[WARN] ArUco marker of type={type_} isn't supported.")
    sys.exit(0)

# Generate aruco marker with specified id and type
print(f"[INFO] Generating ArUco marker with type={type_}, ID={args['id']}")
tag = np.zeros((300, 300, 1), dtype="uint8")
cv2.aruco.drawMarker(aruco_dict, args['id'], 300, tag, 1)

# Write marker into file
cv2.imwrite(args["output"], tag)
cv2.imshow("Output", tag)
cv2.waitKey(0)
