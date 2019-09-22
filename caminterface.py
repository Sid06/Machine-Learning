import cv2
cam=cv2.VideoCapture(0)
while True:
 """   ret,frame=cam.read()
    r,c,ch=frame.shape
    x=int(r/2)
    y=int(c/2)
    cv2.rectangle(frame,(200,200),(100,100),(185,128,4),3)
    cv2.circle(frame,(y,x),10,(185,128,4),-1)
    cv2.imshow("img",frame)
# or we can use if cv2.waitKey(3)&0xFF==ord('q'):
    if cv2.waitKey(3)==ord('a'):
        break"""
cam.release()
cv2.destroyAllWindows()
