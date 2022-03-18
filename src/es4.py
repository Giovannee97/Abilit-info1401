class CS:
  def __init__(self,name,score):
    self.name=str(name)
    self.score=float(score)

  def add(self):
    print("Ho aggiunto la squadra:",self.name,self.score)
  def __del__(self):
    print("Squadra eliminata")

teams=[]
nteams=[]

temp1="sì"

while temp1=="sì":
    
  temp1=input(str("Vuoi aggiungere una squadra?"))

  if temp1=="sì":
  
    name=str(input("nome squadra:"))
    score=float(input("punteggio:"))
    
    obj=CS(name,score)
    CS.add(obj)

    teams.append(obj) 
    nteams.append(obj.name)
    print(nteams)

  else:
    pass

else:
  pass

temp2="sì"

while temp2=="sì":
  
  temp2=input(str("Vuoi eliminare una squadra?"))
  
  if temp2=="sì":
    namedel=str(input("nome squadra da eliminare:"))
    for i in range(len(nteams)):
      if namedel==nteams[i]:
        del teams[i]
      else:
      
  else:
    pass
    
else:
  pass
    
    
  