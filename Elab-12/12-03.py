land=list()
while True:
	a=input()
	if a=='':
		break
	land.append(list(map(int,a.split())))

square=True
for i in land:
	if len(i)!=len(land[0]):
		square=False

if square==False:
	print("Can't Buy")
else:
	mins=1e9
	for i in range(len(land)-1):
		for j in range(len(land[i])-1):
			mins=min(mins,land[i][j]+land[i][j+1]*1.1+land[i+1][j+1]*1.1+land[i+1][j]*1.21)
			mins=min(mins,land[i+1][j]+land[i+1][j+1]*1.1+land[i][j+1]*1.1+land[i][j]*1.21)
	print(f"{mins:.2f}")