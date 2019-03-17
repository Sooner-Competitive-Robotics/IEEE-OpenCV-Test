import cv2
import imutils

# https://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/

# Returns -1 if object is to the left
#			0 if object is in the center
#			1 if object is to the right

def main():
	image = cv2.imread("picamera1.png")
	cv2.imshow("image", image)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.GaussianBlur(image, (5,5), 0)

	image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)[1]
	
	cv2.imshow("thresh", image)
	cv2.waitKey(0)
	#center("picamera1.png")
	#center("Left.jpg")
	#center("Right.jpg")
	#enter("Center.jpg")
	
	
def center(imagename):
	image = cv2.imread(imagename)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
	
	cv2.imshow("thresh", thresh)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	
	for c in cnts:
		M = cv2.moments(c)
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		
		cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
		cv2.circle(image, (cX, cY), 7, (0, 0, 255), -1)
		cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		
		cv2.imshow("Image", image)
		cv2.waitKey(0)
	
	# image dim
	width, height = image.shape[:2]
	
	print("Image dimension: " + str(width) + ", " + str(height))
	print("Image center: " + str(width/2) + ", " + str(height/2))
	print("Center of object: " + str(cX) + ", " + str(cY))
	
	# Get the x coord difference
	diff = cX - width/2
	print("Object away from center: " + str(diff))
	
	CENTER_RANGE = 50
	
	if diff > CENTER_RANGE:
		print("Right")
		return 1
	elif diff < -CENTER_RANGE:
		print("Left")
		return -1
	else:
		print("Center")
		return 0

if __name__ == '__main__':
	main()
