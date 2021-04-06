import numpy as np
import cv2

img = cv2.imread('images/Atrium2.jpg')

# Lấy kích thước của ảnh
(h, w, d) = img.shape
print("width={}, height={}, depth={}".format(w, h, d))

# Lấy giá trị màu ở một điểm ảnh
(B, G, R) = img[50, 50]
print("R={}, G={}, B={}".format(R, G, B))

