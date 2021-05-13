# Usage
# python convolutions.py -i ../../Data/Input/3d_pokemon.png

# Load the libraries
import argparse
import cv2
import numpy as np
from skimage.exposure import rescale_intensity

# Define a convolve function to implement convolution from scratch


def convolve(image, kernel):
    '''
    This function implements convolution operation of kernel over image.

    Arguments:
        image: A gray-scale image (Convolution can work on RGB image, but for simplicity, we take gray scale image)
        kernel: A 2D NxN matrix that is defined by driver code. Kernel can be to blur, sharpen, edge detection, etc.

    Returns:
        Output image after convolution operation on input image
    '''

    # Find image height(iH), image width(iW)
    (iH, iW) = image.shape[:2]
    # Find kernel height(kH), kernel width(kW)
    (kH, kW) = kernel.shape[:2]

    # Pad the input image to keep output image size same as input image after convolution operation
    # We are using BORDER_REPLICATE because we need to see output image as well. Usually, in CNN, it is zero padded.
    pad = (kW - 1)//2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    cv2.imshow("Padded image", image)
    # Allocate memory to output image
    output = np.zeros((iH, iW), dtype="float32")

    # Move our kernel from left to right, top to bottom and apply convolution
    for y in np.arange(pad, iH+pad):
        for x in np.arange(pad, iW+pad):
            # Extract the ROI from the padded input image
            roi = image[y-pad:y+pad+1, x-pad:x+pad+1]

            # Apply convolution
            val = (roi * kernel).sum()

            # Store the convolution value into output image
            output[y-pad, x-pad] = val

    # Rescale the output to range[0, 255]
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")

    return output


def get_kernel(kernel_name):
    '''
    Returns actual kernel matrix based on given kernel_name

    Arguments:
        kernel_name: string like 'small_blur', 'large_blue', etc.

    Returns:
        A 2D matrix that defines kernel
    '''
    kernels = {
        'small_blur': np.ones((7, 7), dtype="float") * (1.0 / (7 * 7)),
        'large_blur': np.ones((21, 21), dtype="float") * (1.0 / (21 * 21)),
    }

    if kernel_name in kernels:
        return kernels[kernel_name]
    else:
        raise(f"{kernel_name} not implemented yet")


# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', type=str, required=True, help="Input image")
ap.add_argument('-k', '--kernel', type=str,
                choices=['small_blur', 'large_blur'], default='small_blur', help='Kernel type')
args = vars(ap.parse_args())

# Load and display original image
image = cv2.imread(args['input'])
# Convert image to grayscale for the sake of this tutorial
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', gray)

# Define kernel
kernel_name = args['kernel']
kernel = get_kernel(kernel_name)

# Call convolve function
outputConvolve = convolve(gray, kernel)
opencvConvolve = cv2.filter2D(gray, -1, kernel)

cv2.imshow(f"OurConvolve:{kernel_name}", outputConvolve)
cv2.imshow(f"OCVConvolve:{kernel_name}", opencvConvolve)

cv2.waitKey(0)
cv2.destroyAllWindows()
