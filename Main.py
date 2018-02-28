from tkinter import *
import CaptureVideo as cp
import CaptureFrame as cf
import RGBTOHSV as rh
import Tracktarget as tt
import Addnoise as an
import remove as rm
import SelfRGBTOHSV as srh
import cv2
root = Tk()
root.title("Menus")
root.minsize(width=100,height=300)
b = Button(root, text="CaptrueVideo", command=cp.captureVideo)
b.place(x=0,y= 0)
cf = Button(root,text = "CaptureFrame", command = cf.CaptureFrame)
cf.place(x=0,y = 20)
rh = Button(root,text = "BGRtoHSV",command = rh.RGBtoHSV)
rh.place(x=0,y = 40)
srh = Button(root,text = "SElfBGRtoHSV",command = srh.SelfRGBTOHSV)
srh.place(x=0, y =60)
trac = Button(root, text ="Track", command =tt.Track)
trac.place(x=0,y=80)
noise = Button(root, text="AddNoise", command=an.sp_noise)
noise.place(x = 0,y =100)
remove = Button(root,text = "removeNoise",command = rm.remove)
remove.place(x = 0,y = 120)
exit = Button(root, text="QUIT", command=root.quit)
exit.place(x = 0,y =140)
mainloop()
