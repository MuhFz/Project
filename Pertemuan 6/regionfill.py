# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:27:03 2024

@author: HP
"""

import cv2
img = cv2.imread("C:/Users/HP/Downloads/agito_logo_by_j_rider1995_di7zwgl.png", 0)

garis = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
garis = garis[0] if len(garis) == 2 else garis[1]

for g in garis:
    cv2.drawContours(img,[g], 0, (255,255,255), -1)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20,20))
regionFill = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)

cv2.imshow('gray', img)
cv2.imshow('region fill', regionFill)
cv2.waitKey(0)