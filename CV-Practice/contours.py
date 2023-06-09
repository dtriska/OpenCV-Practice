import cv2
import numpy as np

# contours curve joining all continuos points along boundry with same color of intensity
# for accuracy use binary image

img = cv2.imread('CaliPortrait.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# contours var in this call is a list of all contours in the image. Each contour is a numpy array of (x,y) coords of boundary points of the obj
# hierarchy is the output vector w info on image topology
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # reqs 2 return vals, will only be in need of the first
# RETR_TREE retrieves all contours in the image and reconstructs a full hierarchy of nested contours -> not needed in excercise... approx_None finds all contours w/w approximation
print("Number of contours is equal to " + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, -1, (0, 255, 0), 3) # 3 is thickness, -1 means we want all contours

cv2.imshow("cali", img)
cv2.imshow("gray", imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()