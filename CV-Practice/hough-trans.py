import cv2 
import numpy as np

# Hough transform is a popular technique to detect any shape, if you can represent that shape in a mathematical form. It can detect a shape even if it is broken or distorted a bit
# A line in an image can be represented with two variables... Cartesian coords y = mx + b or Polar coords xcos(theta) + ysin(theta) = r

# Hough Space is represented in the mc space rather than the xy space
# Hough space allows us to represent a single point rather than needing to do a collection of points -> this is the capabilities of using the mc space
# formula for mc space is c = xm + ym -> slope is x and y is intercept
# every point is a line that intersects with each other at a single point to give the (m, c) point

# Hough transform algo
# Edge detection EX Canny edge detector
# Mapping of edge points to Hough space and storae in an accumulator
# Interpretation of accumulator yield lines of infinite length. Done by thresholding and possbily other constraints
# Conversion of infinite lines to finite lines

img  = cv2.imread('Sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3) # canny edge detection, 50 and 150 are the first and second threshold
cv2.imshow('Canny', edges)
# lines in HoughLines is in polar coords, rep by 2 or 3 element vectors either rho theta or rho theta and vertz
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200) # Houghlines takes source img, row value is distance resolution of acc in pixels, theta which is angle resolution of acc in radians, acc threshold parameter -> only returns lines within threshold

for line in lines:
    # rho is distance from coord (0, 0) (top left), and theta is line rotation angle in radians
    # want to tranform into normal cartesian coordinates for line formula
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    # x0 and y0 will give origin/top left corner of image
    x0 = a * rho
    y0 = b * rho
    # x1 stores the rounded off value of (rho * cos(theta) + 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2) # 2 is line thickness

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()