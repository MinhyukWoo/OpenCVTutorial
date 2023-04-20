import cv2
import numpy as np
from os import path

img = cv2.imread(path.join("res", "sudoku.jpg"))
print(img.dtype)
cv2.imshow("filter", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
