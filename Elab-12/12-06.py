n=int(input("n: "))
matrix=[[" " for i in range(n)]for j in range(n)]
x=0
y=n-1
for i in range(n//2):
	matrix[i][x+i]="+"
	matrix[i][n//2]="+"
	matrix[i][y-i]="+"
for i in range(n):
	matrix[n//2][i]="+"
for i in range(n//2):
	matrix[n-i-1][x+i]="+"
	matrix[n-i-1][n//2]="+"
	matrix[n-i-1][y-i]="+"

for i in range(n):
	for j in range(n):
		print(matrix[i][j],end="")
	print()
