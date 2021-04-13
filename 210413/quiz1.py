import numpy as np
import matplotlib.pyplot as plt
import cv2

def wait():
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('./resources/test.png',img)
    cv2.destroyAllWindows()


# origin image
img = cv2.imread('./images/origin.jpg', cv2.IMREAD_UNCHANGED)

# origin gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


# cv2.imshow('Original Image', img)
# cv2.imshow('Original Gray Image', gray)
# cv2.imshow('Threshold Image', thresh)

cv2.imwrite('./images/quiz1_origin_gray.png',gray)
cv2.imwrite('./images/quiz1_thresshold_05.png',thresh)


wait()