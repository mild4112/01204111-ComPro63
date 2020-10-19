number=int(input("n: "))
for i in range(2,number+1):
  if number==1:
    break
  while number%i==0:
    print(i,end=" ")
    number=number//i 