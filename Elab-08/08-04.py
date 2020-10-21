s='''1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
*
1 2 3
4 5 6
7 8 9
10 11 12
13 14 15
+
1 0 0
0 1 0
0 0 1'''
with open("matrix.txt","w") as f:
	f.write(s)

def plus_matrix(A,B):
  result=[]
  for i in range(len(A)): 
    res=[]
    for j in range(len(A[0])):
      res.append(int(A[i][j])+int(B[i][j]))
    result.append(res)
  return result

def mul_matrix(A,B):
  result=[]
  for i in range(len(A)):
    res=[]
    for j in range(len(B[0])):
      sum=0
      for x in range(len(B)):  
        sum+=int(A[i][x])*int(B[x][j])
      res.append(sum)
    result.append(res)
  return result

def minus_matrix(A,B):
  result=[]
  for i in range(len(A)):
    res=[]
    for j in range(len(A[0])):
      res.append(A[i][j]-B[i][j])
    result.append(res)
  return result

def print_matrix(res):
	for i in range(len(res)):
		for j in range(len(res[0])):
			print(f"{res[i][j]:^5}",end=" ")
		print()

def readfile(filename):
	with open(filename) as f:
		op=[]
		matrix=[]
		res=[]
		for i in f:
			if i.strip()=="":
				pass
			elif i.strip() in ["*","+"]:
				op.append(i.strip())
				matrix.append(res)
				res=[]
			else:
				res.append(i.strip().split())
			matrix.append(res)
		return matrix,op

matrix,op=readfile(input("File name: "))
print(matrix)
for i in range(len(op)):
  if op[i]=="+":
    matrix[i+1]=plus_matrix(matrix[i],matrix[i+1])
  elif op[i]=="*":
    matrix[i+1]=mul_matrix(matrix[i],matrix[i+1])
  elif op[i]=="-":
    matrix[i+1]=minus_matrix(matrix[i],matrix[i+1])

print_matrix(matrix[len(matrix)-1])