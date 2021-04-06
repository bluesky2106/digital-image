import cv2

def decrease_bright(value):
  img = cv2.imread('./internet/quiz3.png', cv2.IMREAD_GRAYSCALE)
  img[img > value] -= value
  img[img <= value] = 0
  return img

l1 = 64
l2 = 32
l3 = 16
l4 = 8


img = cv2.imread('./internet/quiz3.png', cv2.IMREAD_UNCHANGED)
img1 = decrease_bright(l1)
img2 = decrease_bright(l2)
img3 = decrease_bright(l3)
img4 = decrease_bright(l4)
cv2.imwrite('./images/quiz3_origin.png',img)
cv2.imwrite('./images/quiz3_level1.png',img1)
cv2.imwrite('./images/quiz3_level2.png',img2)
cv2.imwrite('./images/quiz3_level3.png',img3)
cv2.imwrite('./images/quiz3_level4.png',img4)


