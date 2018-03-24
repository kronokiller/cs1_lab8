"""
Demonstrates the pixelMapper function
"""

import lab8Functions as lab8Fn
import scipy.misc as misc

# Read an image to be transformed
oldImage = misc.imread("flowers.png")

# Transform the image
newImage = lab8Fn.pixelMapper(oldImage, lab8Fn.grayPixel)

lab8Fn.displayImage(lab8Fn.makeStackedImages(oldImage, newImage))
