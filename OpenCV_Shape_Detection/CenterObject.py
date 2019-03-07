import cv2
import imutils

# https://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/

#	Returns -1 if object is to the left
#			0 if object is in the center
#			1 if object is to the right			

def main():
	center()

def center():
	image = cv2.imread("Right.jpg")
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
	
	cv2.imshow("thresh", thresh)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	
	# loop over the contours
	for c in cnts:
		# compute the center of the contour
		M = cv2.moments(c)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		
		# draw the contour and center of the shape on the image
		cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
		cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
		cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	
		# show the image
		cv2.imshow("Image", image)
		cv2.waitKey(0)
		
	# Get the dimensions of the image
	(width, height) = image.shape[:2]
	
	print("Size of the image: " + str(width) + ", " + str(height))
	print("Center of obj: " + str(cX) + ", " + str(cY))
	print("The center coordinate: " + str(width/2, height/2)
	
	
	
	
if __name__ == '__main__':
	main()