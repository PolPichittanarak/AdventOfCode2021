file = open("day3.txt", "r")
filecontent = file.readlines()
filearray = []
for line in filecontent:
	filearray.append(line)
gamma = "111011100000"
epsilon = "000100011111"
currentindex = 0
filtered = []
for i in range(12):
	countzero = 0
	countone = 0
	for count, line in enumerate(filearray):
		for index, bit in enumerate(line):
			if index == currentindex:
				if bit == "0":
					countzero += 1
				else:
					countone += 1
	less = "1" if countzero > countone else "0"
	for line in filearray:
		if line[currentindex] == less:
			filtered.append(line)

	print(filtered)
	filearray = filtered
	filtered = []
	currentindex += 1

	# print("current index:", str(currentindex), "there are", str(countzero), "zeros and " + str(countone), "ones.")

	'''
	if countzero > countone:
		gamma = gamma + "0"
		epsilon = epsilon + "1"
	else:
		gamma = gamma + "1"
		epsilon = epsilon + "0"
	''' 


# print(gamma)
# print(epsilon)