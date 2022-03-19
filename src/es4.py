class CS:
  def __init__(self,name,score):
    self.name=str(name)
    self.score=float(score)

  def add(self,c,d):
    print("Ho aggiunto la squadra:",self.name,self.score)
    
  def printa(self):
    print(self.name,self.score)
    
  def score(self):
    return self.score
    
  def winner(a,b):
    pool=[]
    for k in range(b):
      
      pool.append(a[k].score)

    j=pool.index(max(pool))
    print("Squadra Vincitrice:",a[j].name, "con:",a[j].score,"pti")
    

teams=[]
nteams=[]
steams=[]
count=int(0)

temp1="sì"

while temp1=="sì":
    
  temp1=input(str("Vuoi aggiungere una squadra?"))

  if temp1=="sì":
  
    name=str(input("Nome squadra:"))
    score=float(input("Punteggio:"))
    
    obj=CS(name,score)
    CS.add(obj)

    teams.append(obj) 
    nteams.append(obj.name)
    steams.append(obj.score)
    count +=1
    
    
  else:
    pass

else:
  pass

#print("teams",teams)
#print("nteams",nteams)

temp2="sì"

while temp2=="sì":
  
  temp2=str(input("Vuoi eliminare una squadra?"))
  
  if temp2=="sì":
    namedel=str(input("Nome squadra da eliminare:"))
    count -=1
    
    for i in range(count):
      if namedel==nteams[i]:
        del (teams[i])
        print("Squadra eliminata")
        nteams.pop(i)
      else:
        pass
  else:
    pass

else:
  pass

temp3="sì"

while temp3=="sì":
  
  temp3=input(str("Vuoi visualizzare una squadra?"))
  
  if temp3=="sì":
    namesrc=str(input("Nome squadra da visualizzare:"))
    
    for i in range(len(nteams)):
      if namesrc==nteams[i]:
        CS.printa(teams[i])
  else:
    pass

else:
  pass
  
temp4=input(str("Vuoi visualizzare il vincitore?"))
  
if temp4=="sì":
    CS.winner(teams,count)

else:
  pass

