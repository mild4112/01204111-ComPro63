import json

def openfile(file):
	with open(file) as f:
		return json.loads(f.read())

def q1(data): 
	print(len(data))

def q2(data):
	sum=0
	for i in data:
		sum+=int(i["population"])
	print(sum)

def q3(data):
	c=0
	five=0
	for i in data:
		if i["country"][0]=="C":
			c+=1
		if len(i["country"])>5:
			five+=1
	print(c)
	print(five)

def q4(data):
	more=0
	bet=0
	less=0
	for i in data:
		if int(i["population"])>500000000:
			more+=1
		if 250000000<int(i["population"])<750000000:
			bet+=1
		if int(i["population"])<10000000:
			less+=1
	print(more)
	print(bet)
	print(less)

def q5(data):
	sum20=0
	sum50_150=0
	for i in data[0:20]:
		sum20+=float(i["World"])*100
	for i in data[49:150]:
		sum50_150+=float(i["World"])*100
	print(f"{sum20:.2f}")
	print(f"{sum50_150:.2f}")


s=input("File Name: ")
f=openfile(s)
quiz=int(input("Input : "))
if quiz==1:
	q1(f)
if quiz==2:
	q2(f)
if quiz==3:
	q3(f)
if quiz==4:
	q4(f)
if quiz==5:
	q5(f)
