

file = open("day11test.txt", "r")
octopus_map = file.readlines()
ocmap = []
width = len(octopus_map[0].strip())
height = len(octopus_map)
for a in octopus_map:
	a_array = []
	for b in a:
		if b.isdigit():
			a_array.append(int(b))
	ocmap.append(a_array)

print(ocmap)




def North(CurrentLevel,j, k):
	CurrentLevel[j][k] = CurrentLevel[j-1][k] + 1


def NorthEast(CurrentLevel,j, k):
	CurrentLevel[j][k] = CurrentLevel[j-1][k+1] + 1


def East(CurrentLevel,j, k):
	CurrentLevel[j][k] = CurrentLevel[j][k+1] + 1


def SouthEast(CurrentLevel,j, k):
	CurrentLevel[j][k] = CurrentLevel[j+1][k+1] + 1


def South(CurrentLevel,j, k):
	CurrentLevel[j][k] = CurrentLevel[j+1][k] + 1
	

def SouthWest(CurrentLevel,j, k):
	CurrentLevel[j][k] = CurrentLevel[j+1][k-1] + 1


def West(CurrentLevel,j, k):
	CurrentLevel[j][k] = CurrentLevel[j][k-1] + 1


def NorthWest(CurrentLevel, j, k):
	CurrentLevel[j][k] = CurrentLevel[j-1][k-1] + 1





def display_map(ocmap):
	for row in ocmap:
		for oc in row:
			print(oc, end = "")
		print()




def standard_increment(ocmap):
	FlashedOc = []
	for i, row in enumerate(ocmap):
		for j, oc in enumerate(row):
			if oc + 1 == 10:
				ocmap[i][j] = 0
				FlashedOc.append((i, j))
			else:
				ocmap[i][j] = oc + 1
	return FlashedOc





def adj_inc(CurrentLevel, i, j):
	if i == 0:
		South(CurrentLevel, i, j)
		if j == 0:
			East(CurrentLevel, i, j)
			SouthEast(CurrentLevel, i, j)
			#top right vertice
			


		elif j == width - 1:
			#top left vertice
			West(CurrentLevel, i, j)
			SouthWest(CurrentLevel, i, j)
			

		else:
			#non vertice top
			East(CurrentLevel, i, j)
			West(CurrentLevel, i, j)
			SouthEast(CurrentLevel, i, j)
			SouthWest(CurrentLevel, i, j)
			

	elif i == height - 1:
		North(CurrentLevel, i, j)
		if j == 0:
			#bottom right vertice
			East(CurrentLevel, i, j)
			NorthEast(CurrentLevel, i, j)
			

		elif j == width - 1:
			#bottom left vertice
			West(CurrentLevel, i, j)
			NorthWest(CurrentLevel, i, j)
			

		else:
			#non vertice bottom
			West(CurrentLevel, i, j)
			East(CurrentLevel, i, j)
			NorthWest(CurrentLevel, i, j)
			NorthEast(CurrentLevel, i, j)
			
			
	elif j != 0 and i != height - 1:
		North(CurrentLevel, i, j)
		South(CurrentLevel, i, j)
		if j == 0:
			#left column non vertices
			East(CurrentLevel, i, j)
			NorthEast(CurrentLevel, i, j)
			SouthEast(CurrentLevel, i, j)
			

		elif j == width - 1:
			#right column non vertices
			West(CurrentLevel, i, j)
			NorthWest(CurrentLevel, i, j)
			SouthWest(CurrentLevel, i, j)
			


		else:
			#normal
			North(CurrentLevel, i, j)
			South(CurrentLevel, i, j)
			East(CurrentLevel, i, j)
			West(CurrentLevel, i, j)
			NorthEast(CurrentLevel, i, j)
			NorthWest(CurrentLevel, i, j)
			SouthEast(CurrentLevel, i, j)
			SouthWest(CurrentLevel, i, j)
	return




def collateral_incCheck():
	for i, row in enumerate(ocmap):
		for j, cell in enumerate(row):
			if cell == 0:
				adj_inc(cell, i, j)
	return

print("stage 0:")
display_map(ocmap)
print()

for i in range(2):
	print("stage:", str(i + 1))
	FlashedOc = standard_increment(ocmap)

	FlashdOc = [] #cannot flash anymore in this stage
	
	Flashed = True
	while Flashed:
		Flashed = False
		collateral_incCheck()

		
	display_map(ocmap)
	

	
	print()
	