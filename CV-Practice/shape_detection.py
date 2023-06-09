import cv2
import numpy as np

img = cv2.imread('shapes.png')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    # True as we know its clossed for arclength
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True) # approximates a polygons curves w specific posistion, epsilon paramter specifying approximation accuracy
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5) # getting the contours of the polygon
    x = approx.ravel()[0] # ravel gives the x and y coords f=needed for the text
    y = approx.ravel()[1] -50 # the -50 moves the text up on the image
    if len(approx) == 3: # length of approx is number of curves/sides
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h # relationship between its width and height
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:     
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, "Other", (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0, 0, 0))

cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()