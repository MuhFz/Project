# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Konversi Warna ke Abu-abu
import cv2
import numpy as np

img = cv2.imread("C:/Users/HP/OneDrive/Documents/OneDrive/Pictures/preview.jpg")
cv2.imshow("Original", img)

row, col = img.shape[0:2]

for i in range(row) :
    for j in range(col) :
        # find the average of the BGR pixel values
        img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()