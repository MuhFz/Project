# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:39:21 2024

@author: HP
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    # Baca gambar
    
    # Konversi ke Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Konversi ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Konversi ke Black and White (BW)
    (thresh, BW) = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    
    # Tampilkan gambar
    cv2.imshow("Original", frame)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Black and White", BW)
    
    print("thresh", thresh)    
    print("BW", BW)
    
    # Tunggu hingga pengguna menekan tombol
    if cv2.waitKey(1) == ord('q'):
        break

# Tutup semua jendela
cap.release()

cv2.destroyAllWindows()