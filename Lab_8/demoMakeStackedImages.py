"""
Demonstrates the makeStackedImages function
"""

import lab8Functions
import cImage

# Read two files of photos
topImage = cImage.FileImage("flowers.png")
bottomImage = cImage.FileImage("tug.png")

# Create a stacked image with one photo above another, then display it
desiredImage = lab8Functions.makeStackedImages(topImage, bottomImage)
lab8Functions.displayImage(desiredImage)
