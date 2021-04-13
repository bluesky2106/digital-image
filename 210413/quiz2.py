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

def gamma_correct(c, gamma):
  img = cv2.imread('./images/origin.jpg', cv2.IMREAD_UNCHANGED)
  new_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # for y in range(img.shape[0]):
  #   for x in range(img.shape[1]):
  #     new_image[y,x] = np.clip(c*img[y,x] + gamma, 0, 255)
  new_image[:,:] = np.clip(c*new_image[:,:] ** gamma, 0, 255)
  return new_image

# origin image
img = cv2.imread('./images/origin.jpg', cv2.IMREAD_UNCHANGED)

# origin gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

c = 1.0
gamma1 = 0.2
gamma2 = 1
gamma3 = 5

gImg1 = gamma_correct(c, gamma1)
gImg2 = gamma_correct(c, gamma2)
gImg3 = gamma_correct(c, gamma3)


# cv2.imshow('Original Image', img)
# cv2.imshow('Original Gray Image', gray)
cv2.imshow('Gamma = 0.2', gImg1)
cv2.imshow('Gamma = 1', gImg2)
cv2.imshow('Gamma = 5', gImg3)



wait()