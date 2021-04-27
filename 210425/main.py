import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def wait():
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('./resources/test.png',img)
    cv2.destroyAllWindows()

def compression():
  path = './images/coat_of_arms.jpg'
  fileSize = os.path.getsize(path)
  print(fileSize)

  # stat = os.stat(path)
  # print(stat)

  img = cv2.imread(path)
  # is_success, im_buf_arr = cv2.imencode(".jpg", img)
  # imageSize = im_buf_arr.tobytes()
  (w, h, d) = img.shape
  print(w, h, d)

  imageSize = w * h * d
  CR = imageSize / fileSize
  print(CR)

# compression()

def save_compression():
  path = './images/statue.jpeg'
  img = cv2.imread(path)

  cv2.imwrite('./images/statue50.jpg',img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
  cv2.imwrite('./images/statue10.jpg',img, [int(cv2.IMWRITE_JPEG_QUALITY), 10])

save_compression()
