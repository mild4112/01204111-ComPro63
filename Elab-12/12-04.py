number=int(input())
matrix=[[0 for i in range(number)] for i in range(number)]

num=1
up=True
for i in range(number-1):
	if up:
		x=i
		y=number-1
		for j in range(i+1):
			matrix[y-j][x-j]=num
			num+=1
		up=not up
	else:
		x=0
		y=number-1-i
		for j in range(i+1):
			matrix[y+j][x+j]=num
			num+=1
		up=not up

for i in range(number):
	if up:
		matrix[number-1-i][number-1-i]=num
		num+=1
	else:
		matrix[i][i]=num
		num+=1
up=not up

for i in range(number-1):
	if up:
		x=number-1
		y=number-2-i
		for j in range(number-1-i):
			matrix[y-j][x-j]=num
			num+=1
		up=not up
	else:
		x=i+1
		y=0
		for j in range(number-1-i):
			matrix[y+j][x+j]=num
			num+=1
		up=not up

for i in range(number):
	for j in range(number):
		print(f'{matrix[i][j]:3.0f}',end=' ')
	print()

