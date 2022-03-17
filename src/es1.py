import math

class SpPoint:
  def __init__(self,x,y,z):
    self.x=float(x)
    self.y=float(y)
    self.z=float(z)

  def delta(aa,bb):
    print(math.sqrt((aa.x-bb.x)**2+(aa.y-bb.y)**2+(aa.z-bb.z)**2))

coord=[0,0,0,0,0,0]

for i in range(0,3):
  coord[i]=input("coordinata primo punto:")

for j in range(3,6):
  coord[j]=input("coordinata secondo punto:")

p0=SpPoint(coord[0],coord[1],coord[2])
p1=SpPoint(coord[3],coord[4],coord[5])

n=int(input("Quanti punti?"))

import numpy
matrix=numpy.zeros((n, 3))

for i in range(n):
  a=[]
  for j in range(3):
    matrix[i][j]=float(input("entrata rowwise(x,y,z):"))

print(matrix)

pts=[]

i=0
for i in range(len(matrix)):
  pts.append((SpPoint(matrix[i][0],matrix[i][1],matrix[i][2])))

print("Tra quali due punti vuoi calcolare la distanza?")
temp1=int(input("primo punto"))
temp2=int(input("secondo punto"))

aa=pts[temp1]
bb=pts[temp2]

SpPoint.delta(aa,bb)