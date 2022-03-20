class CS:
  def __init__(self,name,score):
    self.name=str(name)
    self.score=float(score)

  def add(self):
    print("Ho aggiunto la squadra:",self.name,self.score)
    
  def printa(temp3,nteams,teams):
    
    if temp3=="sì":
      namesrc=str(input("Nome squadra da visualizzare:"))
    
      for i in range(len(nteams)):
        if namesrc==nteams[i]:
          print(teams[i].name,teams[i].score)
    else:
      pass
    
  def score(self):
    return self.score
    
  def winner(a,b):
    pool=[]
    for k in range(b):
      
      pool.append(a[k].score)

    j=pool.index(max(pool))
    print("Squadra Vincitrice:",a[j].name, "con:",a[j].score,"pti")

  def looser(a,b):
    pool=[]
    loosers=[]
    for k in range(b):
      
      pool.append(a[k].score)

    for z in range(0,3):
      j=pool.index(min(pool))
      loosers.append([a[j].name,a[j].score])
      pool.pop(j)
      a.pop(j)

    print("Gli ultimi tre in classifica sono:",loosers)

#####################################################

teams=[]
nteams=[]
steams=[]
count=int(0)

temp1="sì"

while temp1=="sì":
    
  temp1=input(str("Vuoi aggiungere una squadra?"))

  if temp1=="sì":
  
    name=str(input("Nome squadra:"))
    if name in nteams:
      raise TypeError("Squadra già inserita")
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
    if namedel not in nteams:
      raise TypeError("Squadra non presente, digita di nuovo")
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

  CS.printa(temp3,nteams,teams)
  
else:
  pass
  
temp4=input(str("Vuoi visualizzare il vincitore?"))
  
if temp4=="sì":
    CS.winner(teams,count)

else:
  pass

CS.looser(teams,count)