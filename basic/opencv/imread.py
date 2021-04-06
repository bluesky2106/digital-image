import numpy as np
import cv2
import utils

# Load an color image in grayscale
img1 = cv2.imread('./images/fpt.png', cv2.IMREAD_UNCHANGED)
cv2.imshow('original image',img1)

img2 = cv2.imread('./images/fpt.png', cv2.IMREAD_COLOR)
cv2.imshow('color image',img2)

img3 = cv2.imread('./images/fpt.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray image',img3)

utils.wait()