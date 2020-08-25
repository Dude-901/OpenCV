# OpenCV
My OpenCV learning notes and examples  
### Enter in command line:  
>pip install opencv-python  

### check version:  
>cv2.\_\_version\_\_  

### Read image:
```python
img = cv2.imread('image_name.jpg/jpeg/png',flag)
```

flag | integer value | description
----- | ------------ | -----------
cv2.IMREAD_COLOR | 1 | Loads a color image
cv2.IMREAD_GREYSCALE | 0 | Loads image in greyscale mode
cv2.IMREAD_UNCHANGED | -1 | Loads an image as it is including alpha channel

### Image output:  
```python
print(img) # prints image pixels in array format
cv2.imshow('image', img) # image output
cv2.waitKey(0) # wait time before closing image window
# waitKey(0) means image won't close after any time by itself.
cv2.destroyAllWindows() # destroy all created windows
```

### Write a new image:
```python
cv2.imwrite('new_img.jpg', img)
# new_img.jpg => name of the new file that you want to create aling with the desirable extension
# second argument is the variable name in which the original image was loaded earlier.
```

### Record video:  
```python
capture = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc code
out = cv2.VideoWriter('record.avi', fourcc, 20.0, (640, 480))
# 'record.avi' iis the created video file name, 20.0 is the frame-rate and (640,480) is the width-height tuple
while capture.isOpened():
    ret, frames = capture.read()
    if ret:
        out.write(frames)
```
