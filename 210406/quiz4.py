import cv2

def print_image_pixel(img):
  (h, w, d) = img.shape
  print("width={}, height={}, depth={}".format(w, h, d))
  for c in range(w):
    for r in range(h):
      print(img[r, c])

def contradict():
  img = cv2.imread('./internet/quiz4.png', cv2.IMREAD_UNCHANGED)
  lim = 100
  img[img > lim] = 0
  img[img <= lim] += 255
  return img

img = cv2.imread('./internet/quiz4.png', cv2.IMREAD_UNCHANGED)
img1 = contradict()

cv2.imwrite('./images/quiz4_origin.png',img)
cv2.imwrite('./images/quiz4_contradict.png',img1)
