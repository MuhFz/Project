# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:05:28 2024

@author: HP
"""

import cv2
import numpy as np

imgC = cv2.imread('C:/Users/HP/Downloads/1ljmqxinvgkb25e.jpg', 0)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(imgC, cv2.MORPH_CLOSE, kernel)


cv2.imshow("closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
