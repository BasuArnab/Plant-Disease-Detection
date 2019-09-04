import cv2
import numpy as np
img=cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)
image=cv2.imread('1.jpg')
img=cv2.resize(img,(200,600))
image=cv2.resize(image,(200,600))
img = cv2.GaussianBlur(img, (5,5), 3)
params = cv2.SimpleBlobDetector_Params()
params.filterByColor=1
params.filterByInertia = False
params.filterByConvexity = False
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(img)
img = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
while True:
	cv2.imshow("original image",image)
	cv2.imshow("image",img)
	key = cv2.waitKey(1) & 0xFF
	if cv2.waitKey(33) == 27:
		break
cv2.destroyAllWindows()