


pos_player1 = 8
pos_player2 = 9

score_player1 = 0
score_player2 = 0

totalrolls = 0

player = 1
rolls = [1, 2, 3]
while score_player1 < 1000 and score_player2 < 1000:
	print("player" + str(player) + "'s turn")
	
	print("rolls: ", rolls)
	steps = sum(rolls)
	if player == 1:
		pos_player1 = (pos_player1 + steps)%10
		if pos_player1 == 0:
			score_player1 += 10
		else:
			score_player1 += pos_player1
		print("player1_score = ", str(score_player1))
	else:
		pos_player2 = (pos_player2 + steps)%10
		if pos_player2 == 0:
			score_player2 += 10
		else:
			score_player2 += pos_player2
		print("player2_score ", str(score_player2))
	
	for i in range(len(rolls)):
		rolls[i] = rolls[i] + 3
		if rolls[i] > 100:
			rolls[i] = rolls[i] - 100
		
	totalrolls += 3

	if player == 1:
		player = 2
	else:
		player = 1

print(score_player1)
print(score_player2)
print(totalrolls)