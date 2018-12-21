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
    compartor_list = 'Stencil_A_0.png', 'Stencil_B_0.png', 'Stencil_C_0.png', 'Stencil_D_0.png', 'Stencil_E_0.png', 'Stencil_F_0.png',\
                     'Stencil_A_90.png', 'Stencil_B_90.png', 'Stencil_C_90.png', 'Stencil_D_90.png', 'Stencil_E_90.png', 'Stencil_F_90.png',\
                     'Stencil_A_180.png', 'Stencil_B_180.png', 'Stencil_C_180.png', 'Stencil_D_180.png', 'Stencil_E_180.png', 'Stencil_F_180.png', \
                     'Stencil_A_0.png', 'Stencil_B_0.png', 'Stencil_C_0.png', 'Stencil_D_0.png', 'Stencil_E_0.png', 'Stencil_F_0.png'
    original = cv2.imread('D_Testing.png',0) #loading in the two images and resisizing the photo we took
    ret, original = cv2.threshold(original, 100, 255, cv2.THRESH_BINARY) #binary thresh it at value 100. It is now a black and white image
    mseValue = sys.maxsize
    mseIndex = 0
    cv2.waitKey(10000000)

    for i in range (0,24):
        compartor = cv2.imread(compartor_list[i],0)

        m = mse(original,compartor)
        if (m < mseValue):
            mseValue = m
            mseIndex = i

    switcher = {
        0: "A_0",
        1: "B_0",
        2: "C_0",
        3: "D_0",
        4: "E_0",
        5: "F_0",
        6: "A_90",
        7: "B_90",
        8: "C_90",
        9: "D_90",
        10: "E_90",
        11: "F_90",
        12: "A_180",
        13: "B_180",
        14: "C_180",
        15: "D_180",
        16: "E_180",
        17: "F_180",
        18: "A_270",
        19: "B_270",
        20: "C_270",
        21: "D_270",
        22: "E_270",
        23: "F_270",
    }

    print (switcher.get(mseIndex, "Unclear"))

if __name__ == "__main__":
    main()