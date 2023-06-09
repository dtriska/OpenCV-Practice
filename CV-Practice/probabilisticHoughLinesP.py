# Optimization of previous Hough-trans.py
# Useful for detecting lines
# this optimized vers wont give a result that has lines never ending
import cv2
import numpy as np

img  = cv2.imread('Sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3) # canny edge detection, 50 and 150 are the first and second threshold
cv2.imshow('Canny', edges)
# lines in HoughLines is in polar coords, rep by 2 or 3 element vectors either rho theta or rho theta and vertz
# edge detected image, rho: dist resolution of acc in pixel, theta val: angle resolution of acc in radians, acc threshold parameter, min length of line, max gap between segments to be treated as single line
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10) 

# to make a line you ofc need at least two points
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()