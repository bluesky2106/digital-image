import numpy as np
import matplotlib.pyplot as plt

def element_wise_divide():
  print("Element-wise divide")

  a = np.array([8, 6, 4, 2])
  b = np.array([4, 3, 2, 1])
  c = a / b
  print('a =', str(a))
  print('b =', str(b))
  print("a / b =", str(c))
  
  c = np.divide(a, b)
  print("np.divide(a, b) =", str(c))

  a = a.reshape((4, 1))
  b = b.reshape((1, 4))
  c = a / b
  print('a =', str(a))
  print('b =', str(b))
  print("a / b =", str(c))

  c = np.divide(a, b)
  print("np.divide(a, b) =", str(c))

  c = np.multiply(a, 1/b)
  print("np.multiply(a, 1/b) =", str(c))

element_wise_divide()