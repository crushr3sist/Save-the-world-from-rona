import pygame
from pygame_functions import *
import random
from array import *

# this is a board game which is a square and the objective is to roll a dice and get as many bars off soap as you can.
# the enemy are bateria which are ment to be called "corona virus"
# the way to win is to kill all corona viruses and get all the bars of soap.
screenSize(1920, 1080)
makeSprite("baord.png")
soap0 = makeSprite("soap.png")
soap1 = makeSprite("soap.png")
soap2 = makeSprite("soap.png")
soap3 = makeSprite("soap.png")
soap4 = makeSprite("soap.png")
soap5 = makeSprite("soap.png")

virus0 = makeSprite("virus.PNG")
virus1 = makeSprite("virus.PNG")
virus2 = makeSprite("virus.PNG")
virus3 = makeSprite("virus.PNG")
virus4 = makeSprite("virus.PNG")
virus5 = makeSprite("virus.PNG")
virus6 = makeSprite("virus.PNG")

player = makeSprite("pla.png")

roll = makeSprite("roll.png")

setBackgroundImage("baord.png")

showSprite(soap0)
moveSprite(soap0, 68, 335)

showSprite(player)
moveSprite(player, 43, 45)

transformSprite(player, 0, 0.5)


#coordinates = {
#    1:(88, 110),
#    2:(88, 300),
#    3:(88, 480),
#    4:(88, 670),
#    5:(88, 855),
#    6:(313,855),
#    7:(543,855),
#    8:(543,670),
#    9:(543,480),
#    10:(543,300),
#    11:(543,110),
#    12:(758,110),
#    13:(983,110),
#    14:(983,300),
#    15:(983,480),
#    16:(983,670),
#    17:(983,855),
#    18:(1208,855),
#    19:(1423,855),
#    20:(1423,670),
#    21:(1423,480),
#    22:(1423,300),
#    23:(1423,110)
#}

xArray = [88,88,88,88,88,313,543,543,543,543,543,758,983,983,983,983,983,1208,1423,1423,1423,1423,1423]
yArray = [110,300,480,670,855,855,855,670,480,300,110,110,110,300,480,670,855,855,855,670,480,300,110]




count = 0

while True:

    if keyPressed("space"):
        print(str(count))
        moveSprite(player, xArray[count], yArray[count])
        count = count + 1
        pause(100)
    if count == 23:
        count = count = 0
    tick(20)


