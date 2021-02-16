#all important imports
import pygame
from pygame_functions import *
import makingsprites
import random
from array import *

player = makeSprite("pla.png")

roll = makeSprite("roll.png")

winningX = 1630
winningY = 140

special = False
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
count = 0

lives = 3

soap = 0
BLACK = (0,0,0)
WHITE = (255,255,255)


#sprites(1920, 1080)

def intro():
    logo = makeLabel("Save The World", 155, 565, 62, WHITE)
    playPress = makeLabel("START", 60, 911, 518, WHITE)
    creds = makeLabel("An Informative game developed for educating kids about personal hygine", 25, 680, 821,WHITE)
    dev = makeLabel("made by Rohaan Ahmed", 40, 809, 938, WHITE)
    showLabel(dev)
    showLabel(creds)
    showLabel(playPress)
    showLabel(logo)

def hide1():
    hideLabel(playPress)
    hideLabel(logo)
    hideLabel(creds)
    hideLabel(dev)
    setBackgroundImage("baord.png")
    showSprite(player)
    
while True:
    intro()
    #hide1()
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
