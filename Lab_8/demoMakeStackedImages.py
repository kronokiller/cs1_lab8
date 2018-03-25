"""
Demonstrates the makeStackedImages function
"""

import lab8Functions
import scipy.misc as misc

# Read two files of photos
topImage = misc.imread("flowers.png")
bottomImage = misc.imread("tug.png")

# Create a stacked image with one photo above another, then display it
desiredImage = lab8Functions.makeStackedImages(topImage, bottomImage)
lab8Functions.displayImage(desiredImage)
