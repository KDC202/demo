import cv2 as cv
import numpy as np

mask = np.zeros((600, 800, 3), np.uint8)
cv.rectangle(mask, (360, 270), (440, 330), (255, 255, 255), -1)

img = cv.imread("picture/pic1.jpg")
img = cv.resize(img, (800, 600))
img = cv.bitwise_and(img, mask)
for i in range(len(img)):
    for j in range(len(img[0])):
        if img[i, j, 0] == 0 & img[i, j, 1] == 0 & img[i, j, 2] == 0:
            img[i,j,1] = 255
cv.imshow("img", img)

cv.waitKey(0)
cv.destroyAllWindows()
