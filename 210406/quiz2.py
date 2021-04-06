import cv2

def increase_brightness(img, value=30):
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  h, s, v = cv2.split(hsv)

  lim = 255 - value
  v[v > lim] = 255
  v[v <= lim] += value

  final_hsv = cv2.merge((h, s, v))
  img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
  return img

def adjust_bright(value):
  img = cv2.imread('./internet/quiz2.png', cv2.IMREAD_UNCHANGED)
  img = img
  lim = 255 - value
  img[img > lim] = 255
  img[img <= lim] += value
  return img

l1 = 128
l2 = 64
l3 = 16
l4 = 8


img = cv2.imread('./internet/quiz2.png', cv2.IMREAD_UNCHANGED)
img1 = adjust_bright(l1)
img2 = adjust_bright(l2)
img3 = adjust_bright(l3)
img4 = adjust_bright(l4)
cv2.imwrite('./images/quiz2_origin.png',img)
cv2.imwrite('./images/quiz2_level1.png',img1)
cv2.imwrite('./images/quiz2_level2.png',img2)
cv2.imwrite('./images/quiz2_level3.png',img3)
cv2.imwrite('./images/quiz2_level4.png',img4)


