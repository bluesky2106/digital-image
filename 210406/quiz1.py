import cv2

img = cv2.imread('./internet/4155459.png', cv2.IMREAD_UNCHANGED)
gray = cv2.imread('./internet/4155459.png', cv2.IMREAD_GRAYSCALE)
img256 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img128 = cv2.convertScaleAbs(img256, alpha=(127.0/255.0))
img64 = cv2.convertScaleAbs(img128, alpha=(63.0/127.0))
img32 = cv2.convertScaleAbs(img64, alpha=(31.0/63.0))
img16 = cv2.convertScaleAbs(img32, alpha=(15.0/31.0))
img8 = cv2.convertScaleAbs(img16, alpha=(7.0/15.0))
img4 = cv2.convertScaleAbs(img8, alpha=(3.0/7.0))
img2 = cv2.convertScaleAbs(img4, alpha=(1.0/3.0))

cv2.imwrite('./images/quiz1_origin.png',img)
cv2.imwrite('./images/quiz1_gray.png',gray)
cv2.imwrite('./images/quiz1_256.png',img256)
cv2.imwrite('./images/quiz1_128.png',img128)
cv2.imwrite('./images/quiz1_64.png',img64)
cv2.imwrite('./images/quiz1_32.png',img32)
cv2.imwrite('./images/quiz1_16.png',img16)
cv2.imwrite('./images/quiz1_8.png',img8)
cv2.imwrite('./images/quiz1_4.png',img4)
cv2.imwrite('./images/quiz1_2.png',img2)

