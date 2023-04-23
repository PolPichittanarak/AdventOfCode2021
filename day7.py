'''
from time import sleep
	
WAIT = 0.3

def my_print(d=0, *string):
	"""Print and wait"""
	s = " ".join(map(str, string))
	print("\t"*d, s)
	sleep(WAIT)
'''


def merge(list1, list2):

	merged = []
	while len(list1) and len(list2):
		if list1[0] < list2[0]:
			merged.append(list1.pop(0))
		else:
			merged.append(list2.pop(0))

	if len(list1):
		merged += list1

	elif len(list2):
		merged += list2
	
	return merged
	
	   
def merge_sort(my_list):
	
	mid = len(my_list) // 2
	left = my_list[:mid]
	right = my_list[mid:]	

	if len(left) > 1:
		left = merge_sort(left)
	
	if len(right) > 1:
		right = merge_sort(right)

	return merge(left, right)
	

	

	
if __name__ == "__main__":

	file = open("day7.txt" , "r")
	position = file.readlines()
	crab = list(position[0].split(","))
	crabfinal = []
	for c in crab:
		crabfinal.append(int(c))


	#print(crabfinal)
	sorted_list = merge_sort(crabfinal)
	#print(sorted_list)
	#print(len(sorted_list))
	fuel = 0
	'''
	for i, crab in enumerate(sorted_list):
		fuel = fuel + abs(crab - 333)
		#if i == 449 or i == 500:
			#print("median ",str(crab))
	print(fuel)
'''
	#positon = 308\\

	# mean position = 465

	for crab in sorted_list:
		different = abs(crab - 464)
		i = 1
		for distance in range(different):
			fuel += i
			i += 1
		
print(fuel)

