file = open("day13test.txt", "r")
filecontent = file.readlines()
coorlist = []
maxx = 0
maxy = 0

def AddVertical():
	return

def AddHorizontal():
	return

for line in filecontent:
	if line != "\n":
		line = line.replace("\n", "")
		coor = line.split(",")
		sublist = []
		for i, val in enumerate(coor):
			if i == 0 and int(val) > maxx:
				maxx = int(val) + 1
			if i == 1 and int(val) > maxy:
				maxy = int(val) + 1
			sublist.append(int(val))
		coorlist.append(sublist)
	elif line.startswith("fold"):
		line = line.split(" ")
		fold = line[2]
		fold = fold.split("=")
		direction = fold[0]
		line = int(fold[1])




def DisplayBoard(board):
	for line in board:
		for cell in line:
			print(cell, end = "")
		print()


print(coorlist)
print(maxx)
print(maxy)
			
#create board
board = []
for i in range(maxy):
	row = []
	for y in range(maxx + 1):
		row.append(".")
	board.append(row)



for coordinate in coorlist:
	print(coordinate)
	x = coordinate[0]
	y = coordinate[1]  
	board[y][x] = "#"
	DisplayBoard(board)
	print()

