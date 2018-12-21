import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys
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

def main():
    compartor_list = 'Stencil_A.png', 'Stencil_B.png', 'Stencil_C.png', 'Stencil_D.png', 'Stencil_E.png', 'Stencil_F.png'
    original = cv2.imread('D_Testing.png',0) #loading in the two images and resisizing the photo we took
    ret, original = cv2.threshold(original, 100, 255, cv2.THRESH_BINARY) #binary thresh it at value 100. It is now a black and white image

    mseValue = sys.maxsize
    mseIndex = 0

    for i in range (0,6):
        compartor = cv2.imread(compartor_list[i],0)

        m = mse(original,compartor)
        if (m < mseValue):
            mseValue = m
            mseIndex = i

    switcher = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F"
    }

    print (switcher.get(mseIndex, "Unclear"))

if __name__ == "__main__":
    main()