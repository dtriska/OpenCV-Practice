import cv2
import numpy as np
img = cv2.imread("CV-Practice-Image.png")

# creates images of diff resolution and can search for image with proper res
# pyramid representation is a type of multi scale signal in which a signal or image is subject to repeated smoothing and subsampling

# Gaussian and Laplacian pyramids are the 2 types

# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# # PyrDown causes us to lose some info -> cant go down and back up to orig image
# # pyrUp increases resolution

# cv2.imshow("Orig", img)
# cv2.imshow("PyrDown", lr1)
# cv2.imshow("PyrDown2", lr2)

layer = img.copy() # the for loop instantly layers the pyramid and creates multiple pyrdown images
gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)


# A level in laplacian pyramid is formed by the difference between that level in gaussian pyramid and expanded version of its uppel level in gaussian pyramid
layer = gp[5]
cv2.imshow('upper level GP', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_ext = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i - 1], gaussian_ext)
    cv2.imshow(str(i), laplacian)

# laplacian and gaussian helps blank and reconstruct images

cv2.waitKey(0)
cv2.destroyAllWindows()