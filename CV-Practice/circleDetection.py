import numpy as np
import cv2 as cv

img = cv.imread('circles2.png') # bad image selection
output = img.copy()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5) # kernal size of 5 which dictates the impact of surronding pixels
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, 
                          minRadius=0, maxRadius=0) # simiar to HoughLines, but just circles instead
detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 255, 0), 3) # draws circle, center of circle is tuple, r is radius
    cv.circle(output, (x, y), 2, (0, 255, 255), 3) # draws small circle if small radius


cv.imshow('output', output)
cv.waitKey(0)
cv.destroyAllWindows()