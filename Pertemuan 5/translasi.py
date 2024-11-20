# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:19:50 2024

@author: HP
"""

# translasi

import cv2
import numpy as np

img = cv2.imread('C:/Users/HP/OneDrive/Documents/OneDrive/Pictures/preview.jpg')

print(img.shape)

row, cols, ghgh = img.shape

MTranslasi = np.float32([
     [2, 0, 100],
     [0, 2, 50]           
    ])

print(MTranslasi, '\n')


dst = cv2.warpAffine(img, MTranslasi, (cols, row))

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
