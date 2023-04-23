file = open("day1.txt", "r")
filecontent = file.readlines()
filecontentlist = []
for line in filecontent:
	filecontentlist.append(int(line))
currentdepth = 0
increasedDepth = 0
for line in filecontent:
	# print(line, end = ":")
	if int(line) > currentdepth:
		# print("increased")
		increasedDepth += 1
	# else:
		# print("decreased")
	currentdepth = int(line)
print(increasedDepth)


def windowsorting(starting, ending):
	window = []
	if ending + 1 <= len(filecontentlist):
		for i in range(starting, ending + 1):
			window.append(filecontentlist[i])
	else:
		return False
	return window

starting = 0
ending = 2
totalwindows = []
for count, line in enumerate(filecontent):
	window = windowsorting(starting, ending)
	if window != False:
		totalwindows.append(window)
		starting += 1
		ending += 1

# print(totalwindows)

totalwindowsum = []
for window in totalwindows:
	windowcount = 0
	for depth in window:
		windowcount += depth
	totalwindowsum.append(windowcount)
	
# print(totalwindowsum)
currentwindowdepth = 0
increasedwindowdepth = 0
for windowdepth in totalwindowsum:
	if windowdepth > currentwindowdepth:
		increasedwindowdepth += 1
	currentwindowdepth = windowdepth

print(increasedwindowdepth)