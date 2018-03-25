"""
Demonstrates the displayFramedImage function
"""

import lab8Functions
import scipy.misc as misc

# Frame a photo with a narrow yellow frame
myImage = misc.imread("flowers.png")
lab8Functions.displayFramedImage(myImage, 20, lab8Functions.yellowPixel)

# Frame some artwork with a magenta frame
tugImage = misc.imread("tug.png")
lab8Functions.displayFramedImage(tugImage, 50, lab8Functions.magentaPixel)
