import numpy as np
import cv2
import math
#"/Users/local/Downloads/IMG-3675.jpg"
image = cv2.imread("/Users/19548/Downloads/IMG_3675.jpg")
output= cv2.imread("/Users/19548/Downloads/IMG_3675.jpg")
# 3264x2448

p1 = (-400,300)
p2 = (3664,300)
p3 = (1632, 2800)
color = (207,219,221)
cv2.line(image, p1, p2, color, 1100)
cv2.line(image, p2, p3, color, 1100)
cv2.line(image, p1, p3, color, 1100)
start_point = (0,2448)
start_point2 = (3264, 2448)
end_point = (200,2000)
end_point2 = (3000,2000)
cv2.rectangle(image, start_point, end_point, color, 1250)
cv2.rectangle(image, start_point2, end_point2, color, 1200)


image = cv2.resize(image, (544, 408))
output = cv2.resize(output,(544,408))
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,75,150)
# cv2.imshow("hi",image)
# cv2.waitKey(0)
#260
#3rd one
#lines = cv2.HoughLinesP(edges,1,np.pi/12,20,minLineLength = 50, maxLineGap = 30)
#2nd one
#lines = cv2.HoughLinesP(edges,1,np.pi/180,20,minLineLength = 10, maxLineGap = 100)
lines = cv2.HoughLinesP(edges,1,np.pi/180,20,minLineLength = 10, maxLineGap = 100)
# leftsideSmallestY = 2448
# leftsideLargestY = 0
# lx1 = 0
# lx2 = 0
# RightSideLargestY = 0
# RightSideSmallestY = 2448
# rx1 = 0
# rx2 = 0
# arrayxRight = []
# arrayyRight = []
# arrayxLeft = []
# arrayyLeft= []
totalx1 = 0
totaly1 = 0
totalx2 = 0
totaly2 = 0
found = False
linesFound = 0
for line in lines:
    for x1,y1,x2,y2 in line:

        linesFound = linesFound +1;
        if(y1 > y2):
            totalx1 = totalx1 + x1
            totaly1 = totaly1 + y1
            totalx2 = totalx2 + x2
            totaly2 = totaly2 + y2
        else:
            totalx1 = totalx1 + x2
            totaly1 = totaly1 + y2
            totalx2 = totalx2 + x1
            totaly2 = totaly2 + y1

        colors = list(np.random.random(size=3) * 256)
        cv2.line(image,(x1,y1),(x2,y2),(255,0,0),1)
        if (found):
            break

# arrayxRightSorted = arrayxRight.copy();
# arrayyRightSorted = arrayyRight.copy();
# arrayxLeftSorted = arrayxLeft.copy();
# arrayyLeftSorted = arrayyLeft.copy();
# arrayxRightSorted.sort()
# arrayyRightSorted.sort()
# arrayxLeftSorted.sort()
# arrayyLeftSorted.sort()
# cv2.line(image,start,finish,(0,255,0),20)
color = (200,0,0)
# cv2.line(image, ((int)((firstx1+lastx1)/2), (int)((firsty1+lasty1)/2)), ((int)((firstx2+lastx2)/2), (int)((firsty2+lasty2)/2)), color, 50)
cv2.arrowedLine(output, (round(totalx1/linesFound), round(totaly1/linesFound)), (round(totalx2/linesFound), round(totaly2/linesFound)), color, 5)
cv2.imwrite('houghlines3.jpg',image)
cv2.imshow("image", image)
cv2.imshow("output", output)
# cv2.imshow("image", output)
cv2.waitKey(0)


