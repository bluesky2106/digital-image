import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def wait():
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('./resources/test.png',img)
    cv2.destroyAllWindows()

def adapt_thresh(gray, dimx, dimy):
  (h, w) = gray.shape
  # print(h, w)
  # Otsu's thresholding
  nx = math.floor(h / dimx)
  ny = math.floor(w / dimy)
  res = np.array([[]])
  for x in range(nx):
    for y in range(ny):
      split = gray[nx*dimx:(nx+1)*dimx, ny*dimx:(ny+1)*dimx]
      _, ret = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
      print(ret)
      # res = np.concatenate((res, ret), axis=1)
  return res

img = cv2.imread('./images/gradient_with_text.png')
new_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1 = adapt_thresh(gray, 10, 10)


plt.subplot(2,2,1)
plt.title('Origin Image', fontweight ="bold")
plt.imshow(new_image, interpolation ='nearest')

plt.subplot(2,2,2)
plt.title('Global Thresholding', fontweight ="bold")
plt.imshow(ret1, cmap ="binary_r", interpolation ='nearest')

plt.subplot(2,2,3)
plt.hist(gray.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.title('Histogram of Original', fontweight ="bold")



# plt.subplot(2,2,4)
# plt.title('Otsu', fontweight ="bold")
# plt.imshow(ret2, cmap ="binary_r", interpolation ='nearest')

plt.show()

# wait()