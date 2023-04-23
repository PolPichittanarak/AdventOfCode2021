import collections
file = open("day14.txt", "r")
filecontent = file.readlines()
modcodes = []
identifier_pairs = []
for i, line in enumerate(filecontent):
	if i == 0:
		init_polymer = line.strip()
	elif line == "\n":
		pass
	else:
		linecontent = line.split(" -> ")
		identifier_pairs.append(linecontent[0])
		modcodes.append(linecontent[1].strip())
	
		

print(init_polymer)
print(modcodes)
print(identifier_pairs)


for count in range(40):
	print(count)
	st_monomer = 0
	en_monomer = 1
	final_polymer = ""
	for j in range(len(init_polymer) - 1):
		polymerpair = init_polymer[st_monomer] + init_polymer[en_monomer]
		for k, pair in enumerate(identifier_pairs):
			if polymerpair == pair:
				addmonomer = modcodes[k]
		final_polymer = final_polymer + init_polymer[st_monomer] + addmonomer
		if j == len(init_polymer) - 2:
			final_polymer += init_polymer[en_monomer]
	
				
		#print(polymerpair, end = "  ")
		#print(addmonomer)
	
	
				
		st_monomer, en_monomer = st_monomer + 1, en_monomer + 1
	
	
	init_polymer = final_polymer 
#print(final_polymer)
x = collections.Counter(final_polymer).most_common()
print(x)
