import cv2
import numpy as np
import os

img = cv2.imread(os.path.join("res", "messi.jpg"))
rows, cols = img.shape[:2]
mask = np.zeros((rows + 2, cols + 2), np.uint8)
new_val = (255, 255, 255)
lo_diff, up_diff = (2, 2, 2), (2, 2, 2)


def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        seed = (x, y)
        retval = cv2.floodFill(img, mask, seed, new_val, lo_diff, up_diff)
        cv2.imshow("img", img)


while True:
    cv2.imshow("img", img)
    cv2.setMouseCallback("img", onMouse)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
        

cv2.destroyAllWindows()
