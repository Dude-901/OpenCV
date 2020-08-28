import numpy as np
import cv2

img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img1.shape) # returns a tuple of number of rows and cols
print(img1.size) # returns total number of pixels
print(img1.dtype) # retuns image datatype

b, g, r = cv2.split(img1)
img1 = cv2.merge(b, g, r)

ball = img1[280:340, 330:390] # Region of interest(ROI)
img1[273:333, 100:160] = ball # copy paste like process

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img1, img2);
dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0);
cv2.imshow('image', dst)

cv2.waitkey(0)
cv2.destroyAllWindows()
