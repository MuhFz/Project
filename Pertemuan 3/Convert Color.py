# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img0 = cv2.imread("C:/Users/HP/OneDrive/Documents/OneDrive/Pictures/Saved Pictures/wp10262640.jpg")
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# print (img0 . shape)
# print (img0 , img0 )
# lowBlue = np.array([30, 10, 10])
# highBlue = np.array([40, 255, 255])
# mask = cv2.inRange (img, lowBlue, highBlue)

# cv2.imshow("img0", img0)
# print(img.shape)

cv2.imshow("gray", gray)
print('gray =' , gray)

cv2.waitKey(0)
cv2.destroyAllWindows()