import cv2 as cv
import numpy as np

# adaptive thresholding separtes and  locates a regoin of interest (ROI) based on variations of intensity

img = cv.imread('CV-Practice-Image.png', 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,  255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2) # Binary or InvBinary... with binary setting it to max if > threshold val
# 11 is blocksize which determines size of the pixel neighborhood area, 2 is a constant which is subtracted in the threshold equation
th3 = cv.adaptiveThreshold(img,  255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2) # Gaussian rather than mean -> weighted sum of neighborhood vals

cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)

cv.waitKey(0)
cv.destroyAllWindows()
