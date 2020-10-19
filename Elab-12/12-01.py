r=int(input("R: "))
c=int(input("C: "))
res=0
while r!=0 and c!=0:
  res+=r*c
  r-=1
  c-=1
print(res) 