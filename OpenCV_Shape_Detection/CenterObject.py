import cv2
import numpy as np


#	Returns -1 if object is to the left
#			0 if object is in the center
#			1 if object is to the right			

def main():
	center()

def center():
	img = cv2.imread("Center.jpg")  #load an image of a single battery
	img_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert to grayscale
	
	#inverted binary threshold: 1 for the battery, 0 for the background
	_, thresh = cv2.threshold(img_gs, 200, 250, cv2.THRESH_BINARY_INV)
	
	#From a matrix of pixels to a matrix of coordinates of non-black points.
	#(note: mind the col/row order, pixels are accessed as [row, col]
	#but when we draw, it's (x, y), so have to swap here or there)
	mat = np.argwhere(thresh != 0)
	
	#let's swap here... (e. g. [[row, col], ...] to [[col, row], ...])
	mat[:, [0, 1]] = mat[:, [1, 0]]
	#or we could've swapped at the end, when drawing
	#(e. g. center[0], center[1] = center[1], center[0], same for endpoint1 and endpoint2),
	#probably better performance-wise
	
	mat = np.array(mat).astype(np.float32) #have to convert type for PCA
	
	#mean (e. g. the geometrical center) 
	#and eigenvectors (e. g. directions of principal components)
	m, e = cv2.PCACompute(mat, mean = np.array([]))
	
	#now to draw: let's scale our primary axis by 100, 
	#and the secondary by 50
	
	center = tuple(m[0])					# THE CENTER POINT!
	endpoint1 = tuple(m[0] + e[0]*100)
	endpoint2 = tuple(m[0] + e[1]*50)
	
	red_color = (0, 0, 255)
	cv2.circle(img, center, 5, red_color)
	cv2.line(img, center, endpoint1, red_color)
	cv2.line(img, center, endpoint2, red_color)
	cv2.imshow("Threshold", thresh)
	cv2.imshow("Img", img)
	
	imageSize = img.shape[:2]
	imageCenter = img.shape[:2]
	imageCenter = (imageCenter[0]/2, imageCenter[1]/2)
	
	CENTER_RANGE = 5
	
	cv2.waitKey(0)
	
	#cv2.circle(img, int(imageCenter), 5, (0,0,0))
	
	print("Center of obj: " + str(center))
	print("Size of the image: " + str(imageSize))
	print("The center coordinate: " + str((imageSize[0]/2, imageSize[1]/2)))
	print("The difference: " + str(center[1] - imageCenter[1]))
	
	cv2.line(img, (int(imageCenter[0]), int(imageCenter[1])), (int(imageSize[0]/2), int(imageSize[1])), (0,0,255))
	
	if center[1] - imageCenter[1] > CENTER_RANGE:
		print("Object is to the left")
		return 1
	elif center [1] - imageCenter[1] < -CENTER_RANGE:
		print("Object is to the right")
		return -1
	else:
		print("Object is in the center")
		return 0
	


 
if __name__ == "__main__":
    main()
