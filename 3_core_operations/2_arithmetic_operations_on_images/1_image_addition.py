import cv2 as cv
import numpy as np
import os

img1 = cv.imread(os.path.join("res", "aloe.jpg"))
img2 = cv.imread(os.path.join("res", "messi.jpg"))
img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))
img3 = cv.addWeighted(img1, 0.3, img2, 0.7, 0)

while 1:
    cv.imshow("img3", img3)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break
cv.destroyAllWindows()
