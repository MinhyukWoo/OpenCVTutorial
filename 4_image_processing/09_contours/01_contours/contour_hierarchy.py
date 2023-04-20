import cv2
import numpy as np


def get_image():
    img = np.zeros((256, 256, 3), np.uint8)
    img = cv2.line(img, (10, 10), (90, 10), (255, 255, 255), 1)
    img = cv2.line(img, (100, 20), (210, 20), (255, 255, 255), 4)
    img = cv2.rectangle(img, (16, 100), (240, 240), (255, 255, 255), 1)
    img = cv2.rectangle(img, (32, 116), (224, 224), (255, 255, 255), 1)
    img = cv2.rectangle(img, (48, 132), (80, 208), (255, 255, 255), -1)
    img = cv2.rectangle(img, (112, 164), (144, 196), (255, 255, 255), -1)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img

img = get_image()
cv2.imshow("contour hierarchy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
