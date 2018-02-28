import numpy as np
from tkinter import *
from tkinter import filedialog
import cv2
def RGBtoHSV():
	path = filedialog.askopenfilename()
	img = cv2.imread(path)
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	lower_red = np.array([0,100,150])
	upper_red = np.array([50,255,240])
	mask = cv2.inRange(hsv, lower_red, upper_red)
	while(1):
		cv2.imshow('hsv',hsv)
		cv2.imshow('original',img)
		cv2.imshow('mask',mask)
		if cv2.waitKey(0) == ord('q'):
			break
	cv2.destroyAllWindows()
