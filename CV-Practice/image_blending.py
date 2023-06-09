import cv2
import numpy as np

# strawberry reconstructed window is final product
# looking to bring together two images and blend them to flesh out a nice looking final product

# PyrUp and PyrDown scale up and down images by altering pixels to produce an image that is larger or smaller

apple = cv2.imread('apple.jpg')
strawb = cv2.imread('strawberry.jpg')
apple = cv2.resize(apple, (350, 350))
strawb = cv2.resize(strawb, (350, 350))

# hstack takes a sequence of arrays or images as input and returns a single array or image by stacking them horizontally
apple_strawb = np.hstack((apple[:, :175], strawb[:, 175:]))

# generate Gaussian pyramid for apple
# The Gaussian pyramid is a sequence of downsampled images, where each level is obtained by applying Gaussian blurring followed by downsampling of the previous level
# reduces the resolution of the image while preserving its overall structure and removing high-frequency details.

apple_c = apple.copy()
gp_apple = [apple_c]

for i in range(6):
    apple_c = cv2.pyrDown(apple_c)
    gp_apple.append(apple_c)

# generate Gaussian pyramid for strawberry

strawb_c = strawb.copy()
gp_strawb = [strawb_c]

for i in range(6):
    strawb_c = cv2.pyrDown(strawb_c)
    gp_strawb.append(strawb_c)

# generate Laplacian pyramid for apple
#  Each level of the Laplacian pyramid is obtained by taking the difference 
# b/W the corresponding level in the Gaussian pyramid and an upsampled and blurred version of the next level in the Gaussian pyrami

apple_c = gp_apple[5]
lp_apple = [apple_c]
for i in range(5, 0, -1):
    gaussian_exp = cv2.pyrUp(gp_apple[i])
    rows, cols, _ = gaussian_exp.shape
    gp_apple_i_minus_1_resized = cv2.resize(gp_apple[i - 1], (cols, rows))
    laplacian = cv2.subtract(gp_apple_i_minus_1_resized, gaussian_exp)
    lp_apple.append(laplacian)

# generate Laplacian pyramid for strawberry

strawb_c = gp_strawb[5]
lp_strawb = [strawb_c]
for i in range(5, 0, -1):
    gaussian_exp = cv2.pyrUp(gp_strawb[i])
    rows, cols, _ = gaussian_exp.shape
    gp_strawb_i_minus_1_resized = cv2.resize(gp_strawb[i - 1], (cols, rows))
    laplacian = cv2.subtract(gp_strawb_i_minus_1_resized, gaussian_exp)
    lp_strawb.append(laplacian)

# join left and right halves at each level

apple_strawb_pyramid = []
n = 0
for apple_lap, strawb_lap in zip(lp_apple, lp_strawb):
    n += 1
    rows, cols, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], strawb_lap[:, int(cols/2):]))
    apple_strawb_pyramid.append(laplacian)

# reconstruct the original image
apple_strawb_reconstruct = apple_strawb_pyramid[0]
for i in range(1, 6):
    apple_strawb_reconstruct = cv2.pyrUp(apple_strawb_reconstruct)
    apple_strawb_pyramid_i_resized = cv2.resize(apple_strawb_pyramid[i], apple_strawb_reconstruct.shape[:2][::-1])
    apple_strawb_reconstruct = cv2.add(apple_strawb_pyramid_i_resized, apple_strawb_reconstruct)

cv2.imshow('apple', apple)
cv2.imshow('strawberry', strawb)
cv2.imshow('apple_strawberry', apple_strawb)
cv2.imshow('strawberry_reconstructed', apple_strawb_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()


# import cv2
# import numpy as np

# apple = cv2.imread('apple.jpg')
# strawb = cv2.imread('strawberry.jpg')
# apple = cv2.resize(apple, (350, 350))
# strawb = cv2.resize(strawb, (350, 350))

# apple_strawb = np.hstack((apple[:, :175], strawb[:, 175:]))

# #gen gaussian pyramid apple

# apple_c = apple.copy()
# gp_apple = [apple_c]

# for i in range(6):
#     apple_c = cv2.pyrDown(apple_c)
#     gp_apple.append(apple_c)

# # gen gaussian pyramid strawberry

# strawb_c = strawb.copy()
# gp_strawb = [strawb_c]

# for i in range(6):
#     strawb_c = cv2.pyrDown(strawb_c)
#     gp_strawb.append(strawb_c)

# # gen laplacian pyramid apple

# apple_c = gp_apple[5]
# lp_apple = [apple_c]
# for i in range(5, 0, -1):
#     gaussian_exp = cv2.pyrUp(gp_apple[i])
#     laplacian = cv2.subtract(gp_apple[i - 1], gaussian_exp)
#     lp_apple.append(laplacian)

# # gen laplacian pyramid strawberry

# strawb_c = gp_strawb[5]
# lp_strawb = [strawb_c]
# for i in range(5, 0, -1):
#     gaussian_exp = cv2.pyrUp(gp_strawb[i])
#     laplacian = cv2.subtract(gp_strawb[i - 1], gaussian_exp)
#     lp_strawb.append(laplacian)

# # left and righ halves at each lvl

# apple_strawb_pyramid = []
# n = 0
# for apple_lap, strawb_lap in zip(lp_apple, lp_strawb):
#     n += 1
#     cols, rows, ch = apple_lap.shape
#     laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], strawb_lap[:, int(cols/2):]))
#     apple_strawb_pyramid.append(laplacian)

# # now reconstruct
# apple_strawb_reconstruct = apple_strawb_pyramid[0]
# for i in range(1, 6):
#     apple_strawb_reconstruct = cv2.pyrUp(apple_strawb_reconstruct)
#     apple_strawb_reconstruct = cv2.add(apple_strawb_pyramid[i], apple_strawb_reconstruct)

# cv2.imshow('apple', apple)
# cv2.imshow('strawberry', strawb)
# cv2.imshow('apple_strawberry', apple_strawb)
# cv2.imshow('strawberry', apple_strawb_reconstruct)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # need to load two images
# # find gaussian pyramids for each image
# # from gaussian find lapalacian
# # join left half of image with right half of other in each level of laplacian
# # reconstruct original image