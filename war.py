import numpy
import random
#import kivy
ccounter =0

itemnamelist = ["block", "farm", "armory", "beacon", "armorHand", "knife", "tool", "armorBody", "person", "gun"]
class Player:
    def __init__(self):
        self.money = 3
        self.gameObjects = [["block",8,3],["farm",2,3],["armory",2,3],["beacon",2,5],["armorHand",0,3],["knife",0,3],["tool",0,3],["armorBody",0,3],["person",0,2],["gun",0,3]]


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
upgradeList = ["F", "A", "B"]
class Upgrade:
    def __init__(self, id, player):
        self.id = id
        self.in_stash = True
        self.player = player

    def move(self, moveLocation, player):
        if (type(gameboard[moveLocation[0]][moveLocation[1]]) is int):
            if (gameboard[moveLocation[0]][moveLocation[1]] > self.id-1):
                playerList[player-1].gameObjects[self.id][1] -= 1
                self.block_base = gameboard[moveLocation[0]][moveLocation[1]]
                self.location = moveLocation
                self.in_stash = False
                gameboard[moveLocation[0]][moveLocation[1]] = self
            else: return True
        else: return True

    def put_in_stash(self, player):
        playerList[player-1].gameObjects[self.id][1] += 1
        self.in_stash = True

    def show(self):
        if (self.id != 1):
            return " " + str(upgradeList[self.id-1]) + str(self.player)

class Beacon(Upgrade):
    acounter = 0
    bcounter = 0
    counts = [acounter, bcounter]

    def __init__(self, player):
        super().__init__(3, player)
        Beacon.counts[player-1] += 1

gameboard[3][3] = Beacon(1)
gameboard[10][3] = Beacon(2)


class Farm(Upgrade):
    probability_to_grow = [0, 1/4, 1/8, 1/16, 0]
    yeild = [0, 0, 1, 2, 4]
    def __init__(self, player):
        super().__init__(1, player)
        self.phase = 1
        self.stage = 0

    def harvest(self, player):
        playerList[player - 1].money += Farm.yeild[self.stage]
        self.stage = 0
        self.phase = 0

    def grow(self):
        if (self.stage == 0):
            self.stage += 1
        else:
            if (random.random() < self.phase * Farm.probability_to_grow[self.stage]):
                self.phase = 0
                self.stage += 1
            else: self.phase += 1
    def show(self):
        return " F" + str(self.stage)

class Armory(Upgrade):
    def __init__(self, player):
        super().__init__(2, player)

class Creature:
    counters = [1, 1]
    alist = []
    blist = []
    creatureLists = [alist, blist]

    def __init__(self, player):
        self.owner = player
        self.movement = True
        self.id = Creature.counters[player-1]
        Creature.counters[player-1] +=1
        Creature.creatureLists[player-1].append(self)

    def move(self, xcoord, ycoord):
        try:gameboard[self.x_coord][self.y_coord] = 0
        except:pass
        self.x_coord = xcoord
        self.y_coord = ycoord
        gameboard[self.x_coord][self.y_coord] = self

class Melee(Creature):
    def __init__(self, player):
        super().__init__(player)



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
    distance_factor = True
    if (abs(cx-bx) < 2 and abs(cy-by) < 2 and abs(cx-bx) + abs(cy-by) != 0):
        distance_factor = False
    if (playerList[player-1].gameObjects[upgrade][1]==0 or type(gameboard[bx][by]) is not int or distance_factor):
        return True
    else:
        if (upgrade == 1):
            if (playerList[player-1].gameObjects[upgrade][1] > 0):
                Farm(player).move([bx, by], player)
            else: return True
        elif (upgrade == 2):
            if (playerList[player-1].gameObjects[upgrade][1] > 0):
                Armory(player).move([bx, by], player)
            else: return True
        elif (upgrade == 3):
            if (playerList[player-1].gameObjects[upgrade][1] > 0):
                Beacon(player).move([bx, by], player)
            else: return True
        else: return True

def harvest(player, cx, cy, bx, by):
    if (abs(cx - bx) < 2 and abs(cy - by) < 2 and type(gameboard[bx][by]) is Farm):
        gameboard[bx][by].harvest(player)
    else: return True

def grow(player, cx, cy, bx, by):
    if (abs(cx - bx) < 2 and abs(cy - by) < 2 and type(gameboard[bx][by]) is Farm and gameboard[cx][cy].owner == player):
        gameboard[bx][by].grow()
    else: return True


def purchaseItem(item, player):
    if (player == 1):
        return playerOne.purchaseItem(item)
    if (player == 2):
        return playerTwo.purchaseItem(item)


creature1 = Creature(1)
creature1.move(0, 0)

while(running):
    #currentPlayer = turn%2+1
    currentPlayer = 1
    print("Player "+str(currentPlayer)+" Stuff:")
    print("money: " + str(playerList[currentPlayer - 1].money))
    for i in range(10):
        print(itemnamelist[i] + ": " + str(playerList[currentPlayer - 1].gameObjects[i][1]))

    for i in range(14):
        row_string = ""
        for j in range(7):
            if (type(gameboard[i][j]) is int):
                row_string += " 0" + str(gameboard[i][j])[-1]
            else:
                if type(gameboard[i][j]) is Creature:
                    row_string += " C" + str(gameboard[i][j].owner)
                else: row_string += gameboard[i][j].show()
        print(row_string)
    if (currentPlayer == 1): statement=oneprompt
    else: statement = twoprompt
    move = input(statement)
    turn_info = move.split(" ")

    if (move == "stop"):
        running = False
    else:
        if (turn_info[0] == "M"):
            if moveCreature(currentPlayer, int(turn_info[1]), int(turn_info[2]), int(turn_info[3]), int(turn_info[4])):
                turn -= 1
                print("movement error #1")#                                                                                                                                                         Error 1
        elif (turn_info[0] == "B"):
            if(placeBlock(currentPlayer, int(turn_info[1]), int(turn_info[2]), int(turn_info[3]), int(turn_info[4]))):
                turn -= 1
                print("Failed to place block.")
        elif (turn_info[0] == "P"):
            print("You passed")
        elif (turn_info[0] == "S"):
            if(purchaseItem(int(turn_info[1]), currentPlayer) > 0):
                turn -= 1
                print("Not enough money")
        elif (turn_info[0] == "U"):
            if(upgradeBlock(currentPlayer, int(turn_info[1]), int(turn_info[2]),int(turn_info[3]),int(turn_info[4]),int(turn_info[5]))):
                turn -= 1
                print("upgrade " + itemnamelist[int(turn_info[1])] + " failed")
        elif (turn_info[0] == "G"):
            if(grow(currentPlayer, int(turn_info[1]), int(turn_info[2]), int(turn_info[3]), int(turn_info[4]))):
                print("Farm grow failed.")
                turn -= 1
        elif (turn_info[0] == "H"):
            if(harvest(currentPlayer, int(turn_info[1]), int(turn_info[2]), int(turn_info[3]), int(turn_info[4]))):
                print("Farm Harvest failed.")
                turn -= 1

        else:
            print("Not a valid command")
            turn -= 1
    turn += 1
