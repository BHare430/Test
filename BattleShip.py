import random


class BattleShipBoard():
    def __init__(self):
        self.LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.setBoardPlayer()
        self.setBoardAI()
        self.options = []
        self.optionsAI = []
        self.count = 0
        self.playerShots = []
        self.AIShots = []
        print(self)
        input("Press any button to begin: ")
        print("You will now be asked to place your ships.")
        #Battleship create method
        self.playerBrow = 0
        self.playerBcol = "A"
        self.playerBS = []
        self.playerBdir = 0
        #Cruiser
        self.playerCrow = 0
        self.playerCcol = "A"
        self.playerC = []
        self.playerCdir = 0
        #Sub
        self.playerSrow = 0
        self.playerScol = "A"
        self.playerS = []
        self.playerSdir = 0
        #Carrier
        self.playerACrow = 0
        self.playerACcol = "A"
        self.playerAC = []
        self.playerACdir = 0
        #PT
        self.playerProw = 0
        self.playerPcol = "A"
        self.playerPT = []
        self.playerPdir = 0
        self.setPlayerShips()
        #Battleship
        self.AIBrow = 0
        self.AIBcol = "A"
        self.AIBS = []
        self.AIBdir = 0
        #Cruiser
        self.AICrow = 0
        self.AICcol = "A"
        self.AIC = []
        self.AICdir = 0
        #Sub
        self.AISrow = 0
        self.AIScol = "A"
        self.AIS = []
        self.AISdir = 0
        #Carrier
        self.AIACrow = 0
        self.AIACcol = "A"
        self.AIAC = []
        self.AIACdir = 0
        #PT
        self.AIProw = 0
        self.AIPcol = "A"
        self.AIPT = []
        self.AIPdir = 0
        print("The AI is now placing its ships...")
        #AI guessing variables
        self.AIlastShot = "miss"
        self.AIhitBS = []
        self.AIhitBSdir = None

        self.setAIships()
        #self.setBoardAI()
        input("The seas are set... Goodluck Captain! (press any button to continue): ")
        print(self)
        self.play()

    def play(self):
        print("Mission: Eliminate All Enemy Ships")
        while(self.finish() == 0):
            self.playerTurn()
            self.AITurn()
            print(self)
        print("Game Over")

    def finish(self):
        if len(self.AIBS) + len(self.AIC) + len(self.AIS) + len(self.AIAC) + len(self.AIPT) == 0:
            print("Congratulations Captain! The day is won!")
            return 1
        elif len(self.playerBS) + len(self.playerC) + len(self.playerS) + len(self.playerAC) + len(self.playerPT) == 0:
            print("Another Captain goes down with their ship.")
            return 2
        else:
            print("Next Salvo!")
            return 0

    def playerTurn(self):
        print("Awaiting your orders Captain!")
        shotrow = input("Input the column you wish to fire at: ").upper()
        shotcol = int(input("Input the row you wish to fire at: "))
        if self.LETTERS.__contains__(shotrow) and shotcol > 0 and shotcol < 11:
            current = [shotrow, shotcol]
            if self.playerShots.__contains__(current):
                print("The inputted coordinates have already been shot at, try again.")
                self.playerTurn()
            else:
                self.searchPlayer(current)
                self.playerShots.append(current)
        else:
            print("Invalid coordinates, please try again.")
            self.playerTurn()
    def searchPlayer(self, current):
        if self.AIBS.__contains__(current) or self.AIC.__contains__(current) or self.AIS.__contains__(current) or self.AIAC.__contains__(current) or self.AIPT.__contains__(current):
            print("Hit!")
            self.setHitPlayer(current)
            self.checkSinkPlayer(current)
        else:
            print("Miss!")
            self.setMissPlayer(current)
    def setHitPlayer(self, coords):
        for y in self.boardAI:
            if y[0] == coords[0]:
                y[coords[1]] = "[X]"
    def setMissPlayer(self, coords):
        for y in self.boardAI:
            if y[0] == coords[0]:
                y[coords[1]] = "[O]"
    def checkSinkPlayer(self, current):
        if self.AIBS.__contains__(current):
            if len(self.AIBS) == 1:
                print("Enemy Battleship sunk!")
                self.AIBS.pop()
            else:
                print("Enemy ship still floating")
                self.AIBS.pop(self.AIBS.index(current))
        elif self.AIC.__contains__(current):
            if len(self.AIC) == 1:
                print("Enemy Cruiser sunk!")
                self.AIC.pop()
            else:
                print("Enemy ship still floating")
                self.AIC.pop(self.AIC.index(current))
        elif self.AIS.__contains__(current):
            if len(self.AIS) == 1:
                print("Enemy Submarine sunk!")
                self.AIS.pop()
            else:
                print("Enemy ship still floating")
                self.AIS.pop(self.AIS.index(current))
        elif self.AIAC.__contains__(current):
            if len(self.AIAC) == 1:
                print("Enemy Aircraft Carrier sunk!")
                self.AIAC.pop()
            else:
                print("Enemy ship still floating")
                self.AIAC.pop(self.AIAC.index(current))
        elif self.AIPT.__contains__(current):
            if len(self.AIPT) == 1:
                print("Enemy PT Boat sunk!")
                self.AIPT.pop()
            else:
                print("Enemy ship still floating")
                self.AIPT.pop(self.AIPT.index(current))

    def AITurn(self):
        print("Shells Incoming!")
        AIShoot #checks last shot, checks direction, fires next shot
        










    def checkPlacePlayer(self):
        countBS = 0
        countC = 0
        countS = 0
        countAC = 0
        countPT = 0
        for y in self.boardPlayer:
            for x in y:
                if str(x) == "[B]":
                    countBS += 1
                elif str(x) == "[C]":
                    countC += 1
                elif str(x) == "[S]":
                    countS += 1
                elif str(x) == "[A]":
                    countAC += 1
                elif str(x) == "[P]":
                    countPT += 1
        if countBS != 4 or countC != 3 or countS != 3 or countAC != 5 or countPT != 2:
            print("Some of your pieces were not set up correctly, starting again...")
            self.setBoardPlayer()
            self.setPlayerships()

    def setPlayerShips(self):
        self.setPlayerBS()
        print(self)
        self.setPlayerC()
        print(self)
        self.setPlayerS()
        print(self)
        self.setPlayerAC()
        print(self)
        self.setPlayerPT()
        print(self)

    def setPlayerBS(self):
        self.playerBrow = str(input("Please enter the letter row you want to start your battleship on: ")).upper()
        self.playerBcol = int(input("Please enter the number column you want to start your battleship on: "))
        if(self.checkPos(1)):
            self.options = []
            print(self)
            if(self.checkDir(1)):
                print("Please enter the direction you want your battleship to go for 3 spaces (" + self.options.__str__() + "): ")
                direction = int(input("Enter an int from above: "))
                self.setDir(1, direction)
        else:
            print("Invalid location, try again.")
            self.setPlayerBS()

    def setPlayerC(self):
        self.playerCrow = str(input("Please enter the letter row you want to start your Cruiser on: ")).upper()
        self.playerCcol = int(input("Please enter the number column you want to start your Cruiser on: "))
        if(self.checkPos(2)):
            self.options = []
            print(self)
            if(self.checkDir(2)):
                print("Please enter the direction you want your Cruiser to go for 2 spaces (" + self.options.__str__() + "): ")
                direction = int(input("Enter an int from above: "))
                self.setDir(2, direction)
        else:
            print("Invalid location, try again.")
            self.setPlayerC()

    def setPlayerS(self):
        self.playerSrow = str(input("Please enter the letter row you want to start your Submarine on: ")).upper()
        self.playerScol = int(input("Please enter the number column you want to start your Submarine on: "))
        if (self.checkPos(3)):
            self.options = []
            print(self)
            if (self.checkDir(3)):
                print("Please enter the direction you want your Submarine to go for 2 spaces (" + self.options.__str__() + "): ")
                direction = int(input("Enter an int from above: "))
                self.setDir(3, direction)
        else:
            print("Invalid location, try again.")
            self.setPlayerS()

    def setPlayerAC(self):
        self.playerACrow = str(input("Please enter the letter row you want to start your Aircraft Carrier on: ")).upper()
        self.playerACcol = int(input("Please enter the number column you want to start your Aircraft Carrier on: "))
        if (self.checkPos(4)):
            self.options = []
            print(self)
            if (self.checkDir(4)):
                print("Please enter the direction you want your Aircraft Carrier to go for 4 spaces (" + self.options.__str__() + "): ")
                direction = int(input("Enter an int from above: "))
                self.setDir(4, direction)
        else:
            print("Invalid location, try again.")
            self.setPlayerAC()

    def setPlayerPT(self):
        self.playerPTrow = str(input("Please enter the letter row you want to start your PT boat on: ")).upper()
        self.playerPTcol = int(input("Please enter the number column you want to start your PT boat on: "))
        if (self.checkPos(5)):
            self.options = []
            print(self)
            if (self.checkDir(5)):
                print("Please enter the direction you want your PT boat to go for 1 space (" + self.options.__str__() + "): ")
                direction = int(input("Enter an int from above: "))
                self.setDir(5, direction)
        else:
            print("Invalid location, try again.")
            self.setPlayerPT()

    def setDir(self, ship, direction):
        length = 0
        if ship == 1:
            length = 3
            for x in range(length):
                if direction == 0:
                    self.playerBrow = self.LETTERS[self.LETTERS.index(self.playerBrow) + 1]
                elif direction == 2:
                    self.playerBcol += 1
                elif direction == 1:
                    self.playerBrow = self.LETTERS[self.LETTERS.index(self.playerBrow) - 1]
                elif direction == 3:
                    self.playerBcol -= 1
                self.checkPos(1)
        if ship == 2:
            length = 2
            for x in range(length):
                if direction == 0:
                    self.playerCrow = self.LETTERS[self.LETTERS.index(self.playerCrow) + 1]
                elif direction == 2:
                    self.playerCcol += 1
                elif direction == 1:
                    self.playerCrow = self.LETTERS[self.LETTERS.index(self.playerCrow) - 1]
                elif direction == 3:
                    self.playerCcol -= 1
                self.checkPos(2)
        if ship == 3:
            length = 2
            for x in range(length):
                if direction == 0:
                    self.playerSrow = self.LETTERS[self.LETTERS.index(self.playerSrow) + 1]
                elif direction == 2:
                    self.playerScol += 1
                elif direction == 1:
                    self.playerSrow = self.LETTERS[self.LETTERS.index(self.playerSrow) - 1]
                elif direction == 3:
                    self.playerScol -= 1
                self.checkPos(3)
        if ship == 4:
            length = 4
            for x in range(length):
                if direction == 0:
                    self.playerACrow = self.LETTERS[self.LETTERS.index(self.playerACrow) + 1]
                elif direction == 2:
                    self.playerACcol += 1
                elif direction == 1:
                    self.playerACrow = self.LETTERS[self.LETTERS.index(self.playerACrow) - 1]
                elif direction == 3:
                    self.playerACcol -= 1
                self.checkPos(4)
        if ship == 5:
            length = 1
            for x in range(length):
                if direction == 0:
                    self.playerPTrow = self.LETTERS[self.LETTERS.index(self.playerPTrow) + 1]
                elif direction == 2:
                    self.playerPTcol += 1
                elif direction == 1:
                    self.playerPTrow = self.LETTERS[self.LETTERS.index(self.playerPTrow) - 1]
                elif direction == 3:
                    self.playerPTcol -= 1
                self.checkPos(5)

    def checkDir(self, ship):
        if ship == 1:
            if self.playerBS[0][0] != "H" and self.playerBS[0][0] != "I" and self.playerBS[0][0] != "J":
                self.options.append("0: Down ")
            if self.playerBS[0][0] != "A" and self.playerBS[0][0] != "B" and self.playerBS[0][0] != "C":
                self.options.append("1: Up")
            if self.playerBS[0][1] != 10 and self.playerBS[0][1] != 9 and self.playerBS[0][1] != 8:
                self.options.append("2: Right")
            if self.playerBS[0][1] != 1 and self.playerBS[0][1] != 2 and self.playerBS[0][1] != 3:
                self.options.append("3: Left")
            if len(self.options) > 0:
                return True
        elif ship == 2:
            checkrow = None
            checkcol = None
            if self.playerC[0][0] != "I" and self.playerC[0][0] != "J":
                collision = 0
                for a in range(2):
                    checkrow = self.LETTERS[self.LETTERS.index(self.playerCrow) + 1 + a]
                    for l in self.playerBS:
                        if l[0] == checkrow and l[1] == self.playerCcol:
                            collision+=1
                if collision == 0:
                    self.options.append("0: Down ")
            if self.playerC[0][0] != "A" and self.playerC[0][0] != "B":
                collision = 0
                for b in range(2):
                    checkrow = self.LETTERS[self.LETTERS.index(self.playerCrow) - 1 - b]
                    for m in self.playerBS:
                        if m[0] == checkrow and m[1] == self.playerCcol:
                            collision += 1
                if collision == 0:
                    self.options.append("1: Up")
            if self.playerC[0][1] != 10 and self.playerC[0][1] != 9:
                collision = 0
                for c in range(2):
                    checkcol = self.playerCcol + 1 + c
                    for n in self.playerBS:
                        if n[1] == checkcol and n[0] == self.playerCrow:
                            collision += 1
                if collision == 0:
                    self.options.append("2: Right")
            if self.playerC[0][1] != 1 and self.playerC[0][1] != 2:
                collision = 0
                for d in range(2):
                    checkcol = self.playerCcol - 1 - d
                    for o in self.playerBS:
                        if o[1] == checkcol and o[0] == self.playerCrow:
                            collision += 1
                if collision == 0:
                    self.options.append("3: Left")
            if len(self.options) > 0:
                return True
        elif ship == 3:
            checkrow = None
            checkcol = None
            if self.playerS[0][0] != "I" and self.playerS[0][0] != "J":
                collision = 0
                for a in range(2):
                    checkrow = self.LETTERS[self.LETTERS.index(self.playerSrow) + 1 + a]
                    for l in self.playerBS:
                        if l[0] == checkrow and l[1] == self.playerScol:
                            collision += 1
                    for w in self.playerC:
                        if w[0] == checkrow and w[1] == self.playerScol:
                            collision += 1
                if collision == 0:
                    self.options.append("0: Down ")
            if self.playerS[0][0] != "A" and self.playerS[0][0] != "B":
                collision = 0
                for b in range(2):
                    checkrow = self.LETTERS[self.LETTERS.index(self.playerSrow) - 1 - b]
                    for m in self.playerBS:
                        if m[0] == checkrow and m[1] == self.playerScol:
                            collision += 1
                    for x in self.playerC:
                        if x[0] == checkrow and x[1] == self.playerScol:
                            collision += 1
                if collision == 0:
                    self.options.append("1: Up")
            if self.playerS[0][1] != 10 and self.playerS[0][1] != 9:
                collision = 0
                for c in range(2):
                    checkcol = self.playerScol + 1 + c
                    for n in self.playerBS:
                        if n[1] == checkcol and n[0] == self.playerSrow:
                            collision += 1
                    for y in self.playerC:
                        if y[1] == checkcol and y[0] == self.playerSrow:
                            collision += 1
                if collision == 0:
                    self.options.append("2: Right")
            if self.playerS[0][1] != 1 and self.playerS[0][1] != 2:
                collision = 0
                for d in range(2):
                    checkcol = self.playerScol - 1 - d
                    for o in self.playerBS:
                        if o[1] == checkcol and o[0] == self.playerSrow:
                            collision += 1
                    for z in self.playerC:
                        if z[1] == checkcol and z[0] == self.playerSrow:
                            collision += 1
                if collision == 0:
                    self.options.append("3: Left")
            if len(self.options) > 0:
                return True
        elif ship == 4:
            checkrow = None
            checkcol = None
            if self.playerAC[0][0] != "H" and self.playerAC[0][0] != "I" and self.playerAC[0][0] != "J" and self.playerAC[0][0] != "G":
                collision = 0
                for a in range(4):
                    checkrow = self.LETTERS[self.LETTERS.index(self.playerACrow) + 1 + a]
                    for l in self.playerBS:
                        if l[0] == checkrow and l[1] == self.playerACcol:
                            collision += 1
                    for w in self.playerC:
                        if w[0] == checkrow and w[1] == self.playerACcol:
                            collision += 1
                    for h in self.playerS:
                        if h[0] == checkrow and h[1] == self.playerACcol:
                            collision += 1
                if collision == 0:
                    self.options.append("0: Down ")
            if self.playerAC[0][0] != "A" and self.playerAC[0][0] != "B" and self.playerAC[0][0] != "C" and self.playerAC[0][0] != "D":
                collision = 0
                for b in range(4):
                    checkrow = self.LETTERS[self.LETTERS.index(self.playerACrow) - 1 - b]
                    for m in self.playerBS:
                        if m[0] == checkrow and m[1] == self.playerACcol:
                            collision += 1
                    for x in self.playerC:
                        if x[0] == checkrow and x[1] == self.playerACcol:
                            collision += 1
                    for i in self.playerS:
                        if i[0] == checkrow and i[1] == self.playerACcol:
                            collision += 1
                if collision == 0:
                    self.options.append("1: Up")
            if self.playerAC[0][1] != 10 and self.playerAC[0][1] != 9 and self.playerAC[0][1] != 8 and self.playerAC[0][1] != 7:
                collision = 0
                for c in range(4):
                    checkcol = self.playerACcol + 1 + c
                    for n in self.playerBS:
                        if n[1] == checkcol and n[0] == self.playerACrow:
                            collision += 1
                    for y in self.playerC:
                        if y[1] == checkcol and y[0] == self.playerACrow:
                            collision += 1
                    for j in self.playerS:
                        if j[1] == checkcol and j[0] == self.playerACrow:
                            collision += 1
                if collision == 0:
                    self.options.append("2: Right")
            if self.playerAC[0][1] != 1 and self.playerAC[0][1] != 2 and self.playerAC[0][1] != 3 and self.playerAC[0][1] != 4:
                collision = 0
                for d in range(4):
                    checkcol = self.playerACcol - 1 - d
                    for o in self.playerBS:
                        if o[1] == checkcol and o[0] == self.playerACrow:
                            collision += 1
                    for z in self.playerC:
                        if z[1] == checkcol and z[0] == self.playerACrow:
                            collision += 1
                    for k in self.playerS:
                        if k[1] == checkcol and k[0] == self.playerACrow:
                            collision += 1
                if collision == 0:
                    self.options.append("3: Left")
            if len(self.options) > 0:
                return True
        elif ship == 5:
            checkrow = None
            checkcol = None
            if self.playerPT[0][0] != "J":
                collision = 0
                for a in range(1):
                    checkrow = self.LETTERS[self.LETTERS.index(self.playerPTrow) + 1 + a]
                    for l in self.playerBS:
                        if l[0] == checkrow and l[1] == self.playerPTcol:
                            collision += 1
                    for w in self.playerC:
                        if w[0] == checkrow and w[1] == self.playerPTcol:
                            collision += 1
                    for h in self.playerS:
                        if h[0] == checkrow and h[1] == self.playerPTcol:
                            collision += 1
                    for e in self.playerAC:
                        if e[0] == checkrow and e[1] == self.playerPTcol:
                            collision += 1
                if collision == 0:
                    self.options.append("0: Down ")
            if self.playerPT[0][0] != "A":
                collision = 0
                for b in range(1):
                    checkrow = self.LETTERS[self.LETTERS.index(self.playerPTrow) - 1 - b]
                    for m in self.playerBS:
                        if m[0] == checkrow and m[1] == self.playerPTcol:
                            collision += 1
                    for x in self.playerC:
                        if x[0] == checkrow and x[1] == self.playerPTcol:
                            collision += 1
                    for i in self.playerS:
                        if i[0] == checkrow and i[1] == self.playerPTcol:
                            collision += 1
                    for f in self.playerAC:
                        if f[0] == checkrow and f[1] == self.playerPTcol:
                            collision += 1
                if collision == 0:
                    self.options.append("1: Up")
            if self.playerPT[0][1] != 10:
                collision = 0
                for c in range(1):
                    checkcol = self.playerPTcol + 1 + c
                    for n in self.playerBS:
                        if n[1] == checkcol and n[0] == self.playerPTrow:
                            collision += 1
                    for y in self.playerC:
                        if y[1] == checkcol and y[0] == self.playerPTrow:
                            collision += 1
                    for j in self.playerS:
                        if j[1] == checkcol and j[0] == self.playerPTrow:
                            collision += 1
                    for g in self.playerAC:
                        if g[1] == checkcol and g[0] == self.playerPTrow:
                            collision += 1
                if collision == 0:
                    self.options.append("2: Right")
            if self.playerPT[0][1] != 1:
                collision = 0
                for d in range(1):
                    checkcol = self.playerPTcol - 1 - d
                    for o in self.playerBS:
                        if o[1] == checkcol and o[0] == self.playerPTrow:
                            collision += 1
                    for z in self.playerC:
                        if z[1] == checkcol and z[0] == self.playerPTrow:
                            collision += 1
                    for k in self.playerS:
                        if k[1] == checkcol and k[0] == self.playerPTrow:
                            collision += 1
                    for u in self.playerAC:
                        if u[1] == checkcol and u[0] == self.playerPTrow:
                            collision += 1
                if collision == 0:
                    self.options.append("3: Left")
            if len(self.options) > 0:
                return True
        else:
            return False

    def checkPos(self, ship):#check if starting pos is valid, then create list of valid directions
        if ship == 1:
            for y in self.boardPlayer:
                if y[0] == self.playerBrow:
                    if self.playerBcol < 11 and self.playerBcol > 0:
                        y[self.playerBcol] = "[B]"
                        self.playerBS.append([self.playerBrow, self.playerBcol])
                        return True
        if ship == 2:
            for y in self.boardPlayer:
                if y[0] == self.playerCrow and y[self.playerCcol] != "[B]":
                    if self.playerCcol < 11 and self.playerCcol > 0:
                        y[self.playerCcol] = "[C]"
                        self.playerC.append([self.playerCrow, self.playerCcol])
                        return True
        elif ship == 3:
            for y in self.boardPlayer:
                if y[0] == self.playerSrow and y[self.playerScol] != "[B]" and y[self.playerScol] != "[C]":
                    if self.playerScol < 11 and self.playerScol > 0:
                        y[self.playerScol] = "[S]"
                        self.playerS.append([self.playerSrow, self.playerScol])
                        return True
        elif ship == 4:
            for y in self.boardPlayer:
                if y[0] == self.playerACrow and y[self.playerACcol] != "[B]" and y[self.playerACcol] != "[C]" and y[self.playerACcol] != "[S]":
                    if self.playerACcol < 11 and self.playerACcol > 0:
                        y[self.playerACcol] = "[A]"
                        self.playerAC.append([self.playerACrow, self.playerACcol])
                        return True
        elif ship == 5:
            for y in self.boardPlayer:
                if y[0] == self.playerPTrow and y[self.playerPTcol] != "[B]" and y[self.playerPTcol] != "[C]" and y[self.playerPTcol] != "[S]" and y[self.playerPTcol] != "[A]":
                    if self.playerACcol < 11 and self.playerPTcol > 0:
                        y[self.playerPTcol] = "[P]"
                        self.playerPT.append([self.playerPTrow, self.playerPTcol])
                        return True
        else:
            return False

    def setBoardPlayer(self):
        self.boardPlayer = []
        count = 0
        for y in range(11):
            self.inner = []
            if y == 0:
                for x in range(11):
                    if x == 0:
                        self.inner.append(" ")
                    else:
                        self.inner.append(x)
            else:
                for x in range(11):
                    if x == 0:
                        self.inner.append(self.LETTERS[count])
                        count += 1
                    else:
                        self.inner.append("[ ]")
            self.boardPlayer.append(self.inner)

    def setBoardAI(self):
        self.boardAI = []
        count = 0
        for y in range(11):
            self.inner = []
            if y == 0:
                for x in range(11):
                    if x == 0:
                        self.inner.append(" ")
                    else:
                        self.inner.append(x)
            else:
                for x in range(11):
                    if x == 0:
                        self.inner.append(self.LETTERS[count])
                        count += 1
                    else:
                        self.inner.append("[ ]")
            self.boardAI.append(self.inner)
    def setAIships(self):
        self.setAIBS(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1,10))
        self.setAIC(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1, 10))
        self.setAIS(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1, 10))
        self.setAIAC(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1, 10))
        self.setAIPT(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1, 10))
        print("Checking Placements")
        self.checkPlaceAI()

    def checkPlaceAI(self):
        countBS = 0
        countC = 0
        countS = 0
        countAC = 0
        countPT = 0
        for y in self.boardAI:
            for x in y:
                if str(x) == "[B]":
                    countBS += 1
                elif str(x) == "[C]":
                    countC += 1
                elif str(x) == "[S]":
                    countS += 1
                elif str(x) == "[A]":
                    countAC += 1
                elif str(x) == "[P]":
                    countPT += 1
        if countBS != 4 or countC != 3 or countS != 3 or countAC != 5 or countPT != 2:
            self.setBoardAI()
            self.setAIships()

    def setAIBS(self, letter, col):
        self.AIBrow = letter
        self.AIBcol = col
        if (self.checkPosAI(1)):
            self.optionsAI = []
            #print(self)
            if (self.checkDirAI(1)):
                directionAI = self.optionsAI[random.randint(0, len(self.optionsAI) - 1)]
                self.setDirAI(1, directionAI)
                #print(self)
        else:
            self.setAIBS(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1,10))

    def setAIC(self, letter, col):
        self.AICrow = letter
        self.AICcol = col
        if (self.checkPosAI(2)):
            self.optionsAI = []
            #print(self)
            if (self.checkDirAI(2)):
                directionAI = self.optionsAI[random.randint(0, len(self.optionsAI) - 1)]
                self.setDirAI(2, directionAI)
                #print(self)
        else:
            self.setAIC(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1,10))

    def setAIS(self, letter, col):
        self.AISrow = letter
        self.AIScol = col
        if (self.checkPosAI(3)):
            self.optionsAI = []
            #print(self)
            if (self.checkDirAI(3)):
                directionAI = self.optionsAI[random.randint(0, len(self.optionsAI) - 1)]
                self.setDirAI(3, directionAI)
                #print(self)
        else:
            self.setAIS(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1,10))

    def setAIAC(self, letter, col):
        self.AIACrow = letter
        self.AIACcol = col
        if (self.checkPosAI(4)):
            self.optionsAI = []
            #print(self)
            if (self.checkDirAI(4)):
                directionAI = self.optionsAI[random.randint(0, len(self.optionsAI) - 1)]
                self.setDirAI(4, directionAI)
                #print(self)
            else:
                self.setAIAC(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1, 10))
        else:
            self.setAIAC(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1,10))

    def setAIPT(self, letter, col):
        self.AIPTrow = letter
        self.AIPTcol = col
        if (self.checkPosAI(5)):
            self.optionsAI = []
            #print(self)
            if (self.checkDirAI(5)):
                directionAI = self.optionsAI[random.randint(0, len(self.optionsAI) - 1)]
                self.setDirAI(5, directionAI)
                #print(self)
        else:
            self.setAIPT(self.LETTERS[random.randint(0, len(self.LETTERS) - 1)], random.randint(1,10))

    def setDirAI(self, ship, direction):
        length = 0
        if ship == 1:
            length = 3
            for x in range(length):
                if direction == 0:
                    self.AIBrow = self.LETTERS[self.LETTERS.index(self.AIBrow) + 1]
                elif direction == 2:
                    self.AIBcol += 1
                elif direction == 1:
                    self.AIBrow = self.LETTERS[self.LETTERS.index(self.AIBrow) - 1]
                elif direction == 3:
                    self.AIBcol -= 1
                self.checkPosAI(1)
        if ship == 2:
            length = 2
            for x in range(length):
                if direction == 0:
                    self.AICrow = self.LETTERS[self.LETTERS.index(self.AICrow) + 1]
                elif direction == 2:
                    self.AICcol += 1
                elif direction == 1:
                    self.AICrow = self.LETTERS[self.LETTERS.index(self.AICrow) - 1]
                elif direction == 3:
                    self.AICcol -= 1
                self.checkPosAI(2)
        if ship == 3:
            length = 2
            for x in range(length):
                if direction == 0:
                    self.AISrow = self.LETTERS[self.LETTERS.index(self.AISrow) + 1]
                elif direction == 2:
                    self.AIScol += 1
                elif direction == 1:
                    self.AISrow = self.LETTERS[self.LETTERS.index(self.AISrow) - 1]
                elif direction == 3:
                    self.AIScol -= 1
                self.checkPosAI(3)
        if ship == 4:
            length = 4
            for x in range(length):
                if direction == 0:
                    self.AIACrow = self.LETTERS[self.LETTERS.index(self.AIACrow) + 1]
                elif direction == 2:
                    self.AIACcol += 1
                elif direction == 1:
                    self.AIACrow = self.LETTERS[self.LETTERS.index(self.AIACrow) - 1]
                elif direction == 3:
                    self.AIACcol -= 1
                self.checkPosAI(4)
        if ship == 5:
            length = 1
            for x in range(length):
                if direction == 0:
                    self.AIPTrow = self.LETTERS[self.LETTERS.index(self.AIPTrow) + 1]
                elif direction == 2:
                    self.AIPTcol += 1
                elif direction == 1:
                    self.AIPTrow = self.LETTERS[self.LETTERS.index(self.AIPTrow) - 1]
                elif direction == 3:
                    self.AIPTcol -= 1
                self.checkPosAI(5)

    def checkPosAI(self, ship):#check if starting pos is valid, then create list of valid directions
        if ship == 1:
            for y in self.boardAI:
                if y[0] == self.AIBrow:
                    if self.AIBcol < 11 and self.AIBcol > 0:
                        y[self.AIBcol] = "[B]"
                        self.AIBS.append([self.AIBrow, self.AIBcol])
                        return True
        if ship == 2:
            for y in self.boardAI:
                if y[0] == self.AICrow and y[self.AICcol] != "[B]":
                    if self.AICcol < 11 and self.AICcol > 0:
                        y[self.AICcol] = "[C]"
                        self.AIC.append([self.AICrow, self.AICcol])
                        return True
        elif ship == 3:
            for y in self.boardAI:
                if y[0] == self.AISrow and y[self.AIScol] != "[B]" and y[self.AIScol] != "[C]":
                    if self.AIScol < 11 and self.AIScol > 0:
                        y[self.AIScol] = "[S]"
                        self.AIS.append([self.AISrow, self.AIScol])
                        return True
        elif ship == 4:
            for y in self.boardAI:
                if y[0] == self.AIACrow and y[self.AIACcol] != "[B]" and y[self.AIACcol] != "[C]" and y[self.AIACcol] != "[S]":
                    if self.AIACcol < 11 and self.AIACcol > 0:
                        y[self.AIACcol] = "[A]"
                        self.AIAC.append([self.AIACrow, self.AIACcol])
                        return True
        elif ship == 5:
            for y in self.boardAI:
                if y[0] == self.AIPTrow and y[self.AIPTcol] != "[B]" and y[self.AIPTcol] != "[C]" and y[self.AIPTcol] != "[S]" and y[self.AIPTcol] != "[A]":
                    if self.AIACcol < 11 and self.AIPTcol > 0:
                        y[self.AIPTcol] = "[P]"
                        self.AIPT.append([self.AIPTrow, self.AIPTcol])
                        return True
        else:
            return False

    def checkDirAI(self, ship):
        if ship == 1:
            if self.AIBS[0][0] != "H" and self.AIBS[0][0] != "I" and self.AIBS[0][0] != "J":
                self.optionsAI.append(0)
            if self.AIBS[0][0] != "A" and self.AIBS[0][0] != "B" and self.AIBS[0][0] != "C":
                self.optionsAI.append(1)
            if self.AIBS[0][1] != 10 and self.AIBS[0][1] != 9 and self.AIBS[0][1] != 8:
                self.optionsAI.append(2)
            if self.AIBS[0][1] != 1 and self.AIBS[0][1] != 2 and self.AIBS[0][1] != 3:
                self.optionsAI.append(3)
            #if len(self.optionsAI) > 0:
                #return True
        elif ship == 2:
            checkrow = None
            checkcol = None
            if self.AIC[0][0] != "I" and self.AIC[0][0] != "J":
                collision = 0
                for a in range(2):
                    checkrow = self.LETTERS[self.LETTERS.index(self.AICrow) + 1 + a]
                    for l in self.AIBS:
                        if l[0] == checkrow and l[1] == self.AICcol:
                            collision+=1
                if collision == 0:
                    self.optionsAI.append(0)
            if self.AIC[0][0] != "A" and self.AIC[0][0] != "B":
                collision = 0
                for b in range(2):
                    checkrow = self.LETTERS[self.LETTERS.index(self.AICrow) - 1 - b]
                    for m in self.AIBS:
                        if m[0] == checkrow and m[1] == self.AICcol:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(1)
            if self.AIC[0][1] != 10 and self.AIC[0][1] != 9:
                collision = 0
                for c in range(2):
                    checkcol = self.AICcol + 1 + c
                    for n in self.AIBS:
                        if n[1] == checkcol and n[0] == self.AICrow:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(2)
            if self.AIC[0][1] != 1 and self.AIC[0][1] != 2:
                collision = 0
                for d in range(2):
                    checkcol = self.AICcol - 1 - d
                    for o in self.AIBS:
                        if o[1] == checkcol and o[0] == self.AICrow:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(3)
            #if len(self.optionsAI) > 0:
                #return True
        elif ship == 3:
            checkrow = None
            checkcol = None
            if self.AIS[0][0] != "I" and self.AIS[0][0] != "J":
                collision = 0
                for a in range(2):
                    checkrow = self.LETTERS[self.LETTERS.index(self.AISrow) + 1 + a]
                    for l in self.AIBS:
                        if l[0] == checkrow and l[1] == self.AIScol:
                            collision += 1
                    for w in self.AIC:
                        if w[0] == checkrow and w[1] == self.AIScol:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(0)
            if self.AIS[0][0] != "A" and self.AIS[0][0] != "B":
                collision = 0
                for b in range(2):
                    checkrow = self.LETTERS[self.LETTERS.index(self.AISrow) - 1 - b]
                    for m in self.AIBS:
                        if m[0] == checkrow and m[1] == self.AIScol:
                            collision += 1
                    for x in self.AIC:
                        if x[0] == checkrow and x[1] == self.AIScol:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(1)
            if self.AIS[0][1] != 10 and self.AIS[0][1] != 9:
                collision = 0
                for c in range(2):
                    checkcol = self.AIScol + 1 + c
                    for n in self.AIBS:
                        if n[1] == checkcol and n[0] == self.AISrow:
                            collision += 1
                    for y in self.AIC:
                        if y[1] == checkcol and y[0] == self.AISrow:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(2)
            if self.AIS[0][1] != 1 and self.AIS[0][1] != 2:
                collision = 0
                for d in range(2):
                    checkcol = self.AIScol - 1 - d
                    for o in self.AIBS:
                        if o[1] == checkcol and o[0] == self.AISrow:
                            collision += 1
                    for z in self.AIC:
                        if z[1] == checkcol and z[0] == self.AISrow:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(3)
            #if len(self.optionsAI) > 0:
                #return True
        elif ship == 4:
            checkrow = None
            checkcol = None
            if self.AIAC[0][0] != "H" and self.AIAC[0][0] != "I" and self.AIAC[0][0] != "J" and self.AIAC[0][0] != "G":
                collision = 0
                for a in range(4):
                    checkrow = self.LETTERS[self.LETTERS.index(self.AIACrow) + 1 + a]
                    for l in self.AIBS:
                        if l[0] == checkrow and l[1] == self.AIACcol:
                            collision += 1
                    for w in self.AIC:
                        if w[0] == checkrow and w[1] == self.AIACcol:
                            collision += 1
                    for h in self.AIS:
                        if h[0] == checkrow and h[1] == self.AIACcol:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(0)
            if self.AIAC[0][0] != "A" and self.AIAC[0][0] != "B" and self.AIAC[0][0] != "C" and self.AIAC[0][0] != "D":
                collision = 0
                for b in range(4):
                    checkrow = self.LETTERS[self.LETTERS.index(self.AIACrow) - 1 - b]
                    for m in self.AIBS:
                        if m[0] == checkrow and m[1] == self.AIACcol:
                            collision += 1
                    for x in self.AIC:
                        if x[0] == checkrow and x[1] == self.AIACcol:
                            collision += 1
                    for i in self.AIS:
                        if i[0] == checkrow and i[1] == self.AIACcol:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(1)
            if self.AIAC[0][1] != 10 and self.AIAC[0][1] != 9 and self.AIAC[0][1] != 8 and self.AIAC[0][1] != 7:
                collision = 0
                for c in range(4):
                    checkcol = self.AIACcol + 1 + c
                    for n in self.AIBS:
                        if n[1] == checkcol and n[0] == self.AIACrow:
                            collision += 1
                    for y in self.AIC:
                        if y[1] == checkcol and y[0] == self.AIACrow:
                            collision += 1
                    for j in self.AIS:
                        if j[1] == checkcol and j[0] == self.AIACrow:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(2)
            if self.AIAC[0][1] != 1 and self.AIAC[0][1] != 2 and self.AIAC[0][1] != 3 and self.AIAC[0][1] != 4:
                collision = 0
                for d in range(4):
                    checkcol = self.AIACcol - 1 - d
                    for o in self.AIBS:
                        if o[1] == checkcol and o[0] == self.AIACrow:
                            collision += 1
                    for z in self.AIC:
                        if z[1] == checkcol and z[0] == self.AIACrow:
                            collision += 1
                    for k in self.AIS:
                        if k[1] == checkcol and k[0] == self.AIACrow:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(3)
            #if len(self.optionsAI) > 0:
                #return True
        elif ship == 5:
            checkrow = None
            checkcol = None
            if self.AIPT[0][0] != "J":
                collision = 0
                for a in range(1):
                    checkrow = self.LETTERS[self.LETTERS.index(self.AIPTrow) + 1 + a]
                    for l in self.AIBS:
                        if l[0] == checkrow and l[1] == self.AIPTcol:
                            collision += 1
                    for w in self.AIC:
                        if w[0] == checkrow and w[1] == self.AIPTcol:
                            collision += 1
                    for h in self.AIS:
                        if h[0] == checkrow and h[1] == self.AIPTcol:
                            collision += 1
                    for e in self.AIAC:
                        if e[0] == checkrow and e[1] == self.AIPTcol:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(0)
            if self.AIPT[0][0] != "A":
                collision = 0
                for b in range(1):
                    checkrow = self.LETTERS[self.LETTERS.index(self.AIPTrow) - 1 - b]
                    for m in self.AIBS:
                        if m[0] == checkrow and m[1] == self.AIPTcol:
                            collision += 1
                    for x in self.AIC:
                        if x[0] == checkrow and x[1] == self.AIPTcol:
                            collision += 1
                    for i in self.AIS:
                        if i[0] == checkrow and i[1] == self.AIPTcol:
                            collision += 1
                    for f in self.AIAC:
                        if f[0] == checkrow and f[1] == self.AIPTcol:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(1)
            if self.AIPT[0][1] != 10:
                collision = 0
                for c in range(1):
                    checkcol = self.AIPTcol + 1 + c
                    for n in self.AIBS:
                        if n[1] == checkcol and n[0] == self.AIPTrow:
                            collision += 1
                    for y in self.AIC:
                        if y[1] == checkcol and y[0] == self.AIPTrow:
                            collision += 1
                    for j in self.AIS:
                        if j[1] == checkcol and j[0] == self.AIPTrow:
                            collision += 1
                    for g in self.AIAC:
                        if g[1] == checkcol and g[0] == self.AIPTrow:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(2)
            if self.AIPT[0][1] != 1:
                collision = 0
                for d in range(1):
                    checkcol = self.AIPTcol - 1 - d
                    for o in self.AIBS:
                        if o[1] == checkcol and o[0] == self.AIPTrow:
                            collision += 1
                    for z in self.AIC:
                        if z[1] == checkcol and z[0] == self.AIPTrow:
                            collision += 1
                    for k in self.AIS:
                        if k[1] == checkcol and k[0] == self.AIPTrow:
                            collision += 1
                    for u in self.AIAC:
                        if u[1] == checkcol and u[0] == self.AIPTrow:
                            collision += 1
                if collision == 0:
                    self.optionsAI.append(3)
            #if len(self.optionsAI) > 0:
                #return True
        if len(self.optionsAI) > 0:
            return True
        else:
            return False

    def __str__(self):
        s = "Your Board:"
        for y in self.boardPlayer:
            s = s + "\n"
            for x in y:
                s = s + "\t" + str(x)
        s = s + '\n' + "Your Shots:"
        for y in self.boardAI:
            s = s + "\n"
            for x in y:
                s = s + "\t" + str(x)
        return s



board = BattleShipBoard()
