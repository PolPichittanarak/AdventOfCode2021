ch = [i for i in open("day10.txt", 'r').read().strip().splitlines()]

d = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
incom = []
invalid = []
invalid_pos = []
# fill up stack, and check if next is closing bracket, if so, pop() (remove from top)
#print(list(enumerate(ch)))
for j,c in enumerate(ch):
	#print(j)
	stack = []
	for i,b in enumerate(c):
		#print()
		#print("Iteration num: ", str(i))
		#print("b is currently: ", b)
		if b not in d.values(): #the .values() part is basically the closer and if b is not in d.values() then it is not the closer
		#.values return an object list so essentially in this case it currently represents [')', ']', '}', '>']
		# it is an opener

		#print("condition 1: the iterator is an opener because b not in d.values when b:", b, "so b added to stack")
			stack.append(b)
		elif b in d.values():
			if b == d[stack[-1]]: #print("condition 2: the iterator is a closer beceause b in d.values when b:", b)
				stack.pop() #print("d[stack[-1]] is currently:", d[stack[-1]], "and is popped")
			else:
				# found invalid closing bracket
				#print("invalid when b:", b)
				invalid.append(b)
				invalid_pos.append(j)
				break
		#print("stack:", stack)
	incom.append(stack)
print(sum(list(points[i] for i in invalid)))

allscores = []
points = {')': 1, ']': 2, '}': 3, '>': 4}
for m,n in enumerate(incom):
	if m not in invalid_pos:
		#print(n)
		score = 0 
		closertags = []
		for e in range(len(n)-1, -1, -1):
			opener = n[e]
			closertags.append(d[opener])
		#print("closertags: ", closertags)
		for closer in closertags:
			score = (score * 5) + points[closer]
		allscores.append(score)
allscores = sorted(allscores)
print(allscores)
print(len(allscores))
print(allscores[len(allscores)//2])
			
		
		