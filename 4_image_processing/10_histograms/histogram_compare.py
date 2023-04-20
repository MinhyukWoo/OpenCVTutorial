import cv2
from os import path


def get_histogram(img_path):
    img = cv2.imread(img_path)
    hsv_image = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    channels = (0, 1)
    h_range = (0, 180)
    s_range = (0, 256)
    hist_size = (180, 256)
    hist = cv2.calcHist([hsv_image], channels, None, hist_size, h_range + s_range)
    noralized_hist = cv2.normalize(hist, 0, 1, cv2.NORM_MINMAX)
    return noralized_hist


img_names = ["sample1.jpg", "sample2.jpg", "sample3.jpg"]
img_paths = [path.join("res", img_name) for img_name in img_names]
hists = [get_histogram(img_path) for img_path in img_paths]

for method, method_name in [
    (cv2.HISTCMP_CORREL, "cv2.HISTCMP_CORREL"),
    (cv2.HISTCMP_CHISQR, "cv2.HISTCMP_CHISQR"),
    (cv2.HISTCMP_INTERSECT, "cv2.HISTCMP_INTERSECT"),
    (cv2.HISTCMP_KL_DIV, "cv2.HISTCMP_KL_DIV"),
    (cv2.HISTCMP_BHATTACHARYYA, "cv2.HISTCMP_BHATTACHARYYA"),
]:
    main_hist = hists[0]
    outs = [cv2.compareHist(main_hist, hist, method) for hist in hists]
    print(method_name)
    print(f"sample1 & sample1: {outs[0]}")
    print(f"sample1 & sample2: {outs[1]}")
    print(f"sample1 & sample3: {outs[2]}")
    print()
