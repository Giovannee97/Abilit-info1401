import math

class vect:
  def __init__(self,a):
    self.a=list()

  def dot(self,b):
    import numpy
    if len(self)!=len(b):
      raise ("Impossibile fare il prodotto tra i due vettori")
    c=numpy.dot(self,b)
    print("Prodotto scalare:",c)
    return c

class mat:
  def __init__(self,a):
    self.a=list()

  def matprod(self,c):
    import numpy
    print("lenself", np.shape(self)[1])
    print("lenb",np.shape(b)[0])
    
    if np.shape(self)[1]!=np.shape(b)[0]:
      raise ("Impossibile fare il prodotto tra le due matrici")
    d=numpy.matmul(self,c)
    print("Prodotto matriciale:",d)
    return d

import numpy as np

a=np.loadtxt("vec1.txt", dtype='f', delimiter=None)
b=np.loadtxt("vec2.txt", dtype='f', delimiter=None)

#a=a.split(",")
#b=b.split(",")

#c=[float(x) for x in a]
#d=[float(x) for x in b]

#c=list(map(float,a))
#d=list(map(float,b))

print(a,b)

vect.dot(a,b)

mat1 = np.loadtxt("mat1.txt", dtype='f', delimiter=None)
mat2 = np.loadtxt("mat2.txt", dtype='f', delimiter=None)

print(mat1,mat2)

mat.matprod(mat1,mat2)

