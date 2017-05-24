from tournament import Tournament
from ping_thing import PingThing

#This script collects the parameters for a tournament from the user, then plays a tournament and spits out the result
queue = []
clone = bool(input("CLONE? "))
num_players = int(input("# of players: "))
if clone == False:
    for i in range(num_players):
        print("PROCESSS "+str(i))
        print("---NEW PINGTHING---")
        ip = input("IP: ")
        launch = int(input("LAUNCH: "))
        jump = int(input("JUMP: "))
        queue.append(PingThing(ip=ip, launch=launch, jump=jump))
if clone == True:
    print("PROCESS == ALL")
    print("---PINGTHING TEMPLATE---")
    ip = input("IP: ")
    launch = int(input("LAUNCH: "))
    jump = int(input("JUMP: "))
    for i in range(num_players):
        queue.append(PingThing(ip=ip,launch=launch, jump=jump))
num_plays = int(input("# of plays per game: "))
print("---RUNNING---")
winner = Tournament(queue=queue, num_plays=num_plays)
print("---TOURNAMENT RESULT---")
print("WINNER:")
winner.print_info()