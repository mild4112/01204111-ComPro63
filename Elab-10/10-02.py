import json
def openfile(file):
	tmp=[json.loads(line) for line in open(file)]
	return tmp
 
def q1(data):
	print(len(data))

def q2(data):
	tmp=set()
	for i in data:
		tmp.add(i["reviewerID"])
	print(len(tmp))

def q3(data):
	tmp=set()
	for i in data:
		tmp.add(i["productID"])
	print(len(tmp))

def q4(data):
	tmp=set()
	for i in data:
		tmp.add(i["category"].split(">")[0])
	print(len(tmp))

def q5(data):
	tmp=set()
	for i in data:
		tmp.add(i["category"].split(">")[1])
	print(len(tmp))

def q6(data):
	maxid=""
	maxreview=0
	tmp=dict()
	for i in data:
		if i["reviewerID"] not in tmp:
			tmp[i["reviewerID"]]=0
		else:
			tmp[i["reviewerID"]]+=1
			if tmp[i["reviewerID"]]>maxreview:
				maxreview=tmp[i["reviewerID"]]
				maxid=i["reviewerID"]
	print(maxid)

def q7(data):
	res=[]
	tmp=dict()
	for i in data:
		if i["productName"] not in tmp:
			tmp[i["productName"]]=[i["overall"],1]
		else:
			tmp[i["productName"]][0]+=i["overall"]
			tmp[i["productName"]][1]+=1
	for i in tmp:
		res.append([tmp[i][0]/tmp[i][1],tmp[i][1],i])
	res.sort(reverse=True)
	print(res[0][2])

def q8(data):
	res=[]
	tmp=dict()
	for i in data:
		if i["productName"] not in tmp:
			tmp[i["productName"]]=[len(i["reviewText"].split()),1]
		else:
			tmp[i["productName"]][0]+=len(i["reviewText"].split())
			tmp[i["productName"]][1]+=1
	for i in tmp:
		res.append([tmp[i][0]/tmp[i][1],tmp[i][1],i])
	res.sort(reverse=True)
	print(res[0][2])



f=openfile(input("file name: "))
quiz=int(input("input: "))
if quiz==1:
	q1(f)
elif quiz==2:
	q2(f)
elif quiz==3:
	q3(f)
elif quiz==4:
	q4(f)
elif quiz==5:
	q5(f)
elif quiz==6:
	q6(f)
elif quiz==7:
	q7(f)
elif quiz==8:
	q8(f)