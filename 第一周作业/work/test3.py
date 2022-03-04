import cv2 as cv
import numpy as np

img = cv.imread("picture/pic1.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("img", img)
cv.imshow("img_gray", img_gray)
cv.waitKey(0)
cv.destroyAllWindows()