def gcd(a,b):
	for i in range(1,min(a,b)+1):
		if  a%i==0 and b%i==0:
			gcd=i
	print(f"GCD : {gcd}")

def lcm(a,b):
	lcm=0
	i=max(a,b)
	while lcm==0:
		if i%a==0 and i%b==0:
			lcm=i
		i+=1
	print(f"LCM : {lcm}")

a=int(input("a : "))
b=int(input("b : "))
gcd(a,b)
lcm(a,b)




