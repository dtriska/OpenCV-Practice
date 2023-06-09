import numpy as np
import cv2 as cv

# bg subtraction is used for generating foreground mask AKA binary image w pixels belonging to moving obj on a scene with a static camera

cap = cv.VideoCapture('ocean.mp4')

fgbg = cv.bgsegm.createBackgroundSubtractorMOG() 
# if you havent downloaded the correct numpy file, use cv2.createBackgroundSubtractorMOG2 -> this vers accounts for shadows and more moving parts... for better or worse


while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame) # creates the mask

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask Frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()