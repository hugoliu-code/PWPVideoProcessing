import numpy as np
import cv2
import math


fileName = "/Users/local/Downloads/IMG_3708.jpg"
# fileName = "/Users/local/Downloads/IMG-3707.jpg"
image = cv2.imread(fileName)
output = cv2.imread(fileName)
cv2.imshow("picture", image)
cv2.waitKey(0)
image = cv2.line(image, (0,0), (0,2448), (184, 196, 196), 2000)
image = cv2.line(image, (3624, 0), (3624, 2448), (184, 196, 196), 2000)
image = cv2.line(image, (0,0),(2448,0), (184, 196, 196), 800)
resized = cv2.resize(image, ((int)(3264 / 3), (int)(2448 / 3)))
cv2.imshow("picture", resized)
cv2.waitKey(0)
print(image[1600, 1200])
lastMedianx = 1800
lastMediany = 3600
i = 0
topPoint = [1632, 1600]
leftPoint = [300, 1800]
rightPoint = [2900, 1800]
while (i < 8):

    resized = cv2.resize(image, ((int)(3264/3),(int) (2448/3)))

    cv2.imshow("picture", resized)
    cv2.waitKey(0)
    print(topPoint)
    print(leftPoint)
    print(rightPoint)

    image = cv2.imread(fileName)
    image = cv2.line(image, (0, 0), (0, 2448), (184, 196, 196), 2000)
    image = cv2.line(image, (3624, 0), (3624, 2448), (184, 196, 196), 1800)
    image = cv2.line(image, (0, 0), (2448, 0), (184, 196, 196), 1000)
    fill_color = [184, 196, 196]  # any BGR color value to fill with
    mask_value = 255  # 1 channel white (can be any non-zero uint8 value)

    # contours to fill outside of

    contours = [np.array([leftPoint, topPoint, rightPoint])
                ]
    # our stencil - some `mask_value` contours on black (zeros) background,
    # the image has same height and width as `img`, but only 1 color channel
    stencil = np.zeros(image.shape[:-1]).astype(np.uint8)
    cv2.fillPoly(stencil, contours, mask_value)

    sel = stencil != mask_value  # select everything that is not mask_value
    image[sel] = fill_color  # and fill it with fill_color
    # Image Processing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 40, minLineLength=30, maxLineGap=20)

    # Total x and y values
    totalx1 = 0
    totaly1 = 0
    totalx2 = 0
    totaly2 = 0
    found = False
    linesFound = 0
    for line in lines:
        for x1, y1, x2, y2 in line:
            # make sure points are saved in the right orientation
            linesFound = linesFound + 1;
            if (y1 > y2):
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
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 5)
            if (found):
                break
    color = (200, 0, 0)

    i += 1
    # find median points
    newMedianx = round((totalx1 + totalx2) / (2 * linesFound))
    newMediany = round((totaly1 + totaly2) / (2 * linesFound))
    cv2.line(image, (newMedianx, newMediany), (newMedianx+4, newMediany+4), (255, 0, 0), 5)
    # print("Medians")
    # print(newMedianx)
    # print(newMediany)

    if not (lastMedianx == 1800 and lastMediany == 3600):
        cv2.arrowedLine(output, (lastMedianx, lastMediany),
                        (newMedianx, newMediany), color, 5)

        # Find Angle of Direction between two points
        RadianRotation = (-math.atan2( newMediany - lastMediany, newMedianx - lastMedianx))/8
        if(( newMediany - lastMediany> 0 or newMedianx - lastMedianx > 0)):
            RadianRotation = (math.atan2(newMediany - lastMediany, newMedianx - lastMedianx)) / 8
        # RadianRotation = -(math.pi / 6)
        # # if (RadianRotation < 0):
        # if((newMedianx - lastMedianx)/(newMediany - lastMediany) < 0)
        print(math.degrees(RadianRotation))
        addx = (int)(leftPoint[0] + rightPoint[0])
        addy = (int)(leftPoint[1] + rightPoint[1])
        if (RadianRotation == 0):
            topPoint = [(int)(topPoint[0]), (int)(topPoint[1] - 100)]
            leftPoint = [(int)(leftPoint[0]), (int)(leftPoint[1] - 100)]
            rightPoint = [(int)(rightPoint[0]), (int)(rightPoint[1] - 100)]

        else:
            topPoint = [-topPoint[0], topPoint[1]]
            leftPoint = [-leftPoint[0], leftPoint[1]]
            rightPoint = [-rightPoint[0], rightPoint[1]]


            offsetx = (int)((rightPoint[0] + leftPoint[0])/2)
            offsety = (int)((rightPoint[1] + leftPoint[1]) / 2)

            topPoint = [topPoint[0] - offsetx, topPoint[1] - offsety]

            topPoint = [topPoint[0] * math.cos(RadianRotation) + topPoint[1] * math.sin(RadianRotation),
                        topPoint[1] * math.cos(RadianRotation) - topPoint[0] * math.sin(RadianRotation)]

            topPoint = [(int)(topPoint[0] + offsetx), (int)(topPoint[1] + offsety)]
            leftPoint = [leftPoint[0] - offsetx, leftPoint[1] - offsety]

            leftPoint = [leftPoint[0] * math.cos(RadianRotation) + leftPoint[1] * math.sin(RadianRotation),
                         leftPoint[1] * math.cos(RadianRotation) - leftPoint[0] * math.sin(RadianRotation)]

            leftPoint = [(int)(leftPoint[0] + offsetx), (int)(leftPoint[1] + offsety)]
            rightPoint = [rightPoint[0] - offsetx, rightPoint[1] - offsety]

            rightPoint = [rightPoint[0] * math.cos(RadianRotation) + rightPoint[1] * math.sin(RadianRotation),
                          rightPoint[1] * math.cos(RadianRotation) - rightPoint[0] * math.sin(RadianRotation)]

            rightPoint = [(int)(rightPoint[0] + offsetx), (int)(rightPoint[1] + offsety)]


            topPoint = [-topPoint[0],topPoint[1]]
            leftPoint = [-leftPoint[0], leftPoint[1]]
            rightPoint = [-rightPoint[0],rightPoint[1]]

            topPoint = [topPoint[0] +(int)(300*math.sin(RadianRotation)), topPoint[1] - (int)(300*math.cos(RadianRotation))]
            leftPoint = [leftPoint[0] + (int)(300*math.sin(RadianRotation)), leftPoint[1]- (int)(300*math.cos(RadianRotation))]
            rightPoint = [rightPoint[0] + (int)(300*math.sin(RadianRotation)), rightPoint[1]- (int)(300*math.cos(RadianRotation))]



    else:
        topPoint = [(int)(topPoint[0]), (int)(topPoint[1] - 100)]
        leftPoint = [(int)(leftPoint[0]), (int)(leftPoint[1] - 100)]
        rightPoint = [(int)(rightPoint[0]), (int)(rightPoint[1] - 100)]

    lastMedianx = newMedianx
    lastMediany = newMediany



resized = cv2.resize(output, ((int)(3264 / 3), (int)(2448 / 3)))
cv2.imshow("picture", resized)
cv2.waitKey(0)
