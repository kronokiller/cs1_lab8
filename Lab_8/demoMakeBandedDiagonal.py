"""
Demonstrates makeBandedDiagonal function

Submitted by:
"""

import lab8Functions

# Create an image and display it
amazingImage = lab8Functions.makeBandedDiagonal(400, 1, lab8Functions.redPixel)
lab8Functions.displayImage(amazingImage)

# Now a second image
amazingImage = lab8Functions.makeBandedDiagonal(400, 3, lab8Functions.greenPixel)
lab8Functions.displayImage(amazingImage)

# And a third
amazingImage = lab8Functions.makeBandedDiagonal(400, 100, lab8Functions.bluePixel)
lab8Functions.displayImage(amazingImage)
