import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('coins.jpg')
imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thrash = cv.threshold(imgGrey, 90, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# cv.drawContours(img, contours, -1, 200, 3)
c = max(contours, key=cv.contourArea)
x, y, w, h = cv.boundingRect(c)
cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()
