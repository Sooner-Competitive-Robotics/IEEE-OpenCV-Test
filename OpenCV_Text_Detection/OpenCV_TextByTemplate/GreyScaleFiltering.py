import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time

original = cv2.imread('D_Temp.png',0)

#img = cv2.imread('D_Temp.png',cv2.IMREAD_GRAYSCALE)

ret,thresh = cv2.threshold(original, 200, 255, cv2.THRESH_BINARY)

cv2.imshow('original',original)
#cv2.imshow('grey',img)
cv2.imshow('threshold', thresh)
cv2.waitKey(0)