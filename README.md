# OpenCV
My OpenCV learning notes and examples  
Enter in command line:  
>pip install opencv-python  

check version:  
>cv2.__version__  

Read image:
>cv2.imread(img,flag)

flag | integer value | description
----- | ------------ | -----------
cv2.IMREAD_COLOR | 1 | Loads a color image
cv2.IMREAD_GREYSCALE | 0 | Loads image in greyscale mode
cv2.IMREAD_UNCHANGED | -1 | Loads an image as it is including alpha channel
