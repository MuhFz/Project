# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:07:05 2024

@author: HP
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/HP/Downloads/colorful-pineapple-sketches-with-cut-pineapple illustration-isolated-vector.jpg", 0)

_, imgBiner = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

img_cp = img.copy()
kernel = np.ones((3, 3), np.uint8)
thickening = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("thickening", thickening)

cv2.waitKey(0)
cv2.destroyAllWindows()
