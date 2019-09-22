import cv2
img=cv2.imread("G:/study/ani.jpg")
cv2.imshow("color_img",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayimg",gray)
cv2.waitKey(0)

#shape
r,c,ch=img.shape
print("row:{},col:{},channels:{}".format(r,c,ch))
