x=[[1,2,3],
   [3,4,5],
   [6,7,8]]
y=[[1,2,0,0],
   [0,1,0,5],
   [0,1,1,0]]

result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

result2 = [[0,0,0],
          [0,0,0],
          [0,0,0]]

print('lenx',len(x))
print('leny0',len(y[0]))

print(x[0][0])

for i in range(len(x)):
  for j in range(len(y[0])):
    for k in range(len(y)):
      result[i][j] += x[i][k] * y[k][j]
for r in range(len(result)):
  print(result[r])

a=1.6

for i in range(len(x[0])):
  for j in range(len(x)):
    result2[i][j] += x[i][j]*a
for r in range(len(result2)):
  print(result2[r]) 

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def myfunc(self):
    print("Hello my name is "+ self.name, "and Im" + self.age, "yrs old" )

p1=Person("Cestilio",133)
print(p1.name)
print(p1.age)

p1.myfunc()