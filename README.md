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

### Convert video feed to grayscale:  
```python
capture = cv2.VideoCapture(0);
while capture.isOpened():
    ret, frames = capture.read()
    if ret:
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cv2.imshow('feed', gray)
    else:
        break
```

### Record video:  
```python
capture = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc code
out = cv2.VideoWriter('record.avi', fourcc, 20.0, (640, 480))
# 'record.avi' => video file name, 20.0 is the frame-rate and (640,480) is the width-height tuple
while capture.isOpened():
    ret, frames = capture.read()
    if ret:
        out.write(frames)
    else:
        break
```

### Read and set image properties:  
```python
print(capture.get(3)) # print width of frame
# cv2.CAP_PROP_FRAME_WIDTH = 3
print(capture.get(4)) # print height of frame
# cv2.CAP_PROP_FRAME_HEIGHT = 4

capture.set(3, 1200) # => wil change to available default value i.e. 1280
capture.set(4, 720) # => remain same 
```

### Draw or Write on image:  
```python
img = cv2.line(img, (0,0), (200,200), (227, 30, 112), 10) # simple line
img = cv2.arrowedLine(img, (200,0), (200,200), (0, 70, 255), 10) # arrowed line

img = cv2.rectangle(img, (200,300), (400,500), (227, 230, 112), 10) # rectangle
img = cv2.circle(img, (300,400), 100, (0, 130, 112), -1) # circle
# thickness = -1: means a solid filled color shape

font = cv2.FONT_HERSHEY_SIMPLEX # font-style for the text
img = cv2.putText(img, 'Dude', (200, 163), font, 4, (255,255,255), 5, cv2.LINE_4) # text on image
```

### create a black image:  
```python
img = np.zeros([512, 512, 3], np.uint8) # (height, width, 3), data_type
```

