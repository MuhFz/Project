# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:15:14 2024

@author: HP
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/HP/Downloads/colorful-pineapple-sketches-with-cut-pineapple-illustration-isolated-vector.jpg", 0)

_, gambarBiner = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY)

img_cp = img.copy()
kernel = np.ones((3, 3), np.uint8)
thick = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("thick", thick)

cv2.waitKey(0)
cv2.destroyAllWindows()