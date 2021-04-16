# Prog-09: Permutation
# Fill in your ID & Name
# ...
# Declare that you do this by yourself

import math

def fpermutation(numberlist):
	if numberlist==[]:
		return []
	result=[]
	for i in range(len(numberlist)):
		a=numberlist[i]
		res=numberlist[:i]+numberlist[i+1:]
		if res==[]:
			return [[a]] #ต้องเป็น list2D เพื่อให้ j เป็น list
		for j in fpermutation(res):
			result.append([a]+j) # j ต้องเป็น list ถึงจะ + ได้\
	result.sort()
	return result

def order_of(permutation):
	permu=fpermutation([i+1 for i in range(len(permutation))])
	return permu.index(permutation)+1
#---------------------------------
def permutation_at(order, n):
	if math.factorial(n)<order:
		return
	permu=fpermutation([i+1 for i in range(n)])
	return permu[order-1]
#---------------------------------
def next_permutation(permutation):
	permu=fpermutation([i+1 for i in range(len(permutation))])
	return permu[order_of(permutation)]
#---------------------------------
def prev_permutation(permutation):
	permu=fpermutation([i+1 for i in range(len(permutation))])
	return permu[order_of(permutation)-1]
#---------------------------------
def longest_cycles(permutation):

  return 
#---------------------------------
def main():
  while True:
    x = input().split()
    cmd = x[0]
    p = [int(e) for e in x[1:]]
    if cmd == 'O':
      print(order_of(p))
    elif cmd == 'A':
      print(permutation_at(p[0], p[1]))
    elif cmd == 'N':
      print(next_permutation(p))
    elif cmd == 'P': 
      print(prev_permutation(p))
    elif cmd == 'C':
      print(longest_cycles(p))
    elif cmd == 'Q':
      return
#-------------------------------------
main()