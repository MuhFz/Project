# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 08:38:00 2024

@author: HP
"""

import cv2
import numpy as np

def normalized_correlation(img1, img2):
  """
  Fungsi untuk menghitung Normalized Correlation (NC) antara dua citra.

  Args:
    img1: Citra pertama.
    img2: Citra kedua.

  Returns:
    Nilai Normalized Correlation.
  """

  # Ubah citra menjadi grayscale
  gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  # Hitung mean dan standar deviasi masing-masing citra
  mean1 = np.mean(gray1)
  mean2 = np.mean(gray2)
  std1 = np.std(gray1)
  std2 = np.std(gray2)

  # Hitung numerator dan denominator dari rumus NC
  numerator = np.sum((gray1 - mean1) * (gray2 - mean2))
  denominator = std1 * std2 * (gray1.shape[0] * gray1.shape[1])

  # Hitung nilai NC
  nc = numerator / denominator

  return nc

# Contoh penggunaan
img1 = cv2.imread('C:/Users/HP/Downloads/2c5c30a58c233c1a2c4e728106356700.png')
img2 = cv2.imread('C:/Users/HP/Downloads/2c5c30a58c233c1a2c4e728106356700.png')

result = normalized_correlation(img1, img2)
print("Normalized Correlation:", result)