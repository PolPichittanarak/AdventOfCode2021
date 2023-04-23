file = open("day2.txt", "r")
filecontent = file.readlines()
horizontal = 0
aim = 0
depth = 0
for line in filecontent:
	command = line.split(" ")
	if command[0].strip() == "forward":
		horizontal += int(command[1])
		#print("forward:", int(command[1]))
		# print("horizontal : " , horizontal)
		depth += int(command[1]) * aim
		#print("depth increase from aim :", int(command[1])*aim)
		# depth += int(command[1]) * aim
	elif command[0].strip() == "up":
		aim -= int(command[1])
		# depth -= int(command[1])
	elif command[0].strip() == "down":
		aim +=  int(command[1])
		# depth += int(command[1])
	#print("aim:", aim)
	#print("depth: ", depth)


print(horizontal)
print(depth)
print(horizontal * depth)