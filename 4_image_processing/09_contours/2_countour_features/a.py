import cv2
import numpy as np


img = np.zeros((64, 64, 3), np.uint8)
img = cv2.ellipse(img, (32, 32), (10, 15), 30, 0, 360, (255, 0, 0), -1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
x, y, w, h = cv2.boundingRect(contours[0])
img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0))

cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
