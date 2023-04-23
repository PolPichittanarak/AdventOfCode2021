file = open("day11test.txt", "r")
filecontent = file.readlines()
SubState = []
width = len(filecontent[0].strip())
height = len(filecontent)
for row in filecontent:
	line = []
	for cell in row.strip():
		line.append(int(cell))
	print(line)
	SubState.append(line)

print()
print()


def North(SubState,j, k):
	SubState[j][k] = SubState[j-1][k] + 1


def NorthEast(SubState,j, k):
	SubState[j][k] = SubState[j-1][k+1] + 1


def East(SubState,j, k):
	SubState[j][k] = SubState[j][k+1] + 1


def SouthEast(SubState,j, k):
	SubState[j][k] = SubState[j+1][k+1] + 1


def South(SubState,j, k):
	SubState[j][k] = SubState[j+1][k] + 1
	

def SouthWest(SubState,j, k):
	SubState[j][k] = SubState[j+1][k-1] + 1


def West(SubState,j, k):
	SubState[j][k] = SubState[j][k-1] + 1


def NorthWest(SubState, j, k):
	SubState[j][k] = SubState[j-1][k-1] + 1
	


def flashIncrement(SubState, j, k):
	if j == 0:
		South(SubState, j, k)
		if k == 0:
			East(SubState, j, k)
			SouthEast(SubState, j, k)
			#top right vertice
			


		elif k == width - 1:
			#top left vertice
			West(SubState, j, k)
			SouthWest(SubState, j, k)
			

		else:
			#non vertice top
			East(SubState, j, k)
			West(SubState, j, k)
			SouthEast(SubState, j, k)
			SouthWest(SubState, j, k)
			

	elif j == height - 1:
		North(SubState, j, k)
		if k == 0:
			#bottom right vertice
			East(SubState, j, k)
			NorthEast(SubState, j, k)
			

		elif k == width - 1:
			#bottom left vertice
			West(SubState, j, k)
			NorthWest(SubState, j, k)
			

		else:
			#non vertice bottom
			West(SubState, j, k)
			East(SubState, j, k)
			NorthWest(SubState, j, k)
			NorthEast(SubState, j, k)
			
			
	elif j != 0 and i != height - 1:
		North(SubState, j, k)
		South(SubState, j, k)
		if k == 0:
			#left column non vertices
			East(SubState, j, k)
			NorthEast(SubState, j, k)
			SouthEast(SubState, j, k)
			

		elif k == width - 1:
			#right column non vertices
			West(SubState, j, k)
			NorthWest(SubState, j, k)
			SouthWest(SubState, j, k)
			


		else:
			#normal
			North(SubState, j, k)
			South(SubState, j, k)
			East(SubState, j, k)
			West(SubState, j, k)
			NorthEast(SubState, j, k)
			NorthWest(SubState, j, k)
			SouthEast(SubState, j, k)
			SouthWest(SubState, j, k)
			

def StandardIncrement(SubState):
	for i, line in enumerate(SubState):
		for j, cell in enumerate(line):
			SubState[i][j] = cell + 1
			if SubState[i][j] == 10:
				SubState[i][j] = 0

	


def flashCheck(SubState):
	FlashCheck = False
	for i, line in enumerate(SubState):
		for j, cell in enumerate(line):
			if cell == 0:
				flashIncrement(SubState, i, j)
				FlashCheck = True
				
	return FlashCheck


iteration = 2
for i in range(iteration):
	Flashing = True
	StandardIncrement(SubState)
	while Flashing:
		Flashing = flashCheck(SubState)
	for k in SubState:
		print(k)

	print()

	



# increment
# check for ones that flash
# increment the surroundings
# check again for ones that flash
# keep checking until Complete Flash == False
# Seperate increment function and checking surrounding function


