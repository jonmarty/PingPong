from os import system
from random import choice


# PingThing is an object that jumps from one port of an IP to another
# pinging them until if finds a port that does not respond
class PingThing():
    def __init__(self, ip: str, launch: int, jump: int = 1):
        self.jump = jump
        self.ip = ip
        self.launch = launch
        self.target = launch

    # Jumps to a port, pings it, and returns true if the port cannot be reached
    def play(self):
        self.target += self.jump * choice([1, -1])#jumps the PingThing (jump) ports up or down
        out = system('ping -c 1 ' + self.ip + '.' + str(self.target)) #Pings the (target) IP
        if out != 0: #i.e. the port did not recieve the ping
            return True
        return False

    def purge(self):
        self.target = self.launch

    # Prints information about a PingThing
    def print_info(self):
        print("---PINGTHING---")
        print("IP = " + str(self.ip))#The IP the PingThing is aimed at
        print("Launch = "+str(self.launch))#The port the PingThing was originally launched at
        print("Jump = "+str(self.jump))#The port the PingThing jumps (up or down) each play