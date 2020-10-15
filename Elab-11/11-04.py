import csv

with open(input("Enter city file: ")) as f:
	city=list(csv.DictReader(f))
with open(input("Enter country file: ")) as f:
	country=list(csv.DictReader(f))

countrylist=[i["country"] for i in country if i["EU"]=="no" and i["coastline"]=="yes"]
tmp=dict()
for i in city:
	if i["country"] in countrylist:
		if i["country"] not in tmp:
			tmp[i["country"]]=[float(i["temperature"])]
		else:
			tmp[i["country"]].append(float(i["temperature"]))
print("Average temperature of countries having coastline, but not in EU:")
for i in sorted(tmp):
	print(f"{i} {sum(tmp[i])/len(tmp[i]):.2f}")

