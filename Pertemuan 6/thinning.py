# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:01:52 2024

@author: HP
"""

import cv2

img= cv2.imread('C:/Users/HP/OneDrive/Documents/OneDrive/Pictures/wallpaperflare.com_wallpaper (3).jpg', 0)
thin = cv2.ximgproc.thinning(img)

cv2.imshow("Thin", thin)
cv2.waitKey(0)
cv2.destroyAllWindows()