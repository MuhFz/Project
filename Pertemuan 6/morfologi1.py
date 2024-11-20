# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 08:50:05 2024

@author: HP
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/HP/Downloads/colorful-pineapple-sketches-with-cut-pineapple-illustration-isolated-vector.jpg', 0)
imgO = cv2.imread('C:/Users/HP/Downloads/istockphoto-184276818-612x612.jpg', 0)
imgC = cv2.imread('C:/Users/HP/Downloads/1ljmqxinvgkb25e.jpg', 0)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(imgO, cv2.MORPH_OPEN, kernel)
opening = cv2.resize(opening,(300,300))
closing = cv2.morphologyEx(imgC, cv2.MORPH_CLOSE, kernel)
closing = cv2.resize(closing,(300,300))

titles = ['Normal Image', 'Erosion',
          'Dilation', 'Before Opening', 
          'Opening', 'Before Closing', 'Closing']

images = [img, erosion, dilation, imgO, opening, imgC, closing]

cv2.imshow("img", img)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("imgO", imgO)
cv2.imshow("opening", opening)
cv2.imshow("imgC", imgC)
cv2.imshow("closing", closing)

for i in range(7):
    plt.subplot(2,5,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()