import cv2
import numpy as np
from tkinter import filedialog
def SelfRGBTOHSV():
    path = filedialog.askopenfilename()
    img = cv2.imread(path)
    imgout = cv2.imread(path)
    b,g,r = cv2.split(img)
    b = b / 255
    g = g / 255
    r = r / 255
    for i in range (0, img.shape[0]):
        for j in range(0, img.shape[1]):
            be = b[i][j]
            ge = g[i][j]
            re = r[i][j]
            maxn = max(re,ge,be)
            minn = min(re,ge,be)
            delt = maxn - minn

            if maxn == minn:
                h =0
            elif maxn == re:
                h = (60 * ((ge - be) / delt) + 360) % 360
            elif maxn == ge:
                h = (60 * ((be - re) / delt) + 120) % 360
            elif maxn == be:
                h = (60 * ((re - ge) / delt) + 240) % 360
            if maxn == 0:
                s = 0
            else :
                s = delt/maxn
            v = maxn
            imgout[i][j][0] = np.round(h / 2)
            imgout[i][j][1] = np.round(255 * s)
            imgout[i][j][2] = np.round(255 * v)
    cv2.imwrite("covertedimage.jpg", imgout)
