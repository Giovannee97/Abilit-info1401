class CS:
  def __init__(self,name,score):
    self.name=str(name)
    self.score=float(score)

  def add(self):
    print("Ho aggiunto la squadra:",self.name,self.score)
  def __delete__(self):
    print("Squadra eliminata")
    
temp1=input(str("Vuoi aggiungere una squadra?"))

if temp1=="sì":
  name=str(input("nome squadra:"))
  score=float(input("punteggio:"))

  obj=CS(name,score)
  CS.add(obj)

else:
  temp2=input(str("Vuoi eliminare una squadra?"))
  if temp2=="sì":
    name=str(input("nome squadra da eliminare:"))
    
  