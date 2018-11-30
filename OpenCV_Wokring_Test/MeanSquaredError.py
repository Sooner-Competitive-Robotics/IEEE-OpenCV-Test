from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import time

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	
	return err

compartor_list = 'Stencil_A.png', 'Stencil_B.png', 'Stencil_C.png', 'Stencil_D.png', 'Stencil_E.png', 'Stencil_F.png'
original = cv2.imread('D_Testing.png',0) #loading in the two images and resisizing the photo we took
original = cv2.resize(original, (680,680))

for i in range (0,6):
	compartor = cv2.imread(compartor_list[i],0)
	
	m = mse(original,compartor)
	s = ssim(original,compartor)
	fig = plt.figure('difference between the two images')
	plt.suptitle("MSE: %.2f, SSIM: %.2f" %(m, s))

	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(original, cmap = plt.cm.gray)
	plt.axis("off")
	
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(compartor, cmap = plt.cm.gray)
	plt.axis("off")
	
	# show the images
	plt.show()





cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)