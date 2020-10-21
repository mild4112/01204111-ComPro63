def reflection(direction,mirror):
	if mirror == "\\":
		if direction == "right":
			return "down"
		elif direction == "left":
			return "up"
		elif direction == "down":
			return "right"
		elif direction == "up":
			return "left"
	elif mirror == "/":
		if direction == "right":
			return "up"
		elif direction == "left":
			return "down"
		elif direction == "down":
			return "left"
		elif direction == "up":
			return "right"

def saitonmove(field,direction,x,y,count=0):
	if field[y][x] == "\\" or field[y][x] == "/":
		direction=reflection(direction,field[y][x])
		count+=1
	if direction == "up":
		if y-1 == -1:
			return count
		else:
			return saitonmove(field,direction,x,y-1,count)
	elif direction == "down":
		if y+1 == len(field):
			return count
		else:
			return saitonmove(field,direction,x,y+1,count)
	elif direction == "left":
		if x-1 == -1:
			return count
		else:	
			return saitonmove(field,direction,x-1,y,count)
	elif direction == "right":
		if x+1 == len(field[0]):
			return count
		else:
			return saitonmove(field,direction,x+1,y,count)

field=[]
while True:
	a = input()
	if a == "":
		break
	field.append(a.split())

maxx= -1e9
for x in range(len(field[0])):
	y=0
	direc="down"
	maxx=max(maxx,saitonmove(field,direc,x,y))
	y=len(field)-1
	direc="up"
	maxx=max(maxx,saitonmove(field,direc,x,y))
for y in range(len(field)):
	x=0
	direc="right"
	maxx=max(maxx,saitonmove(field,direc,x,y))
	x=len(field[0])-1
	direc="left"
	maxx=max(maxx,saitonmove(field,direc,x,y))

print(f"Maximum saitron is {2**maxx} particle(s)")