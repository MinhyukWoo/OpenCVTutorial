import cv2 as cv
import numpy as np
import os

img = cv.imread(os.path.join("res", "aloe.jpg"))
img = cv.resize(img, (img.shape[1] // 4, img.shape[0] // 4))

replicated_img = cv.copyMakeBorder(img, 40, 40, 40, 40, cv.BORDER_REPLICATE)

# like this : fedcba|abcdefgh|hgfedcb
reflected_img = cv.copyMakeBorder(img, 40, 40, 40, 40, cv.BORDER_REFLECT)
# cv.rectangle(
#     reflected_img,
#     (40, 40),
#     (reflected_img.shape[1] - 40, reflected_img.shape[0] - 40),
#     (0, 0, 255),
#     1,
# )

# like this : gfedcb|abcdefgh|gfedcba
reflected101_img = cv.copyMakeBorder(img, 40, 40, 40, 40, cv.BORDER_REFLECT_101)

wrapped_img = cv.copyMakeBorder(img, 40, 40, 40, 40, cv.BORDER_WRAP)

constant_img = cv.copyMakeBorder(
    img, 40, 40, 40, 40, cv.BORDER_CONSTANT, value=(255, 0, 0)
)

while 1:
    cv.imshow("aloe", img)
    cv.imshow("replicated", replicated_img)
    cv.imshow("reflected", reflected_img)
    cv.imshow("reflected101", reflected101_img)
    cv.imshow("wrapped", wrapped_img)
    cv.imshow("constant", constant_img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows()
