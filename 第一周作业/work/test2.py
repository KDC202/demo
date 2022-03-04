import cv2 as cv
import numpy as np

img = np.zeros((600, 800, 3), np.uint8)
i = 0
j = 0
k = True
while i < 600:
    while j < 800:
        if k:
            img[i:i + 29, j:j + 39, 2] = 255
        else:
            img[i:i + 29, j:j + 39, 0] = 255
        k = not k
        j += 40
    k = not k
    j = 0
    i += 30
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()