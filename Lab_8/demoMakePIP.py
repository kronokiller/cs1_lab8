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
newImage = f.makePIP(myImage, billy, 0, 0)

# Upper right corner
newImage = f.makePIP(newImage,
                                 billy,
                                 0,
                                 len(newImage[0]) - len(billy[0]))

# Lower left corner
newImage = f.makePIP(newImage,
                                 billy,
                                 len(newImage) - len(billy),
                                 0)

# Lower right corner
newImage = f.makePIP(newImage,
                                 billy,
                                 len(newImage) - len(billy),
                                 len(newImage[0]) - len(billy[0])

f.displayImage(newImage)
