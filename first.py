import cv2

img = cv2.imread('lena.jpg',1)
# print(img)
cv2.imshow('image', img)

button = cv2.waitKey(0) 

if button == 27: # press esc key
    cv2.destroyAllWindows()
elif button == ord('s'): # press 's' key
    cv2.imwrite('img_copy.png', img)
    cv2.destroyAllWindows()
