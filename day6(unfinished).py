'''
file = open("day6.txt", "r")
filecontent = file.readlines()
fish = []
for i in filecontent[0]:
	if i != ",":
		fish.append(int(i))
'''

def BabyCount(day, life):
	day = day - life
	for d in range(day):
		BabyNum = BabyCount(d, )
	return baby

fish = [3]

for day in range(50):
	print("day: ", str(day))
	for f in range(len(fish)):
		fish[f] = fish[f] - 1
		if fish[f] == -1:
			fish.append(8)
			fish[f] = 6

print(len(fish))