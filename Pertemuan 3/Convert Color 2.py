# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Konversi Warna ke Abu-abu
import cv2
import numpy as np

img = cv2.imread("C:/Users/HP/OneDrive/Documents/OneDrive/Pictures/preview.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, BW) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

print ("Original = ", img.shape)
print ("Gray = ", gray.shape)
print("BW = ", BW.shape)
print (BW)
cv2.imwrite("C:/Users/HP/OneDrive/Documents/OneDrive/Pictures/preview.jpg", BW)

cv2.waitKey(0)
cv2.destroyAllWindows()