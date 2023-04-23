
file = open("day4test.txt", "r")
filecontent = file.readlines()
bingonum = [46,12,57,37,14,78,31,71,87,52,64,97,10,35,54,36,27,84,80,94,99,22,0,11,30,44,86,59,66,7,90,21,51,53,92,8,76,41,39,77,42,88,29,24,60,17,68,13,79,67,50,82,25,61,20,16,6,3,81,19,85,9,28,56,75,96,2,26,1,62,33,63,32,73,18,48,43,65,98,5,91,69,47,4,38,23,49,34,55,83,93,45,72,95,40,15,58,74,70,89]



boards = []
board = []
singleline = []
for line in filecontent:
	if line == "\n":
		boards.append(board)
		board = []
	else:
		numbers = line.split(" ")
		for number in numbers:
			if number != "":
				if number.endswith("\n"):
					number = number.replace("\n", "")
				singleline.append(number)
		board.append(singleline)
		singleline = []



def checkHorizontal(boardmarking):
	count = 0
	for i, row in enumerate(boardmarking):
		for y, cell in enumerate(row):
			if cell != "":
				count += 1
		if count == 5:
			return True
		else:
			count = 0
	return False

def checkVertical(boardmarking):
	count = 0
	index = 0
	for j in range(5):
		for i, row in enumerate(boardmarking):
			cell = row[index]
			if cell != "":
				count += 1
		if count == 5:
			return True
		else:
			count = 0
			index += 1
	return False


mostnum = 0
#print(leastnum)
boardnum = 0
for i, board in enumerate(boards):
	breakoutflag = False
	boardmarking = [
		["", "", "", "", ""],
		["", "", "", "", ""],
		["", "", "", "", ""],
		["", "", "", "", ""],
		["", "", "", "", ""]
	]
	numreq = 0
	for number in bingonum:
		numreq += 1
		#print("number: ", str(number))
		for y, row in enumerate(board):
			for x, cell in enumerate(row):
				if int(cell) == number:
					#print(str(number), "is on the board")
					boardmarking[y][x] = str(number)
					#for line in boardmarking:
						#print(line)
					#print()
					horizontal = checkHorizontal(boardmarking)
					vertical = checkVertical(boardmarking)
					if horizontal or vertical:
						
						
						breakoutflag = True
						break
			if breakoutflag:
				break
		if breakoutflag:
			break
	print("Number required = " + str(numreq))
	print("finalnum = ", str(number))
	print()
		#print()
	#print(boardmarking)
	for line in boardmarking:
		print(line)
	print()
	if numreq > mostnum:
		mostnum = numreq
		boardnum = i
	
print("most num =", str(mostnum), "on board number", str(boardnum + 1))
	
for line in boards[boardnum]:
	print(line)


	#print(boardmarking)

