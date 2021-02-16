from pygame_functions import *
import random
screenSize(1920, 1080)
def intro():
    logo = makeLabel("Save The World", 155, 565, 62, WHITE)
    playPress = makeLabel("START", 60, 911, 518, WHITE)
    creds = makeLabel("An Informative game developed for educating kids about personal hygine", 25, 680, 821,WHITE)
    dev = makeLabel("made by Rohaan Ahmed", 40, 809, 938, WHITE)
    showLabel(dev)
    showLabel(creds)
    showLabel(playPress)
    showLabel(logo)
    endWait()
