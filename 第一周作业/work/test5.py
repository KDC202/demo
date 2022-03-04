import cv2 as cv
import numpy as np

img = cv.imread("picture/pic1.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
i = 0
j = 0
for i in range(len(img_gray)):
    for j in range(len(img_gray[0])):
        if img_gray[i, j] < 100:
            img[i, j, 0] = 255
            img[i, j, 1] = 0
            img[i, j, 2] = 0
        else:
            img[i, j, 0] = 0
            img[i, j, 1] = 0
            img[i, j, 2] = 255

cv.imshow("img", img)
cv.imshow("img_gray", img_gray)
cv.waitKey(0)
cv.destroyAllWindows()
