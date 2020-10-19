import csv
def opencsv(file):
	with open(file) as f:
		return list(csv.DictReader(f))

file=opencsv(input("Enter file name: "))
tmp=[float(i["temperature"]) for i in file]
print(f"Minimum: {min(tmp):.2f}")
print(f"Maximum: {max(tmp):.2f}")
print(f"Average temperature: {sum(tmp)/len(tmp):.4f}")

 