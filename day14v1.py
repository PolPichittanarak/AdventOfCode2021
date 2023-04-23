from collections import Counter
import string

lines = [line.strip() for line in open('day14.txt', 'r').readlines()]
template = lines[0]
#NNCB
rules = [rule.split(' ') for rule in lines[2:]]
rules = {a: (a[0]+c,c+a[1]) for a,b,c in rules} # dictionary pair {'NN': "NC", "CN"}
pairs = [''.join(p) for p in zip(template, template[1:])] #pair up first letter and second letter

#1 pair up letters
#2 check for insertion
#3 new pair of letter
#4 relate pair to the rule pairs and then count as the pair will always be in the rule book
#5 count character by iterating through each items or rule pairs
#6 first letter is always the start of next so only countthe first and do the last seperately


#rpc for rule pairs count
#ctr for string pair count

ctr = Counter(pairs)


for i in range(40):
	rpc = {key: 0 for key in rules.keys()} #keys() iterable object containing keys of the dict # rules pair based
	
	for (key, value) in ctr.items(): #ctr.items(): [('NN', 1), ('NC', 1), ('CB', 1)]
		rpc[rules[key][0]] += value # insertion - pair value incremented
		rpc[rules[key][1]] += value
	ctr = rpc
	#print(ctr)

char_count = {char: 0 for char in list(string.ascii_uppercase)}
for (key, value) in ctr.items():
	char_count[key[0]] += value

#last letter
char_count[template[-1]] += 1

max = max(char_count.values())
min = min([value for value in char_count.values() if value != 0])
print(max-min)

