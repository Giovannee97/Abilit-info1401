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

a=input("Primo vettore:")
b=input("Secondo vettore:")

a=a.split(",")
b=b.split(",")

c=[]
d=[]

c=[float(x) for x in a]
d=[float(x) for x in b]

print(c,d)

vect.dot(c,d)