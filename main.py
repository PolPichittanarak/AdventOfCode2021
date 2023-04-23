map = []
for i in range(40):
	row = []
	for j in range(40):
		row.append(".")
	map.append(row)



map[10][0] = "S"

for y, row in enumerate(map):
	for x, cell in enumerate(row):
		#if (10 <= y and y <= 5) and (30 <= x and 20 >= x):
		if (y in list(range(15, 21))) and (x in list(range(20,31))):
			map[y][x] = "T"
		



for row in map: 
	for cell in row:
		print(cell, end = "")
	print()