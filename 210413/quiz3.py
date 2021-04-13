import numpy as np
import matplotlib.pyplot as plt
import cv2

def gamma_correct(c, gamma):
  img = cv2.imread('./images/origin.jpg', cv2.IMREAD_UNCHANGED)
  new_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  for y in range(new_image.shape[0]):
    for x in range(new_image.shape[1]):
      value = c * (new_image[y,x] ** gamma)
      if value > 255: value = 255
      new_image[y,x] = value
  return new_image

# origin image
# img = cv2.imread('./images/origin.jpg', cv2.IMREAD_UNCHANGED)
# origin gray
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

c = 1.0
gamma = 2
gammaImg = gamma_correct(c, gamma)
equ = cv2.equalizeHist(gammaImg)
# res = np.hstack((gammaImg,equ)) #stacking images side-by-side

cv2.imwrite('./images/quiz3_gamma_2.png',gammaImg)
cv2.imwrite('./images/quiz3_equalization.png',equ)

hist,bins = np.histogram(gammaImg.flatten(),256,[0,256])
cdf = hist.cumsum()
# cdf_normalized = cdf * float(hist.max()) / cdf.max()

hist_equ, bins_equ = np.histogram(equ.flatten(),256,[0,256])
cdf_equ = hist_equ.cumsum()
# cdf_normalized_equ = cdf_equ * float(hist_equ.max()) / cdf_equ.max()

plt.subplot(1,2,1)
plt.plot(cdf, color = 'b')
plt.hist(gammaImg.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')

plt.subplot(1,2,2)
plt.plot(cdf_equ, color = 'b')
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')

plt.show()