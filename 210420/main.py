import cv2
import numpy as np

def wait():
  k = cv2.waitKey(0)
  if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('./resources/test.png',img)
    cv2.destroyAllWindows()

def mat2gray(img):
  A = np.double(img)
  out = np.zeros(A.shape, np.double)
  normalized = cv2.normalize(A, out, 1.0, 0.0, cv2.NORM_MINMAX)
  return out

 #Add noise to the image
def random_noise(image, mode='gaussian', seed=None, clip=True, **kwargs):
  image = mat2gray(image)
  
  mode = mode.lower()
  if image.min() < 0:
    low_clip = -1
  else:
    low_clip = 0
  if seed is not None:
    np.random.seed(seed=seed)
      
  if mode == 'gaussian':
    noise = np.random.normal(kwargs['mean'], kwargs['var'] ** 0.5, image.shape)        
    out = image  + noise
  if clip:        
    out = np.clip(out, low_clip, 1.0)
      
  return out

def prewitt_edge_detection():
  img = cv2.imread('./images/lenna.jpeg')
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
  kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
  img_prewittx = cv2.filter2D(gray, -1, kernelx)
  img_prewitty = cv2.filter2D(gray, -1, kernely)
  # cv2.imshow("Original Image", img)
  cv2.imshow("Original Gray Image", gray)
  cv2.imshow("Prewitt X", img_prewittx)
  cv2.imshow("Prewitt Y", img_prewitty)
  cv2.imshow("Prewitt", img_prewittx + img_prewitty)

  wait()

def prewitt_edge_detection_noise():
  img = cv2.imread('./images/lenna.jpeg')
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # img_gaussian = cv2.GaussianBlur(gray,(5,5),0)
  img_gaussian = random_noise(img,'gaussian', mean=0.1,var=0.01)
  img_gaussian = np.uint8(img_gaussian*255)

  kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
  kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
  img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
  img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
  # cv2.imshow("Original Image", img)
  cv2.imshow("Original Gray Image", gray)
  cv2.imshow("Gaussian Image", img_gaussian)
  cv2.imshow("Prewitt X", img_prewittx)
  cv2.imshow("Prewitt Y", img_prewitty)
  cv2.imshow("Prewitt", img_prewittx + img_prewitty)

  wait()

# prewitt_edge_detection()
# prewitt_edge_detection_noise()

def sobel_edge_detection():
  img = cv2.imread('./images/lenna.jpeg')
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  img_sobelx = cv2.Sobel(gray,cv2.CV_8U,1,0,ksize=1)
  img_sobely = cv2.Sobel(gray,cv2.CV_8U,0,1,ksize=1)
  img_sobel = img_sobelx + img_sobely

  # cv2.imshow("Original Image", img)
  cv2.imshow("Gray Image", gray)
  cv2.imshow("Sobel X", img_sobelx)
  cv2.imshow("Sobel Y", img_sobely)
  cv2.imshow("Sobel", img_sobel)

  wait()

def sobel_edge_detection_noise():
  img = cv2.imread('./images/lenna.jpeg')
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  gaussian = random_noise(img,'gaussian', mean=0.1,var=0.01)
  gaussian = np.uint8(gaussian*255)

  img_sobelx = cv2.Sobel(gaussian,cv2.CV_8U,1,0,ksize=1)
  img_sobely = cv2.Sobel(gaussian,cv2.CV_8U,0,1,ksize=1)
  img_sobel = img_sobelx + img_sobely

  # cv2.imshow("Original Image", img)
  cv2.imshow("Gray Image", gray)
  cv2.imshow("Gaussian Noise Image", gaussian)
  cv2.imshow("Sobel X", img_sobelx)
  cv2.imshow("Sobel Y", img_sobely)
  cv2.imshow("Sobel", img_sobel)

  wait()

# sobel_edge_detection()
# sobel_edge_detection_noise()

def canny_edge_detection():
  img = cv2.imread('./images/lenna.jpeg')
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  canny1 = cv2.Canny(gray,0,255)
  canny2 = cv2.Canny(gray,50,250)
  canny3 = cv2.Canny(gray,100,250)
  canny4 = cv2.Canny(gray,150,250)

  # cv2.imshow("Original Image", img)
  cv2.imshow("Gray Image", gray)
  cv2.imshow("Canny 1", canny1)
  cv2.imshow("Canny 2", canny2)
  cv2.imshow("Canny 3", canny3)
  cv2.imshow("Canny 4", canny4)

  wait()

canny_edge_detection()


# wait()