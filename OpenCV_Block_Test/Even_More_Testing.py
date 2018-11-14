import cv2
import numpy as np
import time

img_bgr = cv2.imread('A_1.png')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

img_bgr = cv2.resize(img_bgr, (960,680))
img_gray = cv2.resize(img_gray, (960,680))

template = cv2.imread('Stincil_A.png', 0)
template = cv2.resize(template, (120,75))
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCORR_NORMED)
threshold = .89
loc = np.where(res >= threshold)
x = 0
for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h),(0,255,255), 2)
	print(x)
	x = x+1
	

cv2.imshow('detected', img_bgr)