import math

class SpPoint:
  def __init__(self,x,y,z):
    self.x=float(x)
    self.y=float(y)
    self.z=float(z)

  def delta(a,b):
    print(math.sqrt((p1.x-p0.x)**2+(p1.y-p0.y)**2+(p1.z-p0.z)**2))


coord=[0,0,0,0,0,0]

for i in range(0,3):
  coord[i]=input("coordinata primo punto:")

for j in range(3,6):
  coord[j]=input("coordinata secondo punto:")

p0=SpPoint(coord[0],coord[1],coord[2])
p1=SpPoint(coord[3],coord[4],coord[5])

SpPoint.delta(p0,p1)