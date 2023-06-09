import cv2
from matplotlib import pyplot as plt

# Intro practice to matplotlib

img = cv2.imread('CV-Practice-Image.png', -1)
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()