# Usage
# python basic_connected_components.py -i ../../Data/Input/png/license_plate.png

# Import libraries
import cv2
import argparse

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="Input image")
ap.add_argument("-c", "--connectivity", type=int,
                default=4, help="Connectivity argument")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["input"])
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply Otsu's thresholding
_, thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

cv2.imshow("Original", image)
cv2.imshow("Threshold", thresh)

# Apply Connected component analysis on binary threshold image
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
    thresh, args["connectivity"], cv2.CV_32S)

for i in range(num_labels):
    # i=0 gives background component
    if i == 0:
        text = f"Examining {i+1}/{num_labels} (background)"
    else:
        text = f"Examining {i+1}/{num_labels}"
    print(text)

    # Get boundary stats for the component
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]
    (cX, cY) = centroids[i]

    # Draw boundary around the connected component and place centroid
    output = image.copy()
    cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.circle(output, (int(cX), int(cY)), 3, (0, 0, 255), -1)

    # Create mask to plot over component
    component = (labels == i).astype("uint8") * 255

    cv2.imshow("Output", output)
    cv2.imshow("Connected Component", component)

    cv2.waitKey(0)

cv2.destroyAllWindows()
