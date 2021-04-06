import numpy as np
import cv2
import utils

# Load an color image in grayscale
img1 = cv2.imread('./images/fpt.png', cv2.IMREAD_UNCHANGED)
cv2.imshow('original image',img1)
print("origin image data type:", str(img1.dtype))

img2 = cv2.imread('./images/fpt.png', cv2.IMREAD_COLOR)
cv2.imshow('color image',img2)
print("color image data type:", str(img2.dtype))

img3 = cv2.imread('./images/fpt.png', cv2.IMREAD_GRAYSCALE)
print("gray image data type:", str(img3.dtype))
(h, w) = img3.shape
for c in range(w):
  for r in range(h):
    img3[img3 > 100] = 255
    img3[img3 < 50] = 0
cv2.imshow('gray image',img3)

utils.wait()