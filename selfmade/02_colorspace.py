import cv2
import numpy as np
import os

"""
Intensity(brightness): 픽셀의 값이자 밝기
0: black
255: white
1.0: white
"""

imgs = {}
imgs["img_default"] = cv2.imread(os.path.join("res", "opencv_logo.png"))
imgs["img_bgr"] = cv2.imread(os.path.join("res", "opencv_logo.png"), cv2.IMREAD_COLOR)
imgs["img_bgra"] = cv2.imread(
    os.path.join("res", "opencv_logo.png"), cv2.IMREAD_UNCHANGED
)
imgs["img_gray"] = cv2.imread(
    os.path.join("res", "opencv_logo.png"), cv2.IMREAD_GRAYSCALE
)

for idx, key in enumerate(imgs):
    print(f"{key}: {imgs[key].shape}")
    cv2.imshow(f"{key}", imgs[key])
print(np.min(imgs["img_bgra"][:, :, -1]), np.max(imgs["img_bgra"][:, :, -1]))
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
img_default: (120, 98, 3)
img_bgr: (120, 98, 3)
img_bgra: (120, 98, 4)
img_gray: (120, 98)
"""
print(np.unique(imgs["img_bgra"][:, :, -1].ravel(), return_counts=True))
'''
주로 0,255 의 값을 가지나 경계상에서의 이들 사이의 값이 존재하는 것을 확인 가능함.
'''