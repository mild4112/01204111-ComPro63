def readfile(filename):
	with open(filename) as f:
		tmp=[]
		for i in f:
			tmp.append(i.strip().split(","))
	return tmp

def q1(data):
	print(len(data))

def q2(data):
	tmp=[]
	for i in range(37):
		sum=0
		for j in range(1,len(data)):
			sum += int(data[j][i]) 
		tmp.append(sum)
	print(data[0][tmp.index(max(tmp))])

def q3(data):
	tmp=[]
	for i in range(1,len(data)):
		tmp.append(int(data[i][5]))
	tmp.sort()
	tmp.reverse()
	for i in range(0,3):
		print(tmp[i],end=" ")

def q4(data):
	tmp=[]
	for i in range(1,len(data)):
		sum=0
		for j in range(len(data[0])-1):
			sum+=int(data[i][j])
		tmp.append(sum)
	print(data[tmp.index(max(tmp))+1][len(data[0])-1],str(max(tmp)))

def q5(data):
	tmp=[]
	for i in range(1,len(data)):
		tmp.append(int(data[i][0]))
	print(data[tmp.index(max(tmp))+1][len(data[0])-1]+" "+str(max(tmp)))

def q6(data):
	res=0
	for i in range(1,len(data)):
		if int(data[i][17])>500:
			res+=1
	print(res)

def q7(data):
	res=0
	for i in range(1,len(data)):
		if int(data[i][7])>int(data[i][4]):
			res+=1
	print(res)

def q8(data):
	tmp=[]
	for i in range(1,len(data)):
		sum=0
		for j in range(37):
			sum+=int(data[i][j])
		tmp.append(int(data[i][26])/sum*100)
	print(data[tmp.index(max(tmp))+1][37])

def q9(data):
	tmp=0
	for i in range(1,len(data)):
		res=[]
		for j in range(37):
			res.append(int(data[i][j]))
			res.sort()
		if (res[len(res)-1]+res[len(res)-2])/sum(res)*100>70:
			tmp+=1
	print(tmp)

def q10(data):
	res=0
	for i in range(1,len(data)):
		if data[i][36]=="0":
			res+=1
	print(res)


f=readfile(input("File name: "))
q=int(input("enter number: "))
if q==1:
	q1(f)
elif q==2:
	q2(f)
elif q==3:
	q3(f)
elif q==4:
	q4(f)
elif q==5:
	q5(f)
elif q==6:
	q6(f)
elif q==7:
	q7(f)
elif q==8:
	q8(f)
elif q==9:
	q9(f)
elif q==10:
	q10(f)

