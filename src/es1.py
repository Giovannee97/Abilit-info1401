class SpPoint:
  def __init__(self,x,y,z):
    self.x=float(x)
    self.y=float(y)
    self.z=float(z)
    
p0=SpPoint(0,0,0)

p0.x=input("coordinata x:")
p0.y=input("coordinata y:")
p0.z=input("coordinata z:")

print("Coordinate punto iniziale:",p0.x,p0.y,p0.z)

n=integer(input("quanti punti vuoi definire?"))

for i in range(n):
  p i.x=input("coordinata x:")
  p i.y=input("coordinata y:")
  p i.z=input("coordinata z:")