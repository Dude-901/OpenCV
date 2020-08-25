import cv2

capture = cv2.VideoCapture(0);
# cv2.VideoCapture() takes argument which is the source of its feed
# like you can give 'video.avi' or 'video.mp4' as its argument to play that particular video (along with path)
# or you can give your camera device as input which is usually 0 or -1
# if more than one cameras are connected, you can give arguments like 1 or 2
# for whichever device you want to take feed from.

fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc code
# http://www.fourcc.org/codecs.php
out = cv2.VideoWriter('record.avi', fourcc, 20.0, (640, 480))
# 20.0 is the frame-rate and (640,480) is the width-height tuple

while capture.isOpened(): # check if the capture is returning True
    # if the path of video or camera device name is wrong, it will give False
    
    ret, frames = capture.read()
    # 'ret' will check if capture.read() is returning True or False
    # 'frame' will read the value from the feed

    if ret:
        # print(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) # print width of frame
        # print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) # print height of frame
        # https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) # convert to grayscale
        # if you want to alter your feed's color properties, this is the way

        out.write(frames) # store the colored frames

        cv2.imshow('feed', gray)
        # second argument will be the one you want to show as output
        # in this case 'frame' for original feed and 'gray' for grayscale feed

        if cv2.waitKey(1) & 0xFF == ord('q'): # to quit feed, the key 'q' is to be pressed.
            break
            # break out of the loop as soon as 'q' is pressed
    else:
        break

capture.release()
# release all the recorded frames
cv2.destroyAllWindows()
