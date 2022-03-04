import cv2 as cv
import numpy as np

img = np.zeros((600, 800, 3), np.uint8)
img[:, :, 2] = 255
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
