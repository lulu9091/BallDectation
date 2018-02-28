import cv2
import numpy as np
from tkinter import filedialog
def remove():
    path = filedialog.askopenfilename()
    img = cv2.imread(path)
    res =cv2.medianBlur(img, 3)
    while (1):
        cv2.imshow('remove_image',res)

        if cv2.waitKey(1) == ord('q'):
            break
    cv2.imwrite('TestSample/H2.jpg', res)
    cv2.destroyAllWindows()
