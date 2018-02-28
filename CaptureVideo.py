import cv2
def captureVideo():
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter("TestSample/cover.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 10.0, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)))
    while(True):
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow("frame", frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    fps = cap.get(cv2.CAP_PROP_FPS);
    print(1/fps)
    out.release()
    cap.release()
    cv2.destroyAllWindows()
