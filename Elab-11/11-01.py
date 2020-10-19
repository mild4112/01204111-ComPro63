import csv
with open(input("Enter File name: ")) as f:
	file=csv.DictReader(f)
	for i in file:
		if i["EU"]=="no" and i["coastline"]=="yes":
			print(i["country"],i["population"])
 