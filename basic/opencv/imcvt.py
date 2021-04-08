import cv2
import numpy as np
import utils

img = cv2.imread('./images/fpt.png', cv2.IMREAD_UNCHANGED)
# print("origin image data type:", str(img.dtype))
# print_image_pixel(img)

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("img1 data type:", str(img1.dtype))

# cvuint8 = cv2.convertScaleAbs(img)
# print("uint8 image data type:", str(cvuint8.dtype))

# cv2.imshow('original image',img)
# cv2.imshow('uint8 image',cvuint8)

# utils.wait()

def print_image_pixel(img):
  (h, w, d) = img.shape
  print("width={}, height={}, depth={}".format(w, h, d))
  for c in range(w):
    for r in range(h):
      tmp = img[r, c][0]
      img[r, c][0] = img[r, c][2]
      img[r, c][2] = tmp
      print(img[r, c])