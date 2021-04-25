import cv2
import numpy as np
import matplotlib.pyplot as plt

def wait():
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('./resources/test.png',img)
    cv2.destroyAllWindows()

img = cv2.imread('./images/coins.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# global thresholding
T = 85
th1,ret1 = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)
# Otsu's thresholding
th2,ret2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


plt.subplot(2,2,1)
plt.title('Origin Gray Image', fontweight ="bold")
plt.imshow(gray, cmap ="binary_r", interpolation ='nearest')

plt.subplot(2,2,2)
plt.hist(gray.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.title('histogram', fontweight ="bold")

plt.subplot(2,2,3)
plt.title('Thresh 85', fontweight ="bold")
plt.imshow(ret1, cmap ="binary_r", interpolation ='nearest')

plt.subplot(2,2,4)
plt.title('Otsu', fontweight ="bold")
plt.imshow(ret2, cmap ="binary_r", interpolation ='nearest')

plt.show()

wait()