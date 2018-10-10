import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time

img = cv2.imread('Test.jpg', 0)
img2 = img.copy()
template = cv2.imread('Template_A.png',0)
cv2.imshow('image', template)

w, h = template.shape[::-1]
res = cv2.matchTemplate(img,template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img,top_left, bottom_right, 255, 2)
plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle('TM_CCOEFF')

plt.show()





