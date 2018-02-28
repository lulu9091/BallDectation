import cv2
import numpy as np
def CaptureFrame():
    vidcap = cv2.VideoCapture("TestSample/cover.mp4")
    count = 0
    success,image = vidcap.read()
    while (success):
      cv2.imshow('Video',image)
      if cv2.waitKey(1) == ord('s'):
          cv2.imwrite("TestSample/frame%d.jpg" % count, image)
          count += 1   # save frame as JPEG file
      success,image = vidcap.read()
    vidcap.release()
    cv2.destroyAllWindows()
