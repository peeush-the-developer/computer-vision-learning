# Usage
# python blog_example.py

# Import libraries
import cv2
import argparse

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, help="Input image",
                default='../../Data/Input/marvel_logo.jpg')
ap.add_argument("-c", "--convert", type=bool, default=True,
                help="We need white foreground on black background. True if you have otherwise.")
args = vars(ap.parse_args())

# Load the image
image_orig = cv2.imread(args["input"])
image = image_orig.copy()
if args["convert"]:
    image = cv2.bitwise_not(image)
# Convert to grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Show original and grayscale images
cv2.imshow(
    f"Original: ({image_orig.shape[0]},{image_orig.shape[1]})", image_orig)  # 340 x 255
cv2.imshow("Inverted", image)
cv2.imshow("Grayscale", gray)

# Perform erosion operations on the binary image
for i in range(1, 6):
    eroded = cv2.erode(gray.copy(), None, iterations=i)
    cv2.imshow(f'Eroded: {i} times', eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Grayscale", gray)

# Perform Dilation, though it will not help in our Marvel example as it is already connected.
for i in range(1, 6):
    dilated = cv2.dilate(gray.copy(), None, iterations=i)
    cv2.imshow(f"Dilated: {i} times", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Grayscale", gray)

# Perform Opening: Erosion followed by Dilation. This doesn't see much different because we don't have noise in the image.
# But we can see that Trademark symbol has been reduced gradually
# (3, 3) => We can see some grayish mark
# (5, 5) => We can see almost invisible mark
# (7, 7) => Removes it completely.
kernel_sizes = [(3, 3), (5, 5), (7, 7)]
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    opened = cv2.morphologyEx(gray.copy(), cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Opened w/ ({kernel_size[0]},{kernel_size[1]})", opened)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Grayscale", gray)

# Perform Closing: Dilation followed by Erosion. This doesn't help much in disconnecting characters from each other.
# And this is expected, because as we saw earlier that Dilation only make it worse.
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    closed = cv2.morphologyEx(gray.copy(), cv2.MORPH_CLOSE, kernel)
    cv2.imshow(f"Closed w/ ({kernel_size[0]},{kernel_size[1]})", closed)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Grayscale", gray)

# Perform Morpholigical_gradient: Difference between Dilation and Erosion
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    grad = cv2.morphologyEx(gray.copy(), cv2.MORPH_GRADIENT, kernel)
    cv2.imshow(f"Gradient w/ ({kernel_size[0]},{kernel_size[1]})", grad)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Grayscale", gray)

# Perform TopHat: Difference between grayscale image and opening. This will give bright foreground over dark background
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (260, 100))
top_hat = cv2.morphologyEx(gray.copy(), cv2.MORPH_TOPHAT, kernel)
cv2.imshow("TopHat (inverted)", top_hat)

top_hat_orig = cv2.morphologyEx(cv2.cvtColor(
    image_orig.copy(), cv2.COLOR_BGR2GRAY), cv2.MORPH_TOPHAT, kernel)
cv2.imshow("TopHat (original)", top_hat_orig)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Grayscale", gray)

# Perform BlackHat: Difference between grayscale image and closing. This will give dark foreground over light background
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (260, 100))
black_hat = cv2.morphologyEx(gray.copy(), cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat (inverted)", black_hat)

black_hat_orig = cv2.morphologyEx(cv2.cvtColor(
    image_orig.copy(), cv2.COLOR_BGR2GRAY), cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat (original)", black_hat_orig)

cv2.waitKey(0)
cv2.destroyAllWindows()
