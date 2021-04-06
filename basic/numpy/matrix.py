import numpy as np
import matplotlib.pyplot as plt

def zeros():
  a = np.zeros((4, 3))
  print(a)

# zeros()

def ones():
  a = np.ones((4, 3))
  print(a)

# ones()

def eye():
  a = np.eye(4)
  print(a)

# eye()

def rand():
  sample_size = 100000
  uniform = np.random.rand(sample_size)
  print("sum of uniform:", str(np.sum(uniform)))
  normal = np.random.randn(sample_size)
  print("sum of normal:", str(np.sum(normal)))

  pdf, bins, patches = plt.hist(uniform, bins=20, range=(0, 1), density=True)
  plt.title('rand: uniform')
  plt.show()

  pdf, bins, patches = plt.hist(normal, bins=20, range=(-4, 4), density=True)
  plt.title('randn: normal')
  plt.show()

# rand()

def magic(n):
  n = int(n)
  if n < 3:
    raise ValueError("Size must be at least 3")
  if n % 2 == 1:
    p = np.arange(1, n+1)
    return n*np.mod(p[:, None] + p - (n+3)//2, n) + np.mod(p[:, None] + 2*p-2, n) + 1
  elif n % 4 == 0:
    J = np.mod(np.arange(1, n+1), 4) // 2
    K = J[:, None] == J
    M = np.arange(1, n*n+1, n)[:, None] + np.arange(n)
    M[K] = n*n + 1 - M[K]
  else:
    p = n//2
    M = magic(p)
    M = np.block([[M, M+2*p*p], [M+3*p*p, M+p*p]])
    i = np.arange(p)
    k = (n-2)//4
    j = np.concatenate((np.arange(k), np.arange(n-k+1, n)))
    M[np.ix_(np.concatenate((i, i+p)), j)] = M[np.ix_(np.concatenate((i+p, i)), j)]
    M[np.ix_([k, k+p], [0, k])] = M[np.ix_([k+p, k], [0, k])]
  return M

def test_magic(ms):
  n = ms.shape[0]
  s = n*(n**2+1)//2 
  columns = np.all(ms.sum(axis=0) == s)
  rows = np.all(ms.sum(axis=1) == s)
  diag1 = np.diag(ms).sum() == s 
  diag2 = np.diag(ms[::-1, :]).sum() == s
  return columns and rows and diag1 and diag2 

print(magic(5))
