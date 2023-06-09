import cv2
import numpy as np
from matplotlib import pyplot as plt

# canny edge detection has less noise than the image gradients

img = cv2.imread("CV-Practice-Image.png", 0)
canny = cv2.Canny(img, 100, 200) # needs two threshold values for the edges... a trackbar to track changes isnt a bad idea

titles = ['image', 'canny']
images = [img, canny]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray') # 1 by 2 display of images
    plt.title(titles[i]) # increments titles array
    plt.xticks([]), plt.yticks([]) # gets rid of graphs ticks

plt.show()


# canny edge detector multi stage algo that detects wide range of edges
# canny edge detection has five steps: 1 noise reduction 2 gradient calc 3 non max suppression 4 double threshold 5 edge tracking by hysteresis