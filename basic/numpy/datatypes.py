import numpy as np

# https://numpy.org/doc/stable/user/basics.types.html

def basic_data_types():
  x = np.float32(1.0)
  print(x)
  print(type(x))


  x = np.float64(1.0)
  print(x)
  print(type(x))

  x = np.int8(1.0)
  print(x)
  print(type(x))

  x = np.int16(1.0)
  print(x)
  print(type(x))

  x = np.int32(1.0)
  print(x)
  print(type(x))

  x = np.int64(1.0)
  print(x)
  print(type(x))

  x = np.uint8(1.0)
  print(x)
  print(type(x))

  x = np.uint16(1.0)
  print(x)
  print(type(x))

  x = np.uint32(1.0)
  print(x)
  print(type(x))

  x = np.uint64(1.0)
  print(x)
  print(type(x))

def dtype_convert():
  a = np.array([[-8.0, 4.0], [0.0, 0.5]])
  print('a =', str(a))
  # print(a.shape)

  b = np.uint8(a)
  print('np.uint8(a) =', str(b))

  b = np.uint16(a)
  print('np.uint16(a) =', str(b))

dtype_convert()