import cv2
cam=cv2.VideoCapture(0)
subtractor=cv2.createBackgroundSubtractorMOG2()
while True:
    ret,frame=cam.read()
    bw=subtractor.apply(frame)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",bw)
    if cv2.waitKey(3)==ord('a'):
        break
cam.release()
cv2.destroyAllWindows()
   
