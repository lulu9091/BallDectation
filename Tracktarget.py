import cv2
import numpy as np
def Track():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    while(ret):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower_red = np.array([0,100,150])
        upper_red = np.array([50,255,240])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        cv2.imshow("frame", frame)
        cv2.imshow("mask",mask)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
