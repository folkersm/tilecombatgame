import numpy
#import kivy
ccounter =0







class Creature:
    acounter =1
    bcounter = 1
    alist = []
    blist = []


    def __init__(self, player):
        self.owner = player

        if(player == 1):
            self.id = Creature.acounter
            Creature.acounter += 1
            Creature.alist.append(self)
        if (player == 2):
            self.id = Creature.bcounter
            Creature.bcounter += 1
            Creature.blist.append(self)
        self.x_coord = -1
        self.y_coord = -1

    def move(self, xcoord, ycoord):
        self.x_coord = xcoord
        self.y_coord = ycoord

# x = Creature(1)
# sdfasdfwer = Creature(1)
# rasdf = Creature(1)
# werwer = Creature(1)
# asdfasdfwe = Creature(2)
# print(Creature.blist)

running = True
turn = 0
oneprompt = "Player 1, enter a command:"
twoprompt = "Player 2, enter a command:"
statement = ""
gameboard = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,Creature(1),0,0,0,0,0],
             [0,0,0,0,0,0,0]]
def moveCreature(player, cx, cy, dx, dy):
    if (player == 1):
        if (gameboard[cx][cy] in Creature.alist):
            if (gameboard[dx][dy] == 0):
                tempcreature = gameboard[cx][cy]
                tempcreature.move(dx, dy)
                gameboard[dx][dy] = tempcreature
                gameboard[cx][cy] = 0
        else: print("You didn't select a character")
    elif (player == 2):
        if (gameboard[cx][cy] in Creature.alist):
            pass
        else: print("You didn't select a character")
    else: print("player selection error")

while(running):
    print(numpy.matrix(gameboard))
    if (turn%2 == 0): statement=oneprompt
    else: statement = twoprompt
    move = input(statement)
    infoturn = move.split(" ")

    if (move == "stop"):
        running = False
    else:
        if (infoturn[0] == "M"):
            moveCreature(turn%2+1, int(infoturn[1]), int(infoturn[2]), int(infoturn[3]), int(infoturn[4]))
        elif (infoturn[0] == "P"):
            print("You passed")
        else:
            print("Not a valid command")
            turn -= 1
    turn += 1










