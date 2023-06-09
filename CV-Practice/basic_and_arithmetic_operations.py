import cv2
import numpy as np

img = cv2.imread('CV-Practice-Image.png')
img2 = cv2.imread('CaliPortrait.png')

print(img.shape) # will give a tuple containt number of rows, colums, and channels
print(img.size) # will give number of pixels accessed in image
print(img.dtype) # will return image datatype obtained

b, g, r = cv2.split(img) # splits image into its appropriate blue green and red colors
img = cv2.merge((b, g, r)) # merges the split colors to produce appropriate color

cutout = img[28:34, 33:39] # get numpy coords of img, 280:340 is upper left, 330:390 is bottom right
img[27:33, 10:16] = cutout # places area of image associated with cutout, on the area provided in the img coords 

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .9, img2, .1, 0)

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
