import cv2
import numpy as np
from sklearn.cluster import KMeans
#from Centerpoint import center

def main():
	findMothership("mothership.jpg")
	findMothership("mothership1.jpg")
	findMothership("mothership2.jpg")
	findMothership("mothership3.jpg")
	findMothership("mothership4.jpg")
	
def findMothership(name):
	img = cv2.imread(name)
	#cv2.imshow("original", img)
	orig = img
	img = cv2.GaussianBlur(img, (5,5), 0)
	#cv2.imshow("blurred", img)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, (40, 10, 180), (100, 180, 240))
	imask = mask>0
	green = np.zeros_like(img, np.uint8)
	green[imask] = img[imask]
	
	#create imask which is array of coordinates of non-zero pixels
	dim = (img.shape[0], img.shape[1])
	imask = np.zeros(dim) + 1 * imask
	imask = np.transpose(np.nonzero(np.transpose(imask)))

	#kmeans clustering to find center points
	kmeans = KMeans(n_clusters=6)
	kmeans.fit(imask)
	
	#centers is array of center coordinates of clusters
	centers = kmeans.cluster_centers_
	centers = [(int(x[0]),int(x[1])) for x in centers]
	
	#put circles on img of where the clusters are
	for x in range(0,len(centers)):
		cv2.circle(orig, tuple(centers[x]), 8, (0,0,255))
	
	cv2.imshow("original", orig)
	cv2.imshow("Green", green)
	
	cv2.waitKey(0);
	print("Done");
	
if __name__ == "__main__":
    main()
