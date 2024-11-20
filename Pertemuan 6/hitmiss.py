# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:06:03 2024

@author: HP
"""

import mahotas as mh 
import numpy as np 
from pylab import imshow, show 
    
# membuat region
# numpy.ndarray 
regions = np.zeros((10, 10), bool)

# setting 1 value to the region 
regions[2, :4] = 1
regions[2:8, 8: 10] = 1
regions[4, 0] = 1

print("img") 
imshow(regions, interpolation ='nearest') 
show()

template = np.array([ 
            [0, 1, 1], 
            [0, 1, 1], 
            [0, 1, 1]]) 

# hit miss transform 
img = mh.hitmiss(regions, template) 
  
# showing image 
print("Gambar after transformasi") 
imshow(img) 
show()
