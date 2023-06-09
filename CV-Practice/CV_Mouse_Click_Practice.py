import numpy as np
import cv2

# basic click event file

def click_event(event, x , y, flags, param):
    # makes a line at clicked points on image
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0, 0, 255), -1) # makes a closed dot circle at mouse click location
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        myColorImage = np.zeros((512, 512, 3), np.uint8)
        myColorImage[:] = [blue, green, red]

        cv2.imshow('color', myColorImage)
        
        

# img = np.zeros((512, 512, 3), np.uint8)
points = []
img = cv2.imread('CV-Practice-Image.png')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event) # calls the mouse click even when clicking on the image

cv2.waitKey(0)
cv2.destroyAllWindows()


# LBUTTONDOwN coordinate location code for click_event
# print(x, ' , ' , y)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strXY = str(x) + ' , ' + str(y)
#         cv2.putText(img, strXY, (x, y), font, 0.5, (255, 255, 0), 2)
#         cv2.imshow('image', img)


# used to make a line between two mouse click points
# used beneath click_event func
# points.append((x, y))
#         if len(points) >= 2: # only want to make a line if there are at least two mouse clicks
#             cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
#         cv2.imshow('image', img)