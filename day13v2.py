coords, fold = open("day13.txt", 'r').read().split('\n\n')
coords = {(int(i[0]), int(i[1])) for i in [i.split(',') for i in coords.split()]}
#print(coords)



fold = [{'axis':j.split('=')[0],'line':int(j.split('=')[1])} for j in \
    [i.split(' ')[2] for i in fold.split('\n')]]



origami = [list(coords)]


for i, f in enumerate(fold):    
	
	no = set()
	for (x,y) in origami[-1]:
		if f['axis'] == 'y' and y > f['line']: 
			y = (2*f['line']) - y
		elif f['axis'] == 'x' and x > f['line']:
			x = (2*f['line']) - x
			
		no.add((x,y))
		
	origami.append(no)
	if i == 0:
		print(len(origami[-1]))
	
print(sorted(origami[-1]))


mr = max([spot[1] for spot in origami[-1]])
mc = max([spot[0] for spot in origami[-1]])

for row in range(mr + 1):
	for cell in range(mc + 1):
		if (cell, row) in origami[-1]:
			print("#", end = "")
		else:
			print(".", end = "")
	print()

#BCZRCEAB
	



