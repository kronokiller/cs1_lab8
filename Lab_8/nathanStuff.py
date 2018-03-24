"""
CSM 2170 -- Spring 2018
Assignment:
Submitted by: Nathan Bartholomew
"""

import numpy as np
import matplotlib.pyplot as plt
import random

# size = 10
#
# h = size
# w = size

# h = 200
# w = 100
#
# resultImage = np.zeros((h,w,3), dtype = 'uint8')

# for i in range(size):
#     resultImage[i:, i] = [255, 255, 255]

# resultImage[:,:] = [255, 255, 255]

largeImage = np.zeros((random.randint(500, 750), random.randint(750, 1000), 3), dtype = 'uint8')

smallImage = np.zeros((random.randint(200, 400), random.randint(300, 600), 3), dtype = 'uint8')
smallImage[:,:] = [255, 255, 255]

# resultImage = np.zeros((len(largeImage), len(largeImage[0]), 3), dtype = 'uint8')
# resultImage[:,:] = largeImage

resultImage = largeImage

upperLeftRow = random.randint(0, len(largeImage) - len(smallImage))
upperLeftCol = random.randint(0, len(largeImage[0]) - len(smallImage[0]))

resultImage[upperLeftRow:upperLeftRow + len(smallImage) , upperLeftCol:upperLeftCol + len(smallImage[0])] = smallImage

# plt.imshow(largeImage)
# plt.show()

plt.imshow(resultImage)
plt.show()


# for r in range(len(billy)):
#     for c in range(len(billy[0])):
#         for i in range(3):
#             billy[r, c, i] = int(billy[r, c, i] * (billy[r, c, 3] / 255) + 255 * (1 - billy[r, c, 3] / 255))
#
# billy = billy[:, :, 0:3]