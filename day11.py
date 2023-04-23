file = open("day11test.txt", "r")
filecontent = file.readlines()
octopus = []
linenum = 0
for i in filecontent:
	row = []
	for letter in i:
		if letter != "\n":
			row.append(int(letter))
	octopus.append(row)
	linenum += 1



def east(rownum, octopusnum, octopus):
	octopus[rownum][octopusnum + 1] = octopus[rownum][octopusnum + 1] + 1

def south(rownum, octopusnum, octopus):
	octopus[rownum + 1][octopusnum] = octopus[rownum + 1][octopusnum] + 1

def southeast(rownum, octopusnum, octopus):
	octopus[rownum + 1][octopusnum + 1] = octopus[rownum + 1][octopusnum + 1] + 1

def north(rownum, octopusnum, octopus):
	rownum = rownum - 1
	print(octopus[rownum][octopusnum])
	octopus[rownum - 1][octopusnum] = octopus[rownum - 1][octopusnum] + 1

def west(rownum, octopusnum, octopus):
	octopus[rownum][octopusnum - 1] = octopus[rownum][octopusnum - 1] + 1

def southwest(rownum, octopusnum, octopus):
	octopus[rownum + 1][octopusnum - 1] = octopus[rownum + 1][octopusnum - 1] + 1

def northeast(rownum, octopusnum, octopus):
	octopus[rownum - 1][octopusnum + 1] = octopus[rownum - 1][octopusnum + 1] + 1

def northwest(rownum, octopusnum, octopus):
	octopus[rownum - 1][octopusnum - 1] = octopus[rownum - 1][octopusnum - 1] + 1

def adjacentincrement(rownum, octopusnum, octopus):
	if rownum == 0:
		south(rownum, octopusnum, octopus)
		if octopusnum == 0:
			east(rownum, octopusnum, octopus)#east increments
			southeast(rownum, octopusnum, octopus) # southeast increments
		elif octopusnum == len(octopus[rownum]) - 1:
			southwest(rownum, octopusnum, octopus)
			west(rownum, octopusnum, octopus)
		else:
			east(rownum, octopusnum, octopus)
			west(rownum, octopusnum, octopus)
			southwest(rownum, octopusnum, octopus)
			southeast(rownum, octopusnum, octopus)

	elif rownum == linenum - 1:
		north(rownum, octopusnum, octopus)
		if octopusnum == 0:
			east(rownum, octopusnum, octopus)
			northeast(rownum, octopusnum, octopus)
		elif octopusnum == len(octopus[rownum]) - 1:
			west(rownum, octopusnum, octopus)
			northwest(rownum, octopusnum, octopus)
		else:
			east(rownum, octopusnum, octopus)
			west(rownum, octopusnum, octopus)
			northeast(rownum, octopusnum, octopus)
			northwest(rownum, octopusnum, octopus)
			
	elif octopusnum == 0:
		east(rownum, octopusnum, octopus)
		if rownum == 0:
			south(rownum, octopusnum, octopus)
			southeast(rownum, octopusnum, octopus)
		elif rownum == linenum - 1:
			northeast(rownum, octopusnum, octopus)
			north(rownum, octopusnum, octopus)
		else:
			north(rownum, octopusnum, octopus)
			south(rownum, octopusnum, octopus)
			southeast(rownum, octopusnum, octopus)
			northeast(rownum, octopusnum, octopus)
		
	elif octopusnum == 10: #len(octopus[rownum]) - 1:
		west(rownum, octopusnum, octopus)
		if rownum == 0:
			south(rownum, octopusnum, octopus)
			southwest(rownum, octopusnum, octopus)
		elif rownum == linenum - 1:
			north(rownum, octopusnum, octopus)
			northwest(rownum, octopusnum, octopus)
		else:
			north(rownum, octopusnum, octopus)
			south(rownum, octopusnum, octopus)
			northwest(rownum, octopusnum, octopus)
			southwest(rownum, octopusnum, octopus)
	
	else:
		north(rownum, octopusnum, octopus)
		northeast(rownum, octopusnum, octopus)
		east(rownum, octopusnum, octopus)
		southeast(rownum, octopusnum, octopus)
		south(rownum, octopusnum, octopus)
		southwest(rownum, octopusnum, octopus)
		west(rownum, octopusnum, octopus)
		northwest(rownum, octopusnum, octopus)
	

for count in range(10):
	for rownum, row in enumerate(octopus):
		for octopusnum, oc in enumerate(row):
			
			octopus[rownum][octopusnum] += 1
			glow = False
			if octopus[rownum][octopusnum] == 9:
				glow = True
				adjacentincrement(rownum, octopusnum, octopus)


				while glow:
					for row in octopus:
						for oc in row:
							if oc == 9:
								adjacentincrement(row, oc, octopus)
					glow = False
	print(octopus)
	print()