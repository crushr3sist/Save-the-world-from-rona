import pygame
from pygame_functions import *
import random
from array import *
xArray = [88,88,88,88,88,313,543,543,543,543,543,758,983,983,983,983,983,1208,1423,1423,1423,1423,1423]
yArray = [110,300,480,670,855,855,855,670,480,300,110,110,110,300,480,670,855,855,855,670,480,300,110]
# this is a board game which is a square and the objective is to roll a dice and get as many bars off soap as you can.
# the enemy are bateria which are ment to be called "corona virus"
# the way to win is to kill all corona viruses and get all the bars of soap.
screenSize(1920, 1080)
BLACK = (0,0,0)
WHITE = (255,255,255)
makeSprite("baord.png")
soap0 = makeSprite("soap.png")
soap1 = makeSprite("soap.png")
soap2 = makeSprite("soap.png")
soap3 = makeSprite("soap.png")
soap4 = makeSprite("soap.png")
soap5 = makeSprite("soap.png")
soap6 = makeSprite("soap.png")
soap7 = makeSprite("soap.png")
soap8 = makeSprite("soap.png")
soap8 = makeSprite("soap.png")
virus0 = makeSprite("virus.PNG")
virus1 = makeSprite("virus.PNG")
virus2 = makeSprite("virus.PNG")
virus3 = makeSprite("virus.PNG")
virus4 = makeSprite("virus.PNG")
virus5 = makeSprite("virus.PNG")
virus6 = makeSprite("virus.PNG")
virus7 = makeSprite("virus.PNG")
virus8 = makeSprite("virus.PNG")
virus9 = makeSprite("virus.PNG")
virus10 = makeSprite("virus.PNG")
virus11 = makeSprite("virus.PNG")
virus12 = makeSprite("virus.PNG")
virus13 = makeSprite("virus.PNG")
virus14 = makeSprite("virus.PNG")
player = makeSprite("pla.png")
roll = makeSprite("roll.png")
xArraySoap=[70, 70, 70, 70, 300,520,520,520,520,520,750,970,970,970,970,970,1190,1410,1410,1410,1410,1410]
yArraySoap=[330,510,700,880,880,880,700,510,330,140,140,140,330,510,700,880,880,880,700,510,300,140]
xArrayVirus = [70,70,70,300,520,520,520,520,520,750,970,970,970,970,970,1190,1410,1410,1410,1410,1410]
yArrayVirus = [480,660,850,850,850,670,480,300,110,110,110,290,480,660,850,850,850,670,480,290,110]
winningX = 1630
winningY = 140
special = False
# virus 2x3
# virus 2x4
# virus rule first_set: 3 viruses
#           second_set: 4 viruses
#            third_set: 4 viruses
#            forth_set: 3 viruses
#
#soap rule first_set: 2
#         second_set: 2
#          third_set: 2
#         fourth_set: 2
# soap  4x2
def start():
    # showSprite(soap1) status bar
    showSprite(soap0)
    showSprite(soap2)
    showSprite(soap3)
    showSprite(soap4)
    showSprite(soap5)
    showSprite(soap6)
    showSprite(soap7)
    showSprite(soap8)
    showSprite(virus0)
    showSprite(virus1)
    showSprite(virus2)
    showSprite(virus3)
    showSprite(virus4)
    showSprite(virus5)
    showSprite(virus6)
    showSprite(virus7)
    showSprite(virus8)
    showSprite(virus9)
    showSprite(virus10)
    showSprite(virus11)
    showSprite(virus12)
    # this doesnt work since sprites start appearing underneath each other since there are only 4 squares that are
    # toggled as showing on the surface.
    # soap sectors:
    # random.randint(2, 5)
    # random.randint(6, 11)
    # random.randint(12, 17)
    # random.randint(18, 20)
    placementsoap0 = 1
    placementsoap1 = random.randint(2, 5)
    placementsoap2 = random.randint(2, 5)
    placementsoap3 = random.randint(6, 11)
    placementsoap4 = random.randint(6, 11)
    placementsoap5 = random.randint(12, 17)
    placementsoap6 = random.randint(12, 17)
    placementsoap7 = random.randint(18, 20)
    placementsoap8 = random.randint(18, 20)
    # soap sectors:
    # random.randint(1, 5)
    # random.randint(6, 11)
    # random.randint(11, 17)
    # random.randint(18, 20)
    placementvirus1 = random.randint(1, 5)
    placementvirus2 = random.randint(1, 5)
    placementvirus3 = random.randint(1, 5)
    placementvirus4 = random.randint(6, 11)
    placementvirus5 = random.randint(6, 11)
    placementvirus6 = random.randint(6, 11)
    placementvirus7 = random.randint(6, 11)
    placementvirus8 = random.randint(11, 17)
    placementvirus9 = random.randint(11, 17)
    placementvirus10 = random.randint(11, 17)
    placementvirus11 = random.randint(11, 17)
    placementvirus12 = random.randint(18, 20)
    placementvirus13 = random.randint(18, 20)
    placementvirus14 = random.randint(18, 20)
    moveSprite(soap1, xArraySoap[placementsoap1], yArraySoap[placementsoap1])
    moveSprite(soap2, xArraySoap[placementsoap2], yArraySoap[placementsoap2])
    moveSprite(soap3, xArraySoap[placementsoap3], yArraySoap[placementsoap3])
    moveSprite(soap4, xArraySoap[placementsoap4], yArraySoap[placementsoap4])
    moveSprite(soap5, xArraySoap[placementsoap5], yArraySoap[placementsoap5])
    moveSprite(soap6, xArraySoap[placementsoap6], yArraySoap[placementsoap6])
    moveSprite(soap7, xArraySoap[placementsoap7], yArraySoap[placementsoap7])
    moveSprite(soap8, xArraySoap[placementsoap8], yArraySoap[placementsoap8])
    moveSprite(virus0, xArrayVirus[placementvirus1], yArrayVirus[placementvirus1])
    moveSprite(virus1, xArrayVirus[placementvirus2], yArrayVirus[placementvirus2])
    moveSprite(virus2, xArrayVirus[placementvirus3], yArrayVirus[placementvirus3])
    moveSprite(virus3, xArrayVirus[placementvirus4], yArrayVirus[placementvirus4])
    moveSprite(virus4, xArrayVirus[placementvirus5], yArrayVirus[placementvirus5])
    moveSprite(virus5, xArrayVirus[placementvirus6], yArrayVirus[placementvirus6])
    moveSprite(virus6, xArrayVirus[placementvirus7], yArrayVirus[placementvirus7])
    moveSprite(virus7, xArrayVirus[placementvirus8], yArrayVirus[placementvirus8])
    moveSprite(virus8, xArrayVirus[placementvirus9], yArrayVirus[placementvirus9])
    moveSprite(virus9, xArrayVirus[placementvirus10], yArrayVirus[placementvirus10])
    moveSprite(virus10, xArrayVirus[placementvirus11], yArrayVirus[placementvirus11])
    moveSprite(virus11, xArrayVirus[placementvirus12], yArrayVirus[placementvirus12])
    moveSprite(virus12, xArrayVirus[placementvirus13], yArrayVirus[placementvirus13])
    moveSprite(virus13, xArrayVirus[placementvirus14], yArrayVirus[placementvirus14])
#showSprite(soap1) status bar
showSprite(soap0)
showSprite(soap2)
showSprite(soap3)
showSprite(soap4)
showSprite(soap5)
showSprite(soap6)
showSprite(soap7)
showSprite(soap8)
showSprite(virus0)
showSprite(virus1)
showSprite(virus2)
showSprite(virus3)
showSprite(virus4)
showSprite(virus5)
showSprite(virus6)
showSprite(virus7)
showSprite(virus8)
showSprite(virus9)
showSprite(virus10)
showSprite(virus11)
showSprite(virus12)
# this doesnt work since sprites start appearing underneath each other since there are only 4 squares that are
# toggled as showing on the surface.
# soap sectors:
# random.randint(2, 5)
# random.randint(6, 11)
# random.randint(12, 17)
# random.randint(18, 20)
placementsoap0 = 1
placementsoap1 = random.randint(2, 5)
placementsoap2 = random.randint(2, 5)
placementsoap3 = random.randint(6, 11)
placementsoap4 = random.randint(6, 11)
placementsoap5 = random.randint(12, 17)
placementsoap6 = random.randint(12, 17)
placementsoap7 = random.randint(18, 20)
placementsoap8 = random.randint(18, 20)
# soap sectors:
# random.randint(1, 5)
# random.randint(6, 11)
# random.randint(11, 17)
# random.randint(18, 20)
placementvirus1 = random.randint(1, 5)
placementvirus2 = random.randint(1, 5)
placementvirus3 = random.randint(1, 5)
placementvirus4 = random.randint(6, 11)
placementvirus5 = random.randint(6, 11)
placementvirus6 = random.randint(6, 11)
placementvirus7 = random.randint(6, 11)
placementvirus8 = random.randint(11, 17)
placementvirus9 = random.randint(11, 17)
placementvirus10 = random.randint(11, 17)
placementvirus11 = random.randint(11, 17)
placementvirus12 = random.randint(18, 20)
placementvirus13 = random.randint(18, 20)
placementvirus14 = random.randint(18, 20)
moveSprite(soap1, xArraySoap[placementsoap1], yArraySoap[placementsoap1])
moveSprite(soap2, xArraySoap[placementsoap2], yArraySoap[placementsoap2])
moveSprite(soap3, xArraySoap[placementsoap3], yArraySoap[placementsoap3])
moveSprite(soap4, xArraySoap[placementsoap4], yArraySoap[placementsoap4])
moveSprite(soap5, xArraySoap[placementsoap5], yArraySoap[placementsoap5])
moveSprite(soap6, xArraySoap[placementsoap6], yArraySoap[placementsoap6])
moveSprite(soap7, xArraySoap[placementsoap7], yArraySoap[placementsoap7])
moveSprite(soap8, xArraySoap[placementsoap8], yArraySoap[placementsoap8])
moveSprite(virus0, xArrayVirus[placementvirus1], yArrayVirus[placementvirus1])
moveSprite(virus1, xArrayVirus[placementvirus2], yArrayVirus[placementvirus2])
moveSprite(virus2, xArrayVirus[placementvirus3], yArrayVirus[placementvirus3])
moveSprite(virus3, xArrayVirus[placementvirus4], yArrayVirus[placementvirus4])
moveSprite(virus4, xArrayVirus[placementvirus5], yArrayVirus[placementvirus5])
moveSprite(virus5, xArrayVirus[placementvirus6], yArrayVirus[placementvirus6])
moveSprite(virus6, xArrayVirus[placementvirus7], yArrayVirus[placementvirus7])
moveSprite(virus7, xArrayVirus[placementvirus8], yArrayVirus[placementvirus8])
moveSprite(virus8, xArrayVirus[placementvirus9], yArrayVirus[placementvirus9])
moveSprite(virus9, xArrayVirus[placementvirus10], yArrayVirus[placementvirus10])
moveSprite(virus10, xArrayVirus[placementvirus11], yArrayVirus[placementvirus11])
moveSprite(virus11, xArrayVirus[placementvirus12], yArrayVirus[placementvirus12])
moveSprite(virus12, xArrayVirus[placementvirus13], yArrayVirus[placementvirus13])
moveSprite(virus13, xArrayVirus[placementvirus14], yArrayVirus[placementvirus14])

if placementsoap1 == placementvirus1:
    if touching(placementsoap1,placementvirus1):
        placementsoap1 += 1
        if touching(placementvirus1,placementsoap1):
            placementvirus1 += 1
    if placementsoap2 == placementvirus2:
        if touching(placementsoap2,placementvirus3):
            placementsoap2 += 1
            if touching(placementvirus2,placementsoap2):
                placementvirus2 += 1
            
        if placementsoap3 == placementvirus3:
            if touching(placementsoap3, placementvirus3):
                placementsoap3+=1
                if touching(placementvirus3, )
            if placementsoap4 == placementvirus4:
                if placementsoap5 == placementvirus5:
                    if placementsoap6 == placementvirus6:
                        if placementsoap7 == placementvirus7:
                            if placementsoap8 == placementvirus8:
                                if placementsoap9 == placementvirus9:
                                    print("its a double 9")
                                print("its a double 8")
                            print("its a double 7")
                        print("its a double 6")
                    print("its a double 5")
                print("its a double 4")
            print("its a double 3")
        print("its a double 2")
    print("its a double 1")
print("its a double 0")
                                                
    




'''
if touching(soap1 or soap2, virus0 or virus1 or virus2):
    
    placementsoap1 += 1
    if placementsoap1 > 21:
        placementsoap1 = placementsoap1 - 3
if touching(soap3 or soap4, virus3 or virus4 or virus5 or virus6):
    placementsoap2 += 1
    if placementsoap2 > 21:
        placementsoap2 = placementsoap2 -3
if touching(soap5 or soap6, virus7 or virus8 or virus9 or virus10):
    placementsoap3 += 1
    if placementsoap3 > 21:
        placementsoap3 = placementsoap3 - 3
if touching(soap7 or soap8, virus11 or virus12 or virus13):
    placementsoap4 += 1
    if placementsoap4 > 21:
        placementsoap4 = placementsoap4 - 3


for k in range(1,22):
    if k == placementsoap1:
        placementsoap1 = int(placementsoap1)
        if k == placementsoap2:
            placementsoap2 = int(placementsoap2)
            
            if k == placementsoap3:
                placementsoap3 = int(placementsoap3)
                
                if k == placementsoap4:
                    placementsoap4 = int(placementsoap4)
                
'''
setBackgroundColour(BLACK)
moveSprite(soap0, 68, 335)
moveSprite(player, 43, 45)
transformSprite(player, 0, 0.5)
transformSprite(soap1,0,0.5)
xTemp = 1000
yTemp = 500

logo = makeLabel("Save The World", 155, 565, 62, WHITE)
playPress = makeLabel("START", 60, 911, 518, WHITE)
creds = makeLabel("An Informative game developed for educating kids about personal hygine", 25, 680, 821,WHITE)
dev = makeLabel("made by Rohaan Ahmed", 40, 809, 938, WHITE)
showLabel(dev)
showLabel(creds)
showLabel(playPress)
showLabel(logo)

count = 0
lives = 3
soap = 0

def hide1():
    hideLabel(playPress)
    hideLabel(logo)
    hideLabel(creds)
    hideLabel(dev)
    setBackgroundImage("baord.png")
    showSprite(player)
    
while True:
    hide1()
    #if spriteClicked(playPress):

    if keyPressed("right"):
        xTemp += 10
        moveLabel(virus0, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    if keyPressed("left"):
        xTemp -= 10
        moveLabel(virus0, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    if keyPressed("up"):
        yTemp -= 10
        moveLabel(virus0, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    if keyPressed("down"):
        yTemp += 10
        moveLabel(virus0, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    tick(120)


    if keyPressed("space"):
        print(str(count))
        moveSprite(player, xArray[count], yArray[count])
        count = count + 1
        pause(100)
    if count == 23:
        start()
        count = count = 0

endWait()
