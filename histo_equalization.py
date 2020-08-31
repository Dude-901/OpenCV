import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('over.jpg', 0)
equ = cv.equalizeHist(img)
# cv.imshow('equalization', equ)

titles = ['over exposed image', 'after equalization']
images = [img, equ]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
