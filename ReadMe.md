#ReadMe
---    
Start the program by running main.py. This app provide a small menus for user to select the task.
This software have multiple functions below:
1.  Turn on the webCam and save a range of time stream in the local disk. By pressing 'q', user can end the record and save the video
2.  Capture Frame from this save video and calculate the time for capturing each frame and output in the console. Press 's' to save the frame user want to save.
3.  Convert the colorspace from RGB to HSV by using openCV build-in function and the function write by myself.
4.  Track the yellow cap by using openCV build-in color detection function in the realtime and mark the colored area as white in dark background.
5.  Add salt& pepper noise on one of the captured frame by the density 0.02
6. Remove the noise and output the noise-removed image to local disk by using medianBlur function.
