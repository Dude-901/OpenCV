import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("lena.jpg")

b, g, r = cv.split(img)
img = cv.imread("lena.jpg", 0)
cv.imshow('image',img)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
