"""
Demonstrates "picture-in-picture"
"""

import lab8Functions as f
import scipy.misc as misc

myImage = misc.imread("eiu.png")
billy = misc.imread("billy.png")

# for r in range(len(billy)):
#     for c in range(len(billy[0])):
#         for i in range(3):
#             billy[r, c, i] = int(billy[r, c, i] * (billy[r, c, 3] / 255) + 255 * (1 - billy[r, c, 3] / 255))
# 
# billy = billy[:, :, 0:3]
#
# misc.imsave('billy.png', billy)


# Upper left corner
newImage = lab8Functions.makePIP(myImage, billy, 0, 0)

# Upper right corner
newImage = lab8Functions.makePIP(newImage,
                                 billy,
                                 0,
                                 newImage.getWidth() - billy.getWidth())

# Lower left corner
newImage = lab8Functions.makePIP(newImage,
                                 billy,
                                 newImage.getHeight() - billy.getHeight(),
                                 0)

# Lower right corner
newImage = lab8Functions.makePIP(newImage,
                                 billy,
                                 newImage.getHeight() - billy.getHeight(),
                                 newImage.getWidth() - billy.getWidth())

lab8Functions.displayImage(newImage)
