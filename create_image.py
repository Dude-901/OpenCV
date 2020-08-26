import cv2
import numpy as np

img = np.zeros([512, 512, 3], np.uint8) # (height, width, 3), data_type
img = cv2.line(img, (0,0), (200,200), (227, 30, 112), 10)
img = cv2.arrowedLine(img, (200,0), (200,200), (0, 70, 255), 10)

img = cv2.rectangle(img, (200,300), (400,500), (227, 230, 112), 10)
img = cv2.circle(img, (300,400), 100, (0, 130, 112), -1) # thickness = -1: means a solid filled color shape

font = cv2.FONT_HERSHEY_SIMPLEX # font for the text
img = cv2.putText(img, 'Dude', (200, 163), font, 4, (255,255,255), 5, cv2.LINE_4)

cv2.imshow('image', img)

button = cv2.waitKey(0) & 0xFF

if button == 27:
    cv2.destroyAllWindows()
