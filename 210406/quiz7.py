import cv2

def change_color():
  lim = 100
  img = cv2.imread('./internet/quiz7.png', cv2.IMREAD_UNCHANGED)
  (h, w, d) = img.shape
  # print("width={}, height={}, depth={}".format(w, h, d))
  for c in range(w):
    for r in range(h):
      # print(img[r, c])
      if img[r, c][0] > lim:
        img[r, c][0] = 255
        img[r, c][1] = 0
        img[r, c][2] = 0
      else:
        img[r, c][0] = 0
        img[r, c][1] = 0
        img[r, c][2] = 255
  return img

img = cv2.imread('./internet/quiz7.png', cv2.IMREAD_UNCHANGED)
img1 = change_color()

cv2.imwrite('./images/quiz7_origin.png',img)
cv2.imwrite('./images/quiz7_changed.png',img1)
