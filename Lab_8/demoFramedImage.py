"""
Demonstrates the displayFramedImage function
"""

import lab8Functions
import cImage

# Frame a photo with a narrow yellow frame
myImage = cImage.FileImage("flowers.png")
lab8Functions.displayFramedImage(myImage, 20, lab8Functions.yellowPixel)

# Frame some artwork with a magenta frame
tugImage = cImage.FileImage("tug.png")
lab8Functions.displayFramedImage(tugImage, 50, lab8Functions.magentaPixel)
