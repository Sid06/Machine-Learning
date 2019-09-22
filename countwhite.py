import cv2
import numpy as np

img = cv2.imread('G:/study/ani.jpg', cv2.IMREAD_GRAYSCALE)
r,c=img.shape
count=0
#img=np.array(img)
for i in range(r):
    for j in range(c):
        print(img[i,j])
 #       if img[i,j]==255:
           # count+=1     

"""print('Number of white pixels:', count)
# another method 
n_white_pix = np.sum(img == 255)
print('Number of white pixels:',n_white_pix)"""