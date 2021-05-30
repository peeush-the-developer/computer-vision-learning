# Usage
# python detect_low_contrast_image.py -i ../../Data/Input/Low_Contrast/examples

# Import libraries
import cv2
import argparse
import imutils
from skimage import exposure
from imutils.paths import list_images
from skimage.exposure.exposure import is_low_contrast

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
                required=True, help="Input images directory path")
ap.add_argument("-t", "--threshold", type=float, default=0.35,
                help="Threshold for low contrast image")
args = vars(ap.parse_args())

imagePaths = sorted(list(list_images(args["input"])))

for i, image_path in enumerate(imagePaths):
    # Load the image
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=450)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), sigmaX=0)
    edged = cv2.Canny(blurred, 30, 150)

    text = "Low contrast: No"
    color = (0, 255, 0)

    if is_low_contrast(image, args["threshold"]):
        text = "Low contrast: Yes"
        color = (0, 0, 255)
    else:
        cnts = cv2.findContours(
            edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key=cv2.contourArea)

        cv2.drawContours(image, [c], -1, color, 2)

    cv2.putText(image, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)

    cv2.imshow("Image", image)
    cv2.imshow("Edged", edged)
    cv2.waitKey(0)
