import cv2
import numpy as np

def wait():
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('./resources/test.png',img)
    cv2.destroyAllWindows()

imga = cv2.imread('./internet/quiz5_a.png', cv2.IMREAD_COLOR)
(h, w, d) = imga.shape
imga1 = imga[0:h, 0:int(w/2)]
imga2 = imga[0:h, int(w/2):w]

# cv2.imshow('Original Image', imga)
# cv2.imshow('A1', imga1)
# cv2.imshow('A2', imga2)
# wait()

imgb = cv2.imread('./internet/quiz5_b.jpg', cv2.IMREAD_COLOR)
(h, w, d) = imgb.shape
imgb1 = imgb[0:h, 0:int(w/2)]
imgb2 = imgb[0:h, int(w/2):w]

imga1b2 = np.concatenate((imga1, imgb2), axis=1)
imgb2a1 = np.concatenate((imgb2, imga1), axis=0)
cv2.imwrite('./images/quiz5_a.png',imga)
cv2.imwrite('./images/quiz5_b.png',imgb)
cv2.imwrite('./images/quiz5_a1b2.png',imga1b2)
cv2.imwrite('./images/quiz5_b2a1.png',imgb2a1)