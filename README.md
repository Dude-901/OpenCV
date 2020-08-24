# OpenCV
My OpenCV learning notes and examples  
Enter in command line:  
>pip install opencv-python  

check version:  
>cv2.\_\_version\_\_  

Read image:
```python
img = cv2.imread('image_name.jpg/jpeg/png',flag)
```
flag | integer value | description
----- | ------------ | -----------
cv2.IMREAD_COLOR | 1 | Loads a color image
cv2.IMREAD_GREYSCALE | 0 | Loads image in greyscale mode
cv2.IMREAD_UNCHANGED | -1 | Loads an image as it is including alpha channel

Image output:  
```python
print(img) # prints image pixels in array format
cv2.imshow('image', img) # image output
cv2.waitKey(0) # wait time before closing image window
# waitKey(0) means image won't close after any time by itself.
cv2.destroyAllWindows() # destroy all created windows
```
