from imutils import paths
import numpy as np
import imutils
import cv2

def main():
	calcDist("knownDistance5.png")
	calcDist("knownDistance8.png")

# Finds focal lengths. Used for calibration
def findFocalLength(name, KNOWN_DISTANCE):
	#KNOWN_DISTANCE = 5
	KNOWN_WIDTH = 1.5
	image = cv2.imread(name)
	marker = find_marker(image)
	focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
	print(focalLength)

# Returns the image with distance	
def calcDist(name):
	KNOWN_WIDTH = 1.5
	FOCAL_LENGTH = 500
	
	image = cv2.imread(name)
	marker = find_marker(image)
	inches = dist2Cam(KNOWN_WIDTH, FOCAL_LENGTH, marker[1][0])
	box = cv2.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
	box = np.int0(box)
	cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
	cv2.putText(image, "%.2fin" % (inches),
		(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
		2.0, (0, 255, 0), 3)
	cv2.imshow("image", image)
	cv2.waitKey(0)

# returns contour with largest area
def find_marker(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1] #optimal threshold 103
	edged = cv2.Canny(gray, 35, 125)
	cv2.imshow("", edged)
	cv2.waitKey(0)
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv2.contourArea)

	return cv2.minAreaRect(c)
	
# Calculates the distance
def dist2Cam(knownWidth, focalLength, perWidth):
	return knownWidth * focalLength / perWidth
	
if __name__ == '__main__':
	main()