# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:04:13 2024

@author: HP
"""

import cv2
import numpy as np

img = cv2.imread('C:/Users/HP/Downloads/colorful-pineapple-sketches-with-cut pineapple-illustration-isolated-vector.jpg', 0)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow("dilation", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
