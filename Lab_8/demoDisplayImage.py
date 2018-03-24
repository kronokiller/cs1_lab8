"""
Demonstrates displayImage function

Submitted by:
"""

import lab8Functions as lab8Fn
import scipy.misc
import numpy as np

# Desired size of the rectangular image
width = 400
height = 400

# Create a square image of a single color, initially black
amazingImage = lab8Fn.emptyImage(height, width)

# Change every pixel in this square to blue

for row in range(height):
    for col in range(width):
        amazingImage[row, col] =  lab8fn.bluePixel

# ... and display it
lab8Fn.displayImage(amazingImage)
