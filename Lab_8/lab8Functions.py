"""
MAT 2170
Support functions for Lab 8

Submitted by:
"""

import numpy as np
import scipy.misc as misc
import matplotlib.pyplot as plt

# Some common colors
redPixel = [255, 0, 0]
greenPixel = [0, 255, 0]
bluePixel = [0, 0, 255]
magentaPixel = [255, 0, 255]
yellowPixel = [255, 255, 0]
cyanPixel = [0, 255, 255]
whitePixel = [255, 255, 255]
blackPixel = [0, 0, 0]


def emptyImage(height, width):
    """
    Creates an array of black pixels in the specified size

    Args:
        height: number of rows
        width: number of columns
    Return:
        ndarray of the specified size containing all zeros
    """
    im = np.zeros((height, width, 4), dtype='uint8')
    im[:, :, 3] = 255
    
    return im

def displayImage(image):
    """
    Display an image in a matplotlib window

    Arguments:
        image: a 2-dimensional array of pixels

    Returns:
        None
    """
    # Display the image in a matplotlib window
    plt.imshow(image)
    # Wait for a mouse click to close the window
    plt.show()

def makeDiagonal(size, desiredPixel):
    """
    Create an image with dimensions (size x size) of a given pixel in the
    shape of a diagonal line from the northwest to southeast corners.

    Arguments:
        size: width and height, in pixels, of image to be generated
        desiredPixel: color of diagonal line (background will be black)

    Returns:
        a square image with the specified properties
    """
    # Begin with a square image with all black pixels
    resultImage = emptyImage(size, size)

    # Set pixels along the diagonal
    for i in range(size):
        resultImage[i, i, 0:3] = desiredPixel

    return resultImage


def makeLowerTriangle(size, desiredPixel):
    """
    Create an image with dimensions (size x size) of a given pixel in the
    shape of a lower triangle

    Arguments:
        size: width and height, in pixels, of image to be generated
        desiredPixel: desired color of pixels in the lower triangle
                      (remaining pixels are black)

    Returns:
        a square image with the specified properties
    """

    resultImage = emptyImage(size, size)
    for i in range(size):
        resultImage[i:,i, 0:3] = desiredPixel

    return resultImage


def makeBandedDiagonal(size, bandWidth, desiredPixel):
    """
    Create a banded diagonal image of (size x size) overall size, using the
    given pixel to highlight this band

    Arguments:
        size: width and height, in pixels, of image to be generated
        bandWidth: number of super-diagonals (and sub-diagonals) to appear
        desiredPixel: desired color of band

    Returns:
        a square image with the specified properties
    """

    resultImage = emptyImage(size, size)
    for i in range(size):
        leftSide = i - bandWidth
        if leftSide < 0:
            leftSide = 0

        rightSide = i + bandWidth + 1
        if rightSide > size:
            rightSide = size

        resultImage[i, leftSide:rightSide, 0:3] = desiredPixel

    return resultImage


def displayImageFile(fileName):
    """
    Displays an image file in an appropriately sized window

    Arguments:
        fileName: the name of a file holding a graphics image
        (*.png, etc.)

    Returns:
        None
    """
    # Get the image file
    theImage = misc.imread(fileName)

    # Display it
    displayImage(theImage)


def makePIP(largeImage, smallImage, upperLeftRow, upperLeftCol):
    """
    Create an image of a "picture-in-picture"

    Arguments:
        largeImage: a graphics image
        smallImage: a smaller image to be placed within the larger image
        upperLeftRow: how far down to place the smaller image
        upperLeftCol: how far over to place the smaller image

    Returns:
        The image with the small image placed within the large image. The upper
        left corner of this small image appears at the given row and column.
    """

    if len(largeImage[0, 0]) == 3:
        largeImage[:, :].append(255)
        
    if len(smallImage[0, 0]) == 3:
        smallImage[:, :].append(255)

    # Make a copy of the large image
    resultImage = largeImage

    # Place the smaller image within the larger one
    for r in range(upperLeftRow:upperLeftRow + len(smallImage))
        for c in range(upperLeftCol:upperLeftCol + len(smallImage[0]))
            (rSmall, cSmall) = (r - upperLeftRow, c - upperLeftColumn)
            
            (RLarge, GLarge, BLarge, ALarge) = (largeImage[r, c, 0], largeImage[r, c, 1], largeImage[r, c, 2], largeImage[r, c, 3])
            (RSmall, GSmall, BSmall, ASmall) = (smallImage[rSmall, cSmall, 0], smallImage[rSmall, cSmall, 1], smallImage[rSmall, cSmall, 2], smallImage[rSmall, cSmall, 3])
            
            RNew = int(RSmall * ASmall / 255 + RLarge * ALarge / 255 * (255 - ASmall) / 255)
            GNew = int(GSmall * ASmall / 255 + GLarge * ALarge / 255 * (255 - ASmall) / 255)
            BNew = int(BSmall * ASmall / 255 + BLarge * ALarge / 255 * (255 - ASmall) / 255)
            ANew = int(ASmall + ALarge * (255 - ASmall) / 255

            resultImage[r, c] = [RNew, GNew, BNew, ANew]
            
    return resultImage


def displayFramedImage(image, frameSize, frameColor):
    """
    Display an image with a border of a specified color

    Arguments:
        image: a graphics image
        frameSize: desired size, in pixels, of the outer frame
        frameColor: desired color of frame

    Returns:
        None
    """                       
    resultImage = emptyImage(len(image) + 2 * frameSize, len(image[0] + 2 * framSize))
    resultImage(:, :, 0:3) = frameColor
    resultImage = makePIP(resultImage, image, frameSize, frameSize)
    
    displayImage(resultImage)
 

def makeStackedImages(topImage, bottomImage):
    """
    Given two images, produce a stacked version, one atop another

    Arguments:
        topImage: a graphics image
        bottomImage: a second graphics image

    Returns:
        The graphics image formed by stacking the two images
    """
    resultImage = emptyImage(len(topImage) + len(bottomeImage), max(len(bottomImage), len(bottomImage)))
    resultImage = makePIP(makePIP(resultImage, topImage, 0, 0), bottomImage, len(topImage), 0)
    
    return resultImage


def pixelMapper(image, rgbFunction):
    """
    Apply a pixel-based function to every pixel of an image

    Arguments:
        image: an image to process
        rgbFunction: a function which can be applied to one pixel

    Returns:
        The image, with the supplied function applied to each pixel
    """

    # Create an image of the same size as the input image
    height = len(image)
    width = len(image[0])

    resultImage = emptyImage(height, width)

    # Apply the given pixel function to each of the pixels in the image
    for row in range(height):
        for col in range(width):
            resultImage[row, col, 0:3] = \
                rgbFunction(image[row,col, 0:3])

    return resultImage


def grayPixel(pixel):
    """
    Convert a given pixel to its gray scale equivalent value

    Arguments:
        pixel: one pixel

    Returns:
        The gray scale equivalent pixel
    """

    avg = sum(Pixel)//3
    return [avg for i in range(3)]


def flip(value):
    """
    Color reverse an RGB value

    Arguments:
        value: a color intensity

    Returns:
        The color-reversed intensity
    """
    return 255 - value


def negativePixel(oldPixel):
    """
    Invert a single pixel

    Arguments:
        oldPixel: one pixel of a graphics image

    Returns:
        The photographic negative of this pixel
    """
    return [flip(v) for v in oldPixel]


def sepiaPixel(oldPixel):
    """
    Convert a given pixel to its sepia equivalent value

    Arguments:
        oldPixel: one pixel of a graphics image

    Returns:
        The sepia tone version of the given pixel

    """
        
                       
                       
    return [, , ]

def makeRectangle(h, w, c):
    """
    Creates a rectangular image of specified dimensions and color

    Arguments:
        h: The height of the rectangle
        w: The width of the rectangle
        c: The color of the rectangle

    Returns:
        An array containing the image data
    """

    resultImage = emptyImage(h, w)
    resultImage[:, :, 0:3] = c

    return resultImage

if __name__=="__main__":
    p = misc.imread("flowers.png")
    print(p.shape)
    print(p[100,100])
    q = pixelMapper(p,negativePixel)
    displayImage(q)
