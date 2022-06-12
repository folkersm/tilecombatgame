import numpy
#import kivy
ccounter =0

itemnamelist = ["block", "farm", "armory", "beacon", "armorHand", "knife", "tool", "armorBody", "person", "gun"]
class Player:
    def __init__(self):
        self.money = 3
        self.gameObjects = [["block",0,3],["farm",0,3],["armory",0,3],["beacon",0,5],["armorHand",0,3],["knife",0,3],["tool",0,3],["armorBody",0,3],["person",0,2],["gun",0,3]]


    def purchaseItem(self, item):
        if (item == 3):
            self.gameObjects[3][2] = 5*self.gameObjects[3][1] + 5
        if (item == 8):
            self.gameObjects[8] = 2*self.gameObjects[8][1]
        if (self.money >= self.gameObjects[item][2]):
            self.money -= self.gameObjects[item][2]
            self.gameObjects[item][1] += 1
            return -1
        else: return self.gameObjects[item+1]

playerOne = Player()
playerTwo = Player()

class Creature:
    acounter =1
    bcounter = 1
    alist = []
    blist = []

    def __init__(self, player):
        self.owner = player
        self.blockmove = True
        self.movement = True
        self.attack = True

        if(player == 1):
            self.id = Creature.acounter
            Creature.acounter += 1
            Creature.alist.append(self)
        if (player == 2):
            self.id = Creature.bcounter
            Creature.bcounter += 1
            Creature.blist.append(self)
        self.x_coord = -10
        self.y_coord = -10

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
gameboard = [[Creature(1),0,0,0,0,0,0],
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
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]

def moveCreature(player, cx, cy, dx, dy):
    if (player == 1):
        if (gameboard[cx][cy] in Creature.alist):
            if (gameboard[dx][dy] == 0 and abs(cx-dx)< 2 and abs(cy-dy)<2):
                tempcreature = gameboard[cx][cy]
                tempcreature.move(dx, dy)
                gameboard[dx][dy] = tempcreature
                gameboard[cx][cy] = 0
            else:
                print("you can't move there")
                return True
        else:
            print("You didn't select a character")
            return True
    elif (player == 2):
        if (gameboard[cx][cy] in Creature.blist):
            if (gameboard[dx][dy] == 0 and abs(cx - dx) < 2 and abs(cy - dy) < 2):
                tempcreature = gameboard[cx][cy]
                tempcreature.move(dx, dy)
                gameboard[dx][dy] = tempcreature
                gameboard[cx][cy] = 0
            else:
                print("you can't move there")
                return True
        else:
            print("You didn't select a character")
            return True
    else:
        print("player selection error")
        return True

def placeBlock(player, cx, cy, bx, by):
    if(player ==1):
        x_seperation = abs(cx-bx)
        y_seperation = abs(cy - by)
        if (isinstance(gameboard[bx][by], int) and x_seperation <2 and y_seperation <2 and (x_seperation!=0 and y_seperation !=0)):
            gameboard[bx][by] += 1
        else:
            return True

def purchaseItem(item, player):
    if (player == 1):
        return playerOne.purchaseItem(item)
    if (player == 2):
        return playerTwo.purchaseItem(item)


playerList = [playerOne, playerTwo]


while(running):
    currentPlayer = turn%2+1

    print("Player "+str(currentPlayer)+" Stuff:")
    print("money: " + str(playerList[currentPlayer - 1].money))
    for i in range(10):
        print(itemnamelist[i] + ": " + str(playerList[currentPlayer - 1].gameObjects[2 * i]))

    print(numpy.matrix(gameboard))
    if (turn%2 == 0): statement=oneprompt
    else: statement = twoprompt
    move = input(statement)
    infoturn = move.split(" ")

    if (move == "stop"):
        running = False
    else:
        if (infoturn[0] == "M"):
            if moveCreature(currentPlayer, int(infoturn[1]), int(infoturn[2]), int(infoturn[3]), int(infoturn[4])):
                turn -= 1
                print("movement error #1")#                                                                                                                                                         Error 1
        elif (infoturn[0] == "B"):
            if(placeBlock(currentPlayer, int(infoturn[1]), int(infoturn[2]), int(infoturn[3]), int(infoturn[4]))):
                turn -= 1
                print("you can't place a block there")
        elif (infoturn[0] == "P"):
            print("You passed")
        elif (infoturn[0] == "S"):
            if(purchaseItem(int(infoturn[1]), currentPlayer) > 0):
                turn -= 1
                print("Not enough money")
        else:
            print("Not a valid command")
            turn -= 1
    turn += 1
