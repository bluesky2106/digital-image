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
# img = cv2.imread('./images/j.png', cv2.IMREAD_UNCHANGED)

# img_gray = cv2.imread('./images/image001.jpg', cv2.IMREAD_GRAYSCALE)
# (thresh, img) = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

img = cv2.imread('./images/image001.jpg', cv2.IMREAD_GRAYSCALE)

se1 = np.ones((3,3),np.uint8)
se2 = np.ones((1,7),np.uint8)
se3 = np.ones((7,1),np.uint8)
dilation1 = cv2.dilate(img,se1,iterations = 1)
dilation2 = cv2.dilate(img,se2,iterations = 1)
dilation3 = cv2.dilate(img,se3,iterations = 1)
erosion1 = cv2.erode(img,se1,iterations = 1)
erosion2 = cv2.erode(img,se2,iterations = 1)
erosion3 = cv2.erode(img,se3,iterations = 1)
opening1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, se1)
closing1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, se1)


cv2.imshow('Original Image', img)
cv2.imshow('Dilation 3x3 Image', dilation1)
cv2.imshow('Dilation 1x7 Image', dilation2)
cv2.imshow('Dilation 7x1 Image', dilation3)
cv2.imshow('Erosion 3x3 Image', erosion1)
cv2.imshow('Erosion 1x7 Image', erosion2)
cv2.imshow('Erosion 7x1 Image', erosion3)
cv2.imshow('Opening 3x3 Image', opening1)
cv2.imshow('Closing 3x3 Image', closing1)

cv2.imwrite('./images/tut1_origin.png',img)
cv2.imwrite('./images/tut1_dilation1_3x3.png',dilation1)
cv2.imwrite('./images/tut1_dilation2_1x7.png',dilation2)
cv2.imwrite('./images/tut1_dilation3_7x1.png',dilation3)
cv2.imwrite('./images/tut1_erosion1_3x3.png',erosion1)
cv2.imwrite('./images/tut1_erosion2_1x7.png',erosion2)
cv2.imwrite('./images/tut1_erosion3_7x1.png',erosion3)
cv2.imwrite('./images/tut1_opening1_3x3.png',opening1)
cv2.imwrite('./images/tut1_closing1_3x3.png',closing1)

wait()