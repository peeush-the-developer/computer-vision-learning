# Usage
# python detect_low_contrast_video.py -i ../../Data/Input/Low_Contrast/example_video.mp4

# Import libraries
import cv2
import argparse
import imutils
from numpy.core.fromnumeric import var
from skimage.exposure import is_low_contrast
import numpy as np

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, help="Input video file path")
ap.add_argument("-t", "--thresh", type=float, default=0.35,
                help="Low contrast threshold value")
args = vars(ap.parse_args())

video = cv2.VideoCapture(args["input"] if args["input"] else 0)

while True:
    grabbed, frame = video.read()

    if not grabbed:
        print("[INFO] No frame detected from video stream. Exiting...")
        break

    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)

    text = "Low contrast: No"
    color = (0, 255, 0)

    if is_low_contrast(frame, fraction_threshold=args["thresh"]):
        text = "Low contrast: Yes"
        color = (0, 0, 255)
    else:
        cnts = cv2.findContours(
            edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key=cv2.contourArea)

        cv2.drawContours(frame, [c], -1, color, 2)

    cv2.putText(frame, text, (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    output = np.dstack([edged]*3)
    output = np.hstack([frame, output])

    cv2.imshow("Output", output)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
