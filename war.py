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
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]

playerList = [playerOne, playerTwo]
class Upgrade:
    def __init__(self, location):
        self.location = location

    def move(self, moveLocation):
        self.location = moveLocation

class Beacon(Upgrade):
    acounter = 1
    bcounter = 1
    alist = []
    blist = []

    def __init__(self, location):
        super().__init__(location)


class Farm:
    def __init__(self, location):


class Creature:
    acounter =1
    bcounter = 1
    alist = []
    blist = []
    creatureLists = [alist, blist]

    def __init__(self, player, coordsArray):
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
        self.x_coord = coordsArray[0]
        self.y_coord = coordsArray[1]
        gameboard[self.x_coord][self.y_coord] = self

    def move(self, xcoord, ycoord):
        gameboard[self.x_coord][self.y_coord] = 0
        self.x_coord = xcoord
        self.y_coord = ycoord
        gameboard[self.x_coord][self.y_coord] = self

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


def moveCreature(player, cx, cy, dx, dy):
    if (gameboard[cx][cy] in Creature.creatureLists[player-1]):
        if (gameboard[dx][dy] == 0 and abs(cx-dx)< 2 and abs(cy-dy)<2):
            gameboard[cx][cy].move(dx,dy)
        else:
            print("you can't move there")
            return True
    else:
        print("You didn't select a character")
        return True

def placeBlock(player, cx, cy, bx, by):
    if (playerList[player-1].gameObjects[0][1] > 0 and type(gameboard[bx][by]) is int and gameboard[cx][cy] in Creature.creatureLists[player-1]):
        x_seperation = abs(cx-bx)
        y_seperation = abs(cy - by)
        if (x_seperation + y_seperation == 0 or x_seperation> 1 or y_seperation > 1):
            return True
        else:
            gameboard[bx][by] += 1
    else: return True

def upgradeBlock(player, upgrade, cx, cy, bx, by):
    if (playerList[player-1].gameObjects[upgrade][1]==0 or type(gameboard[bx][by]) is not int):
        return True
    elif (gameboard[bx][by] > 2):


    else: return True

def purchaseItem(item, player):
    if (player == 1):
        return playerOne.purchaseItem(item)
    if (player == 2):
        return playerTwo.purchaseItem(item)


creature1 = Creature(1, [1, 1])

while(running):
    currentPlayer = turn%2+1

    print("Player "+str(currentPlayer)+" Stuff:")
    print("money: " + str(playerList[currentPlayer - 1].money))
    for i in range(10):
        print(itemnamelist[i] + ": " + str(playerList[currentPlayer - 1].gameObjects[i][1]))

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
                print("Failed to place block.")
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
