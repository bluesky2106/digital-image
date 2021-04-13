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

# negative
negative = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
negative[:] = 255 - negative[:]

# log
c = 255.0 / np.log(256)
logi = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
logi[:] = c * np.log(1 + logi[:])

# exp


# increase bright
value = 100
lim = 255 - value
  
add = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
add[add > lim] = 255
add[add <= lim] += value

cv2.imshow('Original Image', img)
cv2.imshow('Original Gray Image', gray)
cv2.imshow('Negative Transform', negative)
cv2.imshow('Log Transform', logi)
cv2.imshow('Add Transform', add)



wait()