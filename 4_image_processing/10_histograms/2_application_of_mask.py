import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

img = cv.imread(os.path.join("res", "lena.jpg"))
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:200, 100:200] = 255
hist = cv.calcHist([img], [0], mask, [256], [0, 256])
masked_img = cv.bitwise_and(img, img, mask=mask)

cv.imshow("img", img)
cv.imshow("masked_img", masked_img)
plt.plot(hist)
plt.show()

cv.destroyAllWindows()
