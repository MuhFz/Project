# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:20:24 2024

@author: HP
"""

# rotasi

import cv2

img = cv2.imread('C:/Users/HP/OneDrive/Documents/OneDrive/Pictures/preview.jpg')

row, cols, ghgh = img.shape
MRotasi = cv2.getRotationMatrix2D((cols/2, row/2), 90, 1)

print(MRotasi)

dstRotasi = cv2.warpAffine(img, MRotasi, (cols, row))

cv2.imshow("dstRotasi", dstRotasi)

cv2.waitKey(0)
cv2.destroyAllWindows()