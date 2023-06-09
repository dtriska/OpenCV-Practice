import cv2
import numpy as np

# first bit of work with numpy... and lines on images
# img = cv2.imread('CV-Practice-Image.png', -1)

img = np.zeros([512, 512, 3], np.uint8) # makes a blank, black image

img = cv2.line(img, (0, 0), (255, 255), (0, 255, 0), 10) # if you want line to be on display it must go before the imshow method 
# if imread is made in grayscale, line will also be grayscale

img = cv2.imshow('Image', img)

k = cv2.waitKey(0)


if k == 27: #escape key = :27
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('copy_of_image.png', img)
    cv2.destroyAllWindows()