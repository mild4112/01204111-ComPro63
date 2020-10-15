import csv
with open(input("Enter file name: ")) as f:
	file=list(csv.DictReader(f))
tmp=dict()
for i in file:
	if i["country"] not in tmp.keys(): tmp[i["country"]]=[float(i["temperature"])]
	else: tmp[i["country"]].append(float(i["temperature"]))
for i in tmp:
	print(f"{i} {sum(tmp[i])/len(tmp[i]):.2f}")
