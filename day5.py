file = open("day5.txt", "r")
filecontent = file.readlines()
points = []
intcoor = []
intersects = 0
for i, line in enumerate(filecontent): 
	print(i + 1, line)
	line = line.replace("\n", "")
	coordinates = line.split(" -> ")
	beginningcoor = coordinates[0].split(",")
	endingcoor = coordinates[1].split(",")


	if beginningcoor[0] == endingcoor[0] or beginningcoor[1] == endingcoor[1]:

		if beginningcoor[0] == endingcoor[0]:
			#if [int(beginningcoor[0]), int(beginningcoor[1])] in points:
				#intcoor.append([int(beginningcoor[0]), int(beginningcoor[1])])
				#intersects += 1

			#points.append([int(beginningcoor[0]), int(beginningcoor[1])])
			
			ydiff = int(endingcoor[1]) - int(beginningcoor[1])
			#print("ydiff = ", str(ydiff))
			#print("vertical", end = " ")
			
			if ydiff > 0:
				for i in range(int(beginningcoor[1]), int(endingcoor[1]) + 1 ):
					coor = [int(beginningcoor[0]), i]
					#print(coor)
					if coor in points:
						if coor not in intcoor:
							intersects += 1
							intcoor.append(coor)
					points.append(coor)
			else:
				for i in range(int(beginningcoor[1]), int(endingcoor[1]) - 1, -1):
					coor = [int(beginningcoor[0]), i]
					#print(coor)
					if coor in points:
						if coor not in intcoor:
							intersects += 1
							intcoor.append(coor)
					points.append(coor)
			
		elif beginningcoor[1] == endingcoor[1]:
			#if [int(beginningcoor[0]), int(beginningcoor[1])] in points:
				#intcoor.append([int(endingcoor[0]), int(endingcoor[1])])
				#intersects += 1 
			#points.append([int(beginningcoor[0]), int(beginningcoor[1])])
			
			xdiff = int(endingcoor[0]) - int(beginningcoor[0])
			#print("xdiff = ", str(xdiff))
			#print("horizontal", end = " ")

			if xdiff > 0:
				for i in range(int(beginningcoor[0]), int(endingcoor[0]) + 1 ):
					coor = [i, int(beginningcoor[1])]
					#print(coor)
					if coor in points:
						if coor not in intcoor:
							intersects += 1
							intcoor.append(coor)
					points.append(coor)
			else:
				for i in range(int(beginningcoor[0]), int(endingcoor[0]) - 1, -1):
					coor = [i , int(beginningcoor[1])]
					#print(coor)
					if coor in points:
						if coor not in intcoor:
							intersects += 1
							intcoor.append(coor)
					points.append(coor)
	else:
		# directions = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
		if int(beginningcoor[0]) < int(endingcoor[0]) and int(beginningcoor[1]) < int(endingcoor[1]):
			for i in range((int(endingcoor[0]) - int(beginningcoor[0]) + 1)):
				coor = [int(beginningcoor[0]) + i , int(beginningcoor[1]) + i]
				if coor in points:
					if coor not in intcoor:
						intersects += 1
						intcoor.append(coor)
				points.append(coor)
				#print(coor)

		elif int(beginningcoor[0]) > int(endingcoor[0]) and int(beginningcoor[1]) < int(endingcoor[1]):
			for i in range((int(endingcoor[1]) - int(beginningcoor[1]) + 1)):
				coor = [int(beginningcoor[0]) - i , int(beginningcoor[1]) + i]
				if coor in points:
					if coor not in intcoor:
						intersects += 1
						intcoor.append(coor)
				points.append(coor)
				#print(coor)

		elif int(beginningcoor[0]) < int(endingcoor[0]) and int(beginningcoor[1]) > int(endingcoor[1]):
			for i in range((int(endingcoor[0]) - int(beginningcoor[0]) + 1)):
				coor = [int(beginningcoor[0]) + i , int(beginningcoor[1]) - i]
				if coor in points:
					if coor not in intcoor:
						intersects += 1
						intcoor.append(coor)
				points.append(coor)
				#print(coor)

		elif int(beginningcoor[0]) > int(endingcoor[0]) and int(beginningcoor[1]) > int(endingcoor[1]):
			for i in range(int(beginningcoor[1]) - int(endingcoor[1]) + 1):
				coor = [int(beginningcoor[0]) - i , int(beginningcoor[1]) - i]
				if coor in points:
					if coor not in intcoor:
						intersects += 1
						intcoor.append(coor)
				points.append(coor)
				#print(coor)
		


#print(points)
print(intersects)
#print(intcoor)
