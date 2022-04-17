from pygame_functions import *

screenSize(1920, 1080)

mouseX = int(mouseX())
mouseY = int(mouseY())

s = makeSprite("textures/soap.png")

showSprite(s)

sx = 400
sy = 300

moveSprite(s, sx, sy)

x = 1

while True:

    if keyPressed("up"):
        x += 0.1
        transformSprite(s, 0, x)
        tick(120)
    if keyPressed("down"):
        x -= 0.1
        transformSprite(s, 0, x)
        tick(120)
    if x == 0.20000000000000015:
        x = 1
    if keyPressed("w"):
        sy -= 5
        moveSprite(s, sx, sy)
        tick(120)
    if keyPressed("s"):
        sy += 5
        moveSprite(s, sx, sy)
        tick(120)
    if keyPressed("a"):
        sx -= 5
        moveSprite(s, sx, sy)
        tick(120)
    if keyPressed("d"):
        sx += 5
        moveSprite(s, sx, sy)
        tick(120)
    if sx > 1920:
        sx = 1919
        moveSprite(s, sx, sy)
    if sx < 1:
        sx = 1
        moveSprite(s, sx, sy)
    if sy > 1080:
        sy = 1079
        moveSprite(s, sx, sy)
    if sy < 1:
        sy = 2
        moveSprite(s, sx, sy)

    tick(120)

endWait()
