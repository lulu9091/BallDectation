import cv2
import numpy as np
from tkinter import filedialog
import random as random
def sp_noise():
# '''
# Add salt and pepper noise to image
# prob: Probability of the noise
# '''
    path = filedialog.askopenfilename()
    image = cv2.imread(path)
    shape = [image.shape[0],image.shape[1]]
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - 0.02
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < 0.02:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    while(1):
        cv2.imshow('noise',output)

        if cv2.waitKey(1) == ord('q'):
            break
    cv2.imwrite('TestSample/N2.jpg', output)
    cv2.destroyAllWindows()
# image = cv2.imread('TestSample/frame106.jpg',0) # Only for grayscale image
# noise_img = sp_noise(img,0.02)
