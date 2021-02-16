import pygame
from pygame_functions import *
import random
import time

#this is a board game which is a square and the objective is to roll a dice and get as many bars off soap as you can.
#the enemy are bateria which are ment to be called "corona virus"
#the way to win is to kill all corona viruses and get all the bars of soap.

y = {

    "y1":{
        1: 110,
        2: 300,
        3: 480,
        4: 670,
        5: 855
    },
    "y2":{
        1:855,
        2:670,
        3:480,
        4:300,
        5:110
    },
    "y3":{
        1: 110,
        2: 300,
        3: 480,
        4: 670,
        5: 855
    },
    "y4":{
        1:855,
        2:670,
        3:480,
        4:300,
        5:110
    },
}
s = {
    1:88,
    2:543,
    3:983,
    4:1423,
}

z = {
    "midX":{
        1:313,
        2:768,
        3:1208
    },
    "midY": {
        1:855,
        2:110,
        3:855
    },
    "win":{
        "x":1653,
        "y":110
    }
}
print(z["midX"][1])
x1 = 1
# screen
dice = random.randint(1,2)
squares = 1
# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (1, 1, 0)
DARKGREEN = (50,205,50)
screenSize(1920, 1080)

makeSprite("baord.png")
soap = makeSprite("soap.png")
virus = makeSprite("virus.PNG")
player = makeSprite("pla.png")
roll = makeSprite("roll.png")

setBackgroundImage("baord.png")
showSprite(soap)
moveSprite(soap, 68, 335)
showSprite(player)
moveSprite(player, 43, 45)
showSprite(roll)
moveSprite(roll, 748, 320)

mouse = makeSprite("mouse.png")
showSprite(mouse)
mouX = mouseX()
mouY = mouseY()
click = mousePressed()
moveSprite(mouse, mouX, mouY)
plaPosX = 43
plaPosY = 45
transformSprite(player, 0, 0.5)
x = makeLabel(str(plaPosX), 16, 800, 11)
y = makeLabel(str(plaPosY), 16, 1008, 10)
x2 = makeLabel("X", 16, 780, 11)
y2 = makeLabel("Y", 16, 989, 10)
showLabel(x)
showLabel(y)
showLabel(x2)
showLabel(y2)

#now implement questions and instead of having the ability to move around just use questions as a form of either
#moving forward or losing lives
while True:
    mouX = mouseX()
    mouY = mouseY()
    moveSprite(mouse, mouX, mouY)
    if touching(mouse, roll) and mousePressed():
        rand = random.randint(1,3)
        print(rand)
    #roll = False
    #while roll






    tick(60)

endWait()
