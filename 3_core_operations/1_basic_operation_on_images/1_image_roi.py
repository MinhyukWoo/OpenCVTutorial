import numpy as np
import cv2 as cv
import os


img = cv.imread(os.path.join("res", "messi.jpg"))
img = cv.resize(img, (img.shape[1] // 4, img.shape[0] // 4))
ball_img = img[431:498, 522:594]
img[431:498, 272:344] = ball_img
while 1:
    cv.imshow("messi", img)
    cv.imshow("ball", ball_img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break
cv.destroyAllWindows()
