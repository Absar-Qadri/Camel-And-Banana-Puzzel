dist=int(input("Total Distance to be Travelled :")) 
total=int(input("No of Bananas :")) 
maxload=int(input("Capacity per trip : ")) 
eachkm=1 
totalmoved=0
midpoints=total//dist
for x in range(midpoints,1,-1):
  trips=2*x-1
  movednow=((total-maxload)-total)/trips
  total=total-maxload
  totalmoved=totalmoved+movednow

bananas=round(maxload-abs(totalmoved))
print("Bananas Remaining",bananas)
  
