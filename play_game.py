from ping_thing import PingThing

#Runs a game with two players, represented by Pingthings
#Players score points when they do not receive a response for their ping
#num_plays determines the number of games played
#if there is a tie, a game with the same settings repeats
def PlayGame (num_plays = 1, player1 = PingThing, player2 = PingThing):
	sum1 = 0
	sum2 = 0
	for i in range(num_plays):
		while True:
			if player1.play() == True:
				sum1 += 1
				break
			if player2.play() == True:
				sum2 += 1
				break
	print("---GAME---")
	print("Score: "+str(sum1)+"-"+str(sum2))
	if sum1 == sum2:
		print ("---TIE---")
		return PlayGame(num_plays, player1, player2)
	if sum1 > sum2:
		print("---PLAYER 1 WINS---")
		player1.purge()
		player2.purge()
		return player1
	if sum1 < sum2:
		print("---PLAYER 2 WINS---")
		player1.purge()
		player2.purge()
		return player2