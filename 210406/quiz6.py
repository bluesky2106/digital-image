import cv2
import numpy as np

def wait():
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('./resources/test.png',img)
    cv2.destroyAllWindows()

def resize(img, w, h):
  dim = (w, h)
  resized = cv2.resize(img, dim)
  return resized

w = 1080
h = 1920

img1 = cv2.imread('./internet/quiz6_1.jpeg', cv2.IMREAD_COLOR)
img1 = resize(img1, int(w/2), int(h/2))
img2 = cv2.imread('./internet/quiz6_2.jpeg', cv2.IMREAD_COLOR)
img2 = resize(img2, int(w/2), int(h/2))

img3 = cv2.imread('./internet/quiz6_3.jpeg', cv2.IMREAD_COLOR)
img3 = resize(img3, int(w/2), int(h/2))
img4 = cv2.imread('./internet/quiz6_4.jpeg', cv2.IMREAD_COLOR)
img4 = resize(img4, int(w/2), int(h/2))

img12 = np.concatenate((img1, img2), axis=1)
img34 = np.concatenate((img3, img4), axis=1)
img1234 = np.concatenate((img12, img34), axis=0)

cv2.imwrite('./images/quiz6_1.png',img1)
cv2.imwrite('./images/quiz6_2.png',img2)
cv2.imwrite('./images/quiz6_3.png',img3)
cv2.imwrite('./images/quiz6_4.png',img4)
cv2.imwrite('./images/quiz6_1234.png',img1234)