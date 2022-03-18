import math
import numpy as np

class DDPoint:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def bari(self,point,n,i):
    if i==0:
      b=DDPoint((1.0/n)*(self.x+point.x),(1.0/n)*      (self.y+point.y))
    else:
      b=DDPoint(self.x+(1.0/n)*(point.x),self.y+(1.0/n)*      (point.y))
      
    return(b)
    
input = np.loadtxt(input(str("Inserire nome file:")), dtype='f', delimiter=None)

print(input)

p=[] #array di istanze DDPoint

for i in range(len(input)):
    p.append(DDPoint(input[i][0],input[i][1]))

o=DDPoint(0,0)

for i in range(1,len(input)):
  temp=DDPoint.bari(o,p[i],len(input),i)
  o=temp

print("Baricentro:",o.x,o.y)