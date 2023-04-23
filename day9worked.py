file = open("day9.txt", "r")
filecontent = file.readlines()
width = len(filecontent[0].strip())
height = len(filecontent)

def CheckNorth(filecontent, cell, j, i):
	if cell < filecontent[i-1][j]:
		return True
	else:
		return False

def CheckEast(filecontent, cell, j, i):
	if cell < filecontent[i][j + 1]:
		return True
	else:
		return False

def CheckSouth(filecontent, cell, j, i):
	if cell < filecontent[i + 1][j]:
		return True
	else:
		return False

def CheckWest(filecontent, cell, j, i):
	if cell < filecontent[i][j - 1]:
		return True
	else:
		return False


lowPoints = []

for i, line in enumerate(filecontent): # i corresponds to rows
	for j, cell in enumerate(line.strip()): # j corresponds to cell
		lowCheck = False
		if i == 0:
			# top left vertice
			if j == 0:
				
				#print("top left vertice")
				#print(cell)
				lowCheck = CheckSouth(filecontent, cell, j, i) and CheckEast(filecontent, cell, j, i)


			# top right vertice
			elif j == (width - 1):
				#print("top right vertice")
				#print(cell)
				lowCheck = CheckSouth(filecontent, cell, j, i) and CheckWest(filecontent, cell, j, i)


			# top row non-vertice
			else:
				#print("top row")
				#print(cell)
				lowCheck = (CheckWest(filecontent, cell, j, i) and CheckEast(filecontent, cell, j, i)) and CheckSouth(filecontent, cell, j, i)
		


		elif i == (height - 1):
			

			#bottom left vertice
			if j == 0:
				#print("bottom left vertice")
				#print(cell)
				lowCheck = CheckNorth(filecontent, cell, j, i) and CheckEast(filecontent, cell, j, i)


			# bottom right vertice
			elif j == (width - 1):
				#print("bottom right vertice")
				#print(cell)
				lowCheck = CheckNorth(filecontent, cell, j, i) and CheckWest(filecontent, cell, j, i)


			# bottom row non-vertice
			else:
				#print("bottom row")
				#print(cell)
				lowCheck = ((CheckEast(filecontent, cell, j, i) and CheckWest(filecontent, cell, j, i))) and CheckNorth(filecontent, cell, j, i)
		
		
		elif i != 0 or i != (height - 1):
			# left column non-vertice
			if j == 0:
				#print("left column")
				#print(cell)
				lowCheck = (CheckNorth(filecontent, cell, j, i) and CheckSouth(filecontent, cell, j, i)) and CheckEast(filecontent, cell, j, i)

			


			# right column non-vertice
			elif j == width - 1:
				#print("right column")
				#print(cell)
				lowCheck = (CheckNorth(filecontent, cell, j, i) and CheckSouth(filecontent, cell, j, i)) and CheckWest(filecontent, cell, j, i)


			else:
				#print("normal")
				lowCheck = (CheckNorth(filecontent, cell, j, i) and CheckSouth(filecontent, cell, j, i)) and (CheckEast(filecontent, cell, j, i) and CheckWest(filecontent, cell, j, i))
		
		if lowCheck:
			print(str(cell), "LOW POINT SPOTTED")
			lowPoints.append(cell)
print(lowPoints)
print(len(lowPoints))
total = 0
for point in lowPoints:
	total += int(point) + 1
print(total)