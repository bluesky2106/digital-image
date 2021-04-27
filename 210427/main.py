import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.ndimage import rotate

def wait():
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('./resources/test.png',img)
    cv2.destroyAllWindows()

def filter_image(img, radius):
  radius = 3
  kernel = np.ones((radius,radius),np.float32)/(radius*radius)
  return cv2.filter2D(img,-1,kernel)

def filter_image_1(img, angle):
  kernel = np.array([
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [-1, -1, -1, -1, -1],
    [0, 0, 0, 0, 0]
  ])
  kernel = rotate(kernel, angle=angle)

  print(kernel)

  return cv2.filter2D(img,-1,kernel)

path = './images/bird_with_noise.jpg'
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
norm_img = cv2.normalize(gray, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

filter_img_3 = filter_image(norm_img, 3)
filter_img_5 = filter_image(norm_img, 5)
filter_img_7 = filter_image(norm_img, 7)

fiter_img_ang_0 = filter_image_1(norm_img, 0)
fiter_img_ang_45 = filter_image_1(norm_img, 45)
fiter_img_ang_90 = filter_image_1(norm_img, 90)

plt.subplot(3,3,1)
plt.title('Original Image', fontweight ="bold")
plt.imshow(img, cmap ="binary_r", interpolation ='nearest')

plt.subplot(3,3,2)
plt.title('Gray Image', fontweight ="bold")
plt.imshow(gray, cmap ="binary_r", interpolation ='nearest')

plt.subplot(3,3,3)
plt.title('Normalize Image', fontweight ="bold")
plt.imshow(norm_img, cmap ="binary_r", interpolation ='nearest')

plt.subplot(3,3,4)
plt.title('Filtered Image with radius 3', fontweight ="bold")
plt.imshow(filter_img_3, cmap ="binary_r", interpolation ='nearest')

plt.subplot(3,3,5)
plt.title('Filtered Image with radius 5', fontweight ="bold")
plt.imshow(filter_img_5, cmap ="binary_r", interpolation ='nearest')

plt.subplot(3,3,6)
plt.title('Filtered Image with radius 7', fontweight ="bold")
plt.imshow(filter_img_5, cmap ="binary_r", interpolation ='nearest')

plt.subplot(3,3,7)
plt.title('Another filter image', fontweight ="bold")
plt.imshow(fiter_img_ang_0, cmap ="binary_r", interpolation ='nearest')

plt.subplot(3,3,8)
plt.title('Another filter image angle 45', fontweight ="bold")
plt.imshow(fiter_img_ang_45, cmap ="binary_r", interpolation ='nearest')

plt.subplot(3,3,9)
plt.title('Another filter image angle 90', fontweight ="bold")
plt.imshow(fiter_img_ang_45, cmap ="binary_r", interpolation ='nearest')

plt.show()

