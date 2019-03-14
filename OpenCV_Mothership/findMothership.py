import cv2
import numpy as np
#from Centerpoint import center

def main():
	findMothership("mothership.jpg")
	findMothership("mothership1.jpg")
	findMothership("mothership2.jpg")
	findMothership("mothership3.jpg")
	findMothership("mothership4.jpg")
	
def findMothership(name):
	img = cv2.imread(name)
	cv2.imshow("original", img)
	img = cv2.GaussianBlur(img, (5,5), 0)
	cv2.imshow("blurred", img)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, (70, 25, 25), (86, 255, 255))
	imask = mask>0
	green = np.zeros_like(img, np.uint8)
	green[imask] = img[imask]
	cv2.imshow("Green", green)
	
	cv2.waitKey(0);
	print("Done");
	
if __name__ == "__main__":
    main()