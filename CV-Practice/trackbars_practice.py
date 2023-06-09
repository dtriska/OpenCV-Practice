import cv2 as cv
import numpy as np

# trackbars are useful whenever you have a variable that you dont know alr what value it should have

def nothing(x): # value of current position of trackbar
    print(x) # prints

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0XFF
    if k == 27:
        break
        
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')

    img[:] = [b, g, r]

cv.destroyAllWindows()