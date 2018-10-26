import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time

#Take in the pgoto you want to test
img = cv2.imread('TestBlock.png', 0)

#Create an array of the template images and then make
#	create an array that will save the likeness quantities.
values = []
templates = [cv2.imread('A_1.png',0), cv2.imread('A_2.png',0),
	cv2.imread('C_1.png',0), cv2.imread('C_2.png',0), cv2.imread('D_1.png',0),
	cv2.imread('D_2.png',0), cv2.imread('E_1.png',0), cv2.imread('C_3.png',0),
	cv2.imread('empty.png',0)]

print("Almost to the loop")

for x in templates:
	w, h = x.shape[::-1]
	#compares the two images using a cetyon algo we chose
	res = cv2.matchTemplate(img, x, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	#append max_val for this image to the array of values
	values.append(max_val)
print(values)



