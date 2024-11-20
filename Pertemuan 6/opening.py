# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:05:09 2024

@author: HP
"""

import cv2
import numpy as np

imgO = cv2.imread('C:/Users/HP/Downloads/istockphoto-184276818-612x612.jpg', 0)
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(imgO, cv2.MORPH_OPEN, kernel)

cv2.imshow("opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
