import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("CV-Practice-Image.png", cv2.IMREAD_GRAYSCALE)
# can add third parameter to laplacian in the format ksize = _ which will increase kernel size
lap = cv2.Laplacian(img, cv2.CV_64F) #64f is a data type for 64 bit float supporting neg nums in laplacian method
lap = np.uint8(np.absolute(lap)) # converts to unsined 8 bit integer
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) # 1 (dx val) is sobelX method 0 is dy direction
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1) # can have another argument for k size like in laplacian

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelC']
images = [img, lap, sobelX, sobelY, sobelCombined]
for i in range(5):
    plt.subplot(3, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# an image gradien is a directional change in the intensity or color of an image
# Laplacian helps highlight edges in a black/white image

# sobel X changes intensity in x direction
# sobel Y changes intensity in y direction