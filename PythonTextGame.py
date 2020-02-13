""" Lost all my python projects when transfering hard drives a while back so
i just wrote up this game quickly for the python portfolio"""

#Game is unfinished

import random
class player:
    hp = 50 #minimum hp
    dmg = 10
    def __init__(self):  #skillpoint assignment for the player
        points = 20
        self.name = input("Please enter your name: ")
        strength = int(input("How many points would you like to put into strength? ("+str(points)+"/20): "))
        points -= strength
        if strength == 0:
            strength = 1#no need for self.strength because this is the only time we use it
        self.hp += strength*10
        self.dmg += strength
        self.speed = int(input("How many points would you like to put into speed? ("+str(points)+"/20): "))
        points -= self.speed
        if self.speed == 0:#speed is used outside of here so has to be self
            self.speed = 1
        self.armour = int(input("How many points would you like to put into armour? ("+str(points)+"/20): "))
        points -= self.armour
        if self.armour == 0:
            self.armour = 1#armour is also used outside
    def attack(self,curenemy):
        realdmg = int(self.dmg/((curenemy.armour*0.1)+0.9))
        curenemy.hp-= realdmg
        print (curenemy.name,"has taken",realdmg,"damage, his HP is now",curenemy.hp)
        if curenemy.hp <= 0:
            print(curenemy.name,"is dead!")
            return False

class enemy:#enemy base class / gremlin enemy
    name = "Gremlin"
    hp = 50
    dmg = 10
    speed = 10
    armour = random.randint(0,10)
    def attack(self,ply):
        realdmg = int(self.dmg/((ply.armour*0.1)+0.9))
        ply.hp-= realdmg
        print (ply.name,"has taken",realdmg,"damage, your HP is now",ply.hp)
        if ply.hp <= 0:
            print("You are dead!")
            return False
class witch(enemy):
    name = "Witch"
    hp = 100
    dmg = 25
    speed = 0
def premovement():
    areas = ["grassland","mountains","cave","path"] #allows for easy expansion
    nav = [["turn left"],["go forward"],["turn right"]]
    for i in range(3):
        temp = random.choice(areas)#overcomplicated way of doing a random area to turn into but may come in useful further down
        nav[i].append(temp)
    return nav
def actualmovement(ply):
    while True:
        nav = premovement()
        print("Which direction would you like to take?")
        for i in range(3): #saves me having to write it out 3 times
            print(str(i+1)+")",nav[i][0],"into the",nav[i][1])
        choice = int(input(">>> "))
        i = choice-1
        if choice > 3:
            print("Invalid option")
        else:
            print("You have decided to",nav[i][0],"into the",nav[i][1])
            x = random.randint(0,100)
            if x > 60:
                y = randomencounter(ply)
                if y == False:
                    reversed
def randomencounter(ply):
    enemies = [enemy(),witch()]
    aenemy = random.choice(enemies)
    print("You have encountered a",aenemy.name,"with",aenemy.hp,"hp!")
    if aenemy.speed > ply.speed:
        print(aenemy.name,"is faster than you!")
        aenemy.attack(ply)
    while True:
        choice = input("What would you like to do?\n1) Attack\n2) Defend\n3) Run!").lower()
        if choice == "1" or choice == "attack":
            x = ply.attack(aenemy)
            if x == False:
                return
        elif choice == "2" or choice == "defend":
            pass
        elif choice == "3" or choice == "run":
            if ply.speed > aenemy.speed:
                print("You have escaped!")
                return
            else:
                print("You are unable to escape")
        else:
            print("Invalid option")
        x = aenemy.attack(ply)
        if x == False:
                menu() #use of iteration which is bad on the memory but no way to do it properly in this short amount of time i had
def menu():   
    print("Welcome to the game menu")
    while True:
        choice = str(input("please select and option\n1) New Game\n2) Load Game\n3) Debug\n4) Exit\n>>> ")).lower()
        if choice == "1" or choice == "new game":
            ply = player()
            actualmovement(ply)
        elif choice == "2" or choice == "load game":
            print ("Option not available")
        elif choice == "3" or choice == "debug":
            break
        elif choice == "4" or choice == "exit":
            exit()
        else:
            print("Invalid Input")
menu()
