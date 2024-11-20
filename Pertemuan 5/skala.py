# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:14:33 2024

@author: HP
"""

# skala

import cv2


img = cv2.imread('C:/Users/HP/OneDrive/Documents/OneDrive/Pictures/preview.jpg')

dstSkala = cv2.resize(img, None, fx=2.5, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("title", img)
cv2.imshow("img", dstSkala)

cv2.waitKey(0)
cv2.destroyAllWindows()