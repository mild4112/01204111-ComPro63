import json
def openjson(file):
	with open(file) as f:
		return json.loads(f.read())

f=openjson(input("File name: "))
number=int(input("input: "))

if number==1:
	print(len(f))
elif number==2:
	print(len(set([i["author"] for i in f])))
elif number==3:
	maxresult=0
	result=dict()
	for i in f:
		if i["author"] not in result:
			result[i["author"]]=1
		else:
			result[i["author"]]+=1
			if result[i["author"]]> maxresult:
				maxresult=result[i["author"]]
	for i in result:
		if result[i]==maxresult:
			print(i)
elif number==4:
	print(len(set([i["topic"] for i in f])))
elif number==5:
	print(len([i for i in f if i["topic_priority"]=="ALERT"]))
elif number==6:
	print(len([i for i in f if i["topic_priority"]=="UNIMPORTANT"]))
elif number==7:
	if len([i for i in f if i["language"]!="EN"]) != 0:
		print(True)
	else:
		print(False)
elif number==8:
	j=[len(i["text"].split()) for i in f]
	j.sort(reverse=True)
	print(j[0])

