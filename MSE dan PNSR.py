# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:38:00 2024

@author: HP
"""
 
import cv2 
import numpy as np 
from math import log10, sqrt

def PSNR(original, compressed): 
	mse = np.mean((original - compressed) ** 2) 
	if(mse == 0): # MSE is zero means no noise is present in the signal . 
				# Therefore PSNR have no importance. 
		return 100
	max_pixel = 255.0
	psnr = 20 * log10(max_pixel / sqrt(mse)) 
	return psnr 

def main(): 
	original = cv2.imread("C:/Users/HP/Downloads/2c5c30a58c233c1a2c4e728106356700.png") 
	compressed = cv2.imread("C:/Users/HP/Downloads/2c5c30a58c233c1a2c4e728106356700.png", 1) 
	value = PSNR(original, compressed) 
	print(f"PSNR value is {value} dB") 
	
if __name__ == "__main__": 
	main()
    
"""
https://www.geeksforgeeks.org/python-peak-signal-to-noise-ratio-psnr/
"""

# PSNR paling umum digunakan untuk memperkirakan efisiensi kompresor, filter, dll. 
# Semakin besar nilai PSNR, semakin efisien metode kompresi atau filter yang sesuai.
# Jika MSE = 0, artinya tidak ada perbedaan antara gambar asli dan gambar kompresi (keduanya identik).