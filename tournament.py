from play_game import PlayGame
from ping_thing import PingThing
from utilities import array_spread

#Runs a tournament of games between an array of players, where players fight to the top
def Tournament(queue = [PingThing], num_plays = 1):
    print(queue)
    left = 0
    right = len(queue)-1
    middle = (left+right)/2
    if len(queue)==0:
        print("FAIL")
        return -1
    if len(queue) == 1:
        return queue[0]
    if len(queue) == 2:
        return PlayGame(num_plays=num_plays,player1=queue[0], player2=queue[1])
    if len(queue) > 2:
        return Tournament([Tournament(array_spread(queue,left,middle+1),num_plays=num_plays), Tournament(array_spread(queue,middle+1,right+1),num_plays=num_plays)])