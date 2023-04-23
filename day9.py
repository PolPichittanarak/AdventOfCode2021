file = open("day9test.txt", "r")
filecontent = file.readlines()

linenum = 0
for line in filecontent:
	linenum += 1

def CheckEast(height, line, j):
	if height < line[j + 1]:
		print("east true")
		return True
	return False

def CheckWest(height, line, j):
	if height < line[j - 1]:
		print("west true")
		return True
	return False

def CheckNorth(height, filecontent, i, j):
	if height < filecontent[i-1][j]:
		print("north true")
		return True
	return False

def CheckSouth(height,filecontent, i, j):
	if height < filecontent[i + 1][j]:
		print("south true")
		return True
	return False


lowpoints = []

for i, line in enumerate(filecontent):
	for j, height in enumerate(line):
		if height != "\n":
			print()
			print(height, end = " ")
			valid = False
			if (i != 0 and i != linenum - 1) and (j != 0 and j != len(line) -1):
				print("Check 1")
				if CheckEast(height, line, j) and CheckWest(height, line, j):
					if CheckNorth(height, filecontent, i, j) and CheckSouth(height,filecontent, i, j):
						valid = True

								
			#top line 
			elif i == 0:
				print("Check 2")
				if CheckSouth(height,filecontent, i, j):
				
					if j == 0:
						print("top left")
						valid = CheckEast(height, line, j)
					elif j == 9:
						print("top right")
						valid = CheckWest(height, line, j)
					else:
						print("none vertices")
						if CheckEast(height, line, j) and CheckWest(height, line, j):
							valid = True
						else:
							valid = False
				else:
					valid = False

					

			# bottom line 
			elif i == linenum - 1:
				print("Check 3")
				if CheckNorth(height, filecontent, i, j):
					if j == 0:
						print("bottom left")
						valid = CheckEast(height, line, j)
					elif j == 9:
						print("bottom right")
						valid = CheckWest(height, line, j)
					else:
						print("none vertices")
						if CheckEast(height, line, j) and CheckWest(height, line, j):
							valid = True
						else:
							valid = False
				else:
					valid = False


			#left
			elif j == 0:
				print("Check 4")
				if CheckEast(height, line, j):
					if i == 0:
						valid = CheckSouth(height,filecontent, i, j)
					elif i == linenum - 1:
						valid = CheckNorth(height, filecontent, i, j)
					else:
						if CheckSouth(height,filecontent, i, j) and CheckNorth(height, filecontent, i, j):
							valid = True
						else:
							valid = False
				else:
					valid = False

			#right
			elif j == 9:
				print("Check 5")
				if CheckWest(height, line, j):
					if i == 0:
						valid = CheckSouth(height, filecontent, i, j)
					elif i == linenum - 1:
						valid = CheckNorth(height, filecontent, i, j)
					else:
						if CheckSouth(height,filecontent, i, j) and CheckNorth(height, filecontent, i, j):
							valid = True
						else:
							valid = False
				else:
					valid = False

			print(valid)
			if valid:
				lowpoints.append(int(height))
			

print(lowpoints)
score = 0
for num in lowpoints:
	score += int(num) + 1
print(len(lowpoints))
print(score)