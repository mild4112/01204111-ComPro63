def pure_table(list,size):
	table=[[] for i in range(size-2)]
	for m in range(size-2):
		for n in range(size-2):
			sum=0
			for i in range(m,3+m):
				for j in range(n,3+n):
					sum+=int(list[i][j])
			table[m].append(sum/9)
	return table

def checkgrade(puretable):
	a=True
	b=True
	for i in range(len(puretable)):
		for j in range(len(puretable[i])):
			if puretable[i][j]<85:
				a=False
			if puretable[i][j]<70:
				b=False
			if puretable[i][j]<60:
				return "nograde"
	if a==True:
		return "a"
	elif b==True:
		return "b"
	else:
		return "c"

def upgrade(list,grade,size):
	if grade=="a":
		return print("Output: Grade A")
	elif grade=="b":
		degree=90
	elif grade=="c":
		degree=85
	elif grade=="nograde":
		degree=70
	tmp=True
	count=0
	for i in range(size):
		for j in range(size):
			if int(list[i][j])>=degree:
				count+=1
	if (count/size**2)*100<=25:
		tmp=False

	if tmp:
		if grade=="b":
			return print("Output: Grade A (Upgrade From B)")
		elif grade=="c":
			return print("Output: Grade B (Upgrade From C)")
		elif grade=="nograde":
			return print("Output: Grade C (Upgrade From No Grade)")
	elif grade=="nograde":
		return	print("Output: No Grade")
	else:
		return print(f"Output: Grade {grade.upper()}")

	
size=int(input("Material size: "))
pure=[]
for i in range(size):
	tmp=input().split()
	pure.append(tmp)
puretable=pure_table(pure,size)
grade=checkgrade(puretable)
upgrade(pure,grade,size)




