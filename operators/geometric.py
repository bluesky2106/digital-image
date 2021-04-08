import numpy as np
import cv2

def wait():
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('./resources/test.png',img)
    cv2.destroyAllWindows()

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_CUBIC)
  return result

def flip_image(img,axes):
  if (axes == 0) :
    #horizental flip
    return cv2.flip( img, 0 )
  elif(axes == 1):
    #vertical flip
    return cv2.flip( img, 1 )
  elif(axes == -1):
    #both direction
    return cv2.flip( img, -1 )

def crop_image(img, xStart, xEnd, yStart, yEnd):
  return img[xStart:xEnd, yStart:yEnd]

def resize_image(img, fx, fy, interpolation):
  return cv2.resize(img,None,fx=fx, fy=fy, interpolation = interpolation)

def translate_image(img, tx, ty):
  (h, w, d) = img.shape
  M = np.float32([
    [1, 0, ty],
    [0, 1, tx]
  ])
  return cv2.warpAffine(img,M,(w,h))

def shear_image(img, shx, shy):
  (h, w, d) = img.shape
  M2 = np.float32([[1, 0, 0], [1, 2, 0]])
  # M2[0,2] = -M2[0,1] * w/2
  # M2[1,2] = -M2[1,0] * h/2
  return cv2.warpAffine(img, M2, (w, h))

# origin image
img = cv2.imread('./internet/image.png', cv2.IMREAD_UNCHANGED)

# rotation
rotate = rotate_image(img, 30)

# resize
resize = resize_image(img, 0.5, 0.5, cv2.INTER_CUBIC)

# translation
trans = translate_image(img, 100, 200)

# shear
aff = shear_image(img, 1, 1)

# crop
crop = crop_image(img, 0, 100, 0, 200)

# flip
hflip = flip_image(resize, 0)
vflip = flip_image(resize, 1)
hvflip = flip_image(resize, -1)

cv2.imshow('Original Image', img)
cv2.imshow('Rotate 30 deg Image', rotate)
cv2.imshow('Resize Image', resize)
cv2.imshow('Translate Image', trans)
cv2.imshow('Shear Image', aff)
cv2.imshow('Crop Image', crop)
cv2.imshow('H Flip Image', hflip)
cv2.imshow('V Flip Image', vflip)
cv2.imshow('HV Flip Image', hvflip)

wait()