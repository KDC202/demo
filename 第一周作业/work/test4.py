import cv2 as cv
import numpy as np

img = cv.imread("picture/pic1.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh1 = cv.threshold(img_gray, 100, 255, cv.THRESH_TOZERO_INV)
cv.imshow("img", img)
cv.imshow("thresh1", thresh1)
cv.waitKey(0)
cv.destroyAllWindows()