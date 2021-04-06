import numpy as np
import cv2

def wait():
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('./resources/test.png',img)
    cv2.destroyAllWindows()

def crop():
  img = cv2.imread('images/Atrium2.jpg')
  cv2.imshow('Original Image', img)

  # Cắt ảnh: Đoạn lệnh sau cắt ảnh có tọa độ điểm trên cùng bên trái là (50, 60) và tọa độ điểm dưới cùng bên phải là (350, 360).
  roi = img[50:350, 60:360]
  cv2.imshow('Region Of Interest', roi)
  wait()

# crop()

def resize():
  img = cv2.imread('images/Atrium2.jpg')
  cv2.imshow('Original Image', img)

  (h, w, d) = img.shape
  r = 300.0 / w
  dim = (300, int(h * r))
  resized = cv2.resize(img, dim)
  cv2.imshow('Resized Image', resized)
  wait()

# resize()

def rotate():
  img = cv2.imread('images/Atrium2.jpg')
  cv2.imshow('Original Image', img)

  (h, w, d) = img.shape 
  center = (w / 2, h / 2) 
  M = cv2.getRotationMatrix2D(center, 45, 1.0) 
  rotated = cv2.warpAffine(img, M, (w, h))
  cv2.imshow('Rotated Image', rotated)
  wait()

rotate()