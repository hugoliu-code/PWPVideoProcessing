import cv2
import numpy as np

image = cv2.imread('/Users/19548/Downloads/test_easy.png')
output = image.copy()
gray = cv2.imread('/Users/19548/Downloads/test_easy.png',0)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,250,
                            param1=30,param2=50,minRadius=50,maxRadius=61)
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 6)
		cv2.circle(output, (x, y), 1, (0, 255, 0), 15)
	# show the output image
	cv2.imshow("TEST CASE ONE", np.hstack([output, image]))
	cv2.waitKey(5000)


image = cv2.imread('/Users/19548/Downloads/test_easy2.png')
output = image.copy()
gray = cv2.imread('/Users/19548/Downloads/test_easy2.png',0)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,250,
                            param1=30,param2=50,minRadius=10,maxRadius=100)
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 6)
		cv2.circle(output, (x, y), 1, (0, 255, 0), 15)
	# show the output image
	cv2.imshow("TEST CASE TWO", np.hstack([output, image]))
	cv2.waitKey(5000)
#TRANSFORM TEST CASE!!!!!

image = cv2.imread('/Users/19548/Downloads/test_l2.png')
output = image.copy()
gray = cv2.imread('/Users/19548/Downloads/test_l2.png',0)
cv2.circle(image, (0,0), 5, (0,0,255),-1)
cv2.circle(image, (0,533), 5, (0,0,255),-1)
cv2.circle(image, (800,0), 5, (0,0,255),-1)
cv2.circle(image, (800,533), 5, (0,0,255),-1)

pts1 = np.float32([[0,0],[0,533],[800,0],[800,533]])
pts2 = np.float32([[0,0],[440,533],[780,30],[780, 500]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(gray, matrix, (800, 533))
result2 = cv2.warpPerspective(image, matrix, (800, 533))
circles = cv2.HoughCircles(result,cv2.HOUGH_GRADIENT,1.2,500, param1=30,param2=50,minRadius=50,maxRadius=108)
# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(result2, (x, y), r, (0, 255, 0), 6)
		cv2.circle(result2, (x, y), 1, (0, 255, 0), 15)
	# show the output image
pts3 = np.float32([[0,0],[0,533],[800,0],[800,533]])
pts4 = np.float32([[0,0],[440,533],[780,30],[780, 500]])
matrix = cv2.getPerspectiveTransform(pts4, pts3)
output = cv2.warpPerspective(result2, matrix, (800, 533))
cv2.imshow("TEST CASE THREE", output)
# cv2.imshow("hiii", result)
cv2.waitKey(0)