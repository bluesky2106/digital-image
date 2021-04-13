import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('images/histeq_numpy1.jpg',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
# print(bins)
cdf = hist.cumsum()
print(cdf)

cdf_normalized = cdf * float(hist.max()) / cdf.max()
# print(cdf_normalized)

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()