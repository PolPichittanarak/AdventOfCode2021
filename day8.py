file = open("day8.txt", "r")
filecontent = file.readlines()
count = 0
totalCodeCount = 0
for line in filecontent:
	line = line.replace("\n", "")
	data = line.split(" | ")
	output = data[1]
	outputVal = output.split(" ")
	entry = data[0]
	'''
	uniqueVal = [2, 4, 3, 7]
	for value in outputVal:
		if len(value) in uniqueVal:
			count += 1
'''

	one = ""
	two = ""
	three = ""
	four = ""
	five = ""
	six = ""
	seven = ""
	eight = ""
	nine = ""
	zero = ""

	singleentry = sorted(entry.split(" "), key = len)
	print(singleentry)
	mm = "" #yes
	oo = "" #yes
	nn = "" #yes
	pp = "" #yes
	qq = ""
	rr = "" #yes
	ss = ""
	count = 1
	for val in singleentry:
		# change for to while and remove the val every time they are identified
		#print("turn: ", str(count))
		count += 1

		if len(val) == 2:
			one = val
			#print("1" , one)
	
		elif len(val) == 4:
			four = val
			#print("4", four)
		elif len(val) == 3:
			seven = val
			#print("7", seven)
			for letter in seven:
				if letter not in one[0] and letter not in one[1]:
					mm = letter
					#print(mm)
		elif len(val) == 7:
			eight = val
			#print("8", eight)



		# identify betweent two and five, find out which of 1 is which, Positional sentitive. 
		# elif len(val) == 5 and not (one[0] in val and one[1] in val):
			# five = val


		elif len(val) == 6 and not (one[0] in val and one[1] in val):
				six = val
				#print("6", six)
				for letter in eight:
					if letter not in val:
						oo = letter
						print(oo)

		elif len(val) == 5:
			
			if (one[0] in val and one[1] in val):
				three = val
				#print("3",three)
		

		elif len(val) == 6:
			ZeroCheck = False
			for letter in four:
				if letter not in val:
					ZeroCheck = True
			if ZeroCheck:
				zero = val
				#print("0", zero)
			else:
				nine = val
		#print()
	
	for letter in eight:
		if letter not in six:
			oo = letter
			

	for val in singleentry:
		if len(val) == 5 and val != three:
			if oo not in val:
				five = val
			else:
				two = val

	one = sorted(list(one))
	two = sorted(list(two))
	three = sorted(list(three))
	four = sorted(list(four))
	five = sorted(list(five))
	six = sorted(list(six))
	seven = sorted(list(seven))
	eight = sorted(list(eight))
	nine = sorted(list(nine))
	zero = sorted(list(zero))
	
	finalOutputCode = ""

	for digit in outputVal:
		digit = sorted(list(digit))
	

		if digit == one:
			finalOutputCode = finalOutputCode + "1"
		
		elif digit == two:
			finalOutputCode = finalOutputCode + "2"
	
		elif digit == three:
			finalOutputCode = finalOutputCode + "3"
	
		elif digit == four:
			finalOutputCode = finalOutputCode + "4"

		elif digit == five:
			finalOutputCode = finalOutputCode + "5"

		elif digit == six:
			finalOutputCode = finalOutputCode + "6"

		elif digit == seven:
			finalOutputCode = finalOutputCode + "7"
		
		elif digit == eight:
			finalOutputCode = finalOutputCode + "8"

		elif digit == nine:
			finalOutputCode = finalOutputCode + "9"
		
		elif digit == zero:
			finalOutputCode = finalOutputCode + "0"

	
	print(int(finalOutputCode))
	totalCodeCount += int(finalOutputCode)
print(totalCodeCount)

'''
for letter in seven:
	if letter != oo and letter != mm:
		rr = letter
	
for letter in eight:
	if letter not in zero:
		pp = letter
for letter in four:
	if (letter != pp and letter != oo) and letter != rr:
		nn = letter

for letter in three:
	if (letter != mm and letter != oo) and (letter != pp and letter != rr):
		ss = letter
			
for letter in eight:
	if letter not in nine:
		qq = letter
				

	print("1" , one)
	print("2", two)
	print("3",three)
	print("4", four)
	print("5", five)
	print("6", six)
	print("7", seven)
	print("8", eight)
	print("9", nine)
	print("0", zero)
	# print(count)

print()
print(mm)
print(oo)
print(rr)
print(pp)
print(nn)
print(ss)
print(qq)
'''

#   mmmm
#  n    o
#  n    o
#   pppp
#  q    r
#  q		r
#	  ssss