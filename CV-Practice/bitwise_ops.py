import numpy as np
import cv2

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("HalfB-HalfW.jpg")
img2 = cv2.resize(img2, (500, 250))

# if you dont know, study bitwise ops... its fairly straight forward :)

bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img2, img1)
bitNot1 = cv2.bitwise_not(img2)
bitNot2 = cv2.bitwise_not(img1)

cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.imshow('BitAnd', bitAnd)
cv2.imshow('bitOR', bitOr)
cv2.imshow('bitXOR', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)


cv2.waitKey(0)
cv2.destroyAllWindows()