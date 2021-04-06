# https://github.com/kyatou/python-opencv_tutorial/blob/master/08_image_encode_decode.py

import cv2
import utils

img = cv2.imread('./images/fpt.png', cv2.IMREAD_UNCHANGED)

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 95]
result, encimg = cv2.imencode('.jpg', img, encode_param)
if False==result:
  print('could not encode image!')
  quit()

#decode from jpeg format
decimg=cv2.imdecode(encimg,1)

cv2.imshow('Source Image',img)
cv2.imshow('Decoded image',decimg)

utils.wait()