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
    compartor_list = 'Stencil_A_0.png', 'Stencil_A_90.png', 'Stencil_A_180.png', 'Stencil_A_270.png',\
                     'Stencil_B_0.png', 'Stencil_B_90.png', 'Stencil_B_180.png', 'Stencil_B_270.png',\
                     'Stencil_C_0.png', 'Stencil_C_90.png', 'Stencil_C_180.png', 'Stencil_C_270.png',\
                     'Stencil_D_0.png', 'Stencil_D_90.png', 'Stencil_D_180.png', 'Stencil_D_270.png',\
                     'Stencil_E_0.png', 'Stencil_E_90.png', 'Stencil_E_180.png', 'Stencil_E_270.png',\
                     'Stencil_F_0.png', 'Stencil_F_90.png', 'Stencil_F_180.png', 'Stencil_F_270.png'
    original = cv2.imread('A_Testing_180.png',0) #loading in the two images and resisizing the photo we took
    ret, original = cv2.threshold(original, 100, 255, cv2.THRESH_BINARY) #binary thresh it at value 100. It is now a black and white image

    values = 0,0,0,0,0,0
    total = 0
    minIndex = 0
    minValue = sys.maxsize

    for i in range (0,6):
        for j in range (0,4):
            compartor = cv2.imread(compartor_list[total],0)
            m = mse(original,compartor)
            values[i] += m
            ++total
        values[i] = values[i]/4

    for i in range (0,6):
        if (values[i] < minValue):
            minIndex = i
            minValue = values[i]




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