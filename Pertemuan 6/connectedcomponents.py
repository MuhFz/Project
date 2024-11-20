# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:47:56 2024

@author: HP
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/HP/Downloads/agito_logo_by_j_rider1995_di7zwgl.png", 0)
img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
numberLabel, Labelobjek = cv2.connectedComponents(img)

hueLabel = np.uint8(179*Labelobjek/np.max(Labelobjek))
emptyChannel = 255*np.ones_like(hueLabel)
Hasilimg = cv2.merge([hueLabel, emptyChannel, emptyChannel])
Hasilimg = cv2.cvtColor(Hasilimg, cv2.COLOR_HSV2BGR)
Hasilimg[hueLabel==0] = 0

cv2.imshow("connectedComponents", Hasilimg)

cv2.waitKey(0)
cv2.destroyAllWindows()