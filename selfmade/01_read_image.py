import cv2
import requests
import numpy as np

"""
Intensity(brightness): 픽셀의 값이자 밝기
0: black
255: white
1.0: white
"""
url = "https://raw.githubusercontent.com/dsaint31x/OpenCV_Python_Tutorial/master/DIP/img/opencv_logo.png"
image_ndarray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
img = cv2.imdecode(image_ndarray, cv2.IMREAD_UNCHANGED)
cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
