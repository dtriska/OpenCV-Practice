import cv2
import numpy as np
from matplotlib import pyplot as plt

# uses a few diff blurs

img = cv2.imread('CV-Practice-Image.png', -1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)
bf = cv2.bilateralFilter(img, 9, 75, 75)
# median must have odd size that isn't 1
median = cv2.medianBlur(img, 5)

titles = ['image', '2D Convolution', 'blur', 'gblur', 'median', 'bf']
images = [img, dst, blur, gblur, median, bf]

for i in range(6):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray') # subplot 1, 2, i+1 means we want it to be displayed in 1 by 2 format
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# LPF helps in removing noises, blurring the images
# HPF filters helps in finding eges in images

# gaussian filter uses nothing but different weight kernels in both x and y direction
# neighborhood center has greatest weight -> outised is lower *gblur var

# median filter is something that replaces each pixels val with the median of its neighbors
# great for "salt and pepper noise"

# bilateral filter is great for blurring while preserving sharp edges