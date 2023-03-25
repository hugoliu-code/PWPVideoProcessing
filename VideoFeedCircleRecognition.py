import numpy as np
import cv2 as cv
cap = cv.VideoCapture("/Users/19548/Downloads/IMG_3659.avi")
# /Users/local/Downloads/IMG_3659.avi
total = 0
found = 0
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Finished")
        break
    output = frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.60, 200, param1 = 100, param2 = 90, minRadius = 100, maxRadius = 250)
    # ensure at least some circles were found
    if circles is not None:
        total += 1
        found += 1
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv.circle(output, (x, y), r, (0, 255, 0), 3)
            cv.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), 20)
    else:
        total += 1
    cv.imshow('frame', output)
    if cv.waitKey(1) == ord('q'):
        break
    cv.waitKey(25)

print(found/total)
cap.release()
cv.destroyAllWindows()