class CS:
  def __init__(self,name,score):
    self.name=str(name)
    self.score=float(score)

  def add(self):
    print("Ho aggiunto la squadra:",self.name,self.score)
  def __delete__(self):
    print("Squadra eliminata")

teams=[]

temp1="sì"

while temp1=="sì":
    
  temp1=input(str("Vuoi aggiungere una squadra?"))

  if temp1=="sì":
    name=str(input("nome squadra:"))
    score=float(input("punteggio:"))

    obj=CS(name,score)
    CS.add(obj)

    teams.append(obj) 

  elif temp1=="no":
    temp2=input(str("Vuoi eliminare una squadra?"))
    if temp2=="sì":
      name=str(input("nome squadra da eliminare:"))
      for name in teams:
        b=obj.name
        print(b)

    
    
  