from pygame_functions import *
import random
from arrays import *
from functions import *

# add in instruction slides available everywhere
# add in the score system
# add in the life system

screenSize(1920, 1080)
BLACK = (0, 0, 0)
WHITE = (180, 180, 180)

soap0 = makeSprite("textures/soap.png")
soap1 = makeSprite("textures/soap.png")
soap2 = makeSprite("textures/soap.png")
soap3 = makeSprite("textures/soap.png")
soap4 = makeSprite("textures/soap.png")
soap5 = makeSprite("textures/soap.png")
soap6 = makeSprite("textures/soap.png")
soap7 = makeSprite("textures/soap.png")
soap8 = makeSprite("textures/soap.png")
soap9 = makeSprite("textures/soap.png")

virus0 = makeSprite("textures/virus.PNG")
virus1 = makeSprite("textures/virus.PNG")
virus2 = makeSprite("textures/virus.PNG")
virus3 = makeSprite("textures/virus.PNG")
virus4 = makeSprite("textures/virus.PNG")
virus5 = makeSprite("textures/virus.PNG")
virus6 = makeSprite("textures/virus.PNG")
virus7 = makeSprite("textures/virus.PNG")
virus8 = makeSprite("textures/virus.PNG")
virus9 = makeSprite("textures/virus.PNG")
virus10 = makeSprite("textures/virus.PNG")
virus11 = makeSprite("textures/virus.PNG")
virus12 = makeSprite("textures/virus.PNG")
virus13 = makeSprite("textures/virus.PNG")
virus14 = makeSprite("textures/virus.PNG")

antidote = makeSprite("textures/antidote.png")

logo = makeLabel("Save The World", 155, 565, 62, WHITE)
playPress = makeLabel("START", 60, 911, 518, WHITE)
creds = makeLabel(
    "An Informative game developed for educating kids about personal hygine",
    25,
    680,
    821,
    WHITE,
)
dev = makeLabel("made by Rohaan Ahmed", 40, 809, 938, WHITE)

buttons = makeSprite("textures/buttons_nodisp.png")
player = makeSprite("textures/pla.png")
roll = makeSprite("textures/roll.png")

showLabel(dev)
showLabel(creds)
showLabel(playPress)
showLabel(logo)
moveSprite(player, 43, 45)
transformSprite(player, 0, 0.5)


questionLabel = makeLabel(
    questions[quizDispInd],
    55,
    questionsX[quizDispInd],
    questionsY[quizDispInd],
    WHITE,
    "Calibri",
    "clear",
)
multiAns1Label = makeLabel(
    multiAns1[quizDispInd],
    29,
    ans1X[quizDispInd],
    ans1Y[quizDispInd],
    WHITE,
    "Calibri",
    "clear",
)
multiAns2Label = makeLabel(
    multiAns2[quizDispInd],
    29,
    ans2X[quizDispInd],
    ans2Y[quizDispInd],
    WHITE,
    "Calibri",
    "clear",
)
multiAns3Label = makeLabel(
    multiAns3[quizDispInd],
    29,
    ans3X[quizDispInd],
    ans3Y[quizDispInd],
    WHITE,
    "Calibri",
    "clear",
)
multiAns4Label = makeLabel(
    multiAns4[quizDispInd],
    29,
    ans4X[quizDispInd],
    ans4Y[quizDispInd],
    WHITE,
    "Calibri",
    "clear",
)
Score = makeLabel(f"SCORE:{score}", 25, 5, 5, BLACK, "Calibri", "clear")
moveLabel(Score, 804, 28)


def instState():
    setBackgroundImage("textures/instBoard.PNG")
    instButtons = makeSprite("textures/instBoard.PNG")
    instQuiz = makeSprite("textures/instButtons.png")


def start():
    showSprite(Score)
    moveSprite(player, 88, 110)
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
    moveSprite(virus0, xArrayVirus[0], yArrayVirus[0])
    moveSprite(virus1, xArrayVirus[2], yArrayVirus[2])
    moveSprite(virus2, xArrayVirus[3], yArrayVirus[3])
    moveSprite(virus3, xArrayVirus[4], yArrayVirus[4])
    moveSprite(virus4, xArrayVirus[7], yArrayVirus[7])
    moveSprite(virus5, xArrayVirus[8], yArrayVirus[8])
    moveSprite(virus6, xArrayVirus[9], yArrayVirus[9])
    moveSprite(virus7, xArrayVirus[10], yArrayVirus[10])
    moveSprite(virus8, xArrayVirus[12], yArrayVirus[12])
    moveSprite(virus9, xArrayVirus[13], yArrayVirus[13])
    moveSprite(virus10, xArrayVirus[14], yArrayVirus[14])
    moveSprite(virus11, xArrayVirus[17], yArrayVirus[17])
    moveSprite(virus12, xArrayVirus[19], yArrayVirus[19])
    moveSprite(soap0, xArraySoap[0], yArraySoap[0])
    moveSprite(soap1, xArraySoap[2], yArraySoap[2])
    moveSprite(soap2, xArraySoap[5], yArraySoap[5])
    moveSprite(soap3, xArraySoap[7], yArraySoap[7])
    moveSprite(soap4, xArraySoap[6], yArraySoap[6])
    moveSprite(soap5, xArraySoap[12], yArraySoap[12])
    moveSprite(soap6, xArraySoap[16], yArraySoap[16])
    moveSprite(soap7, xArraySoap[17], yArraySoap[17])
    moveSprite(soap8, xArraySoap[19], yArraySoap[19])
    moveSprite(soap9, xArraySoap[21], yArraySoap[21])
    showSprite(soap0)
    showSprite(soap1)
    showSprite(soap3)
    showSprite(soap4)
    showSprite(soap5)
    showSprite(soap6)
    showSprite(soap7)
    showSprite(soap8)
    showSprite(soap9)
    transformSprite(antidote, 0, 0.5)
    showSprite(antidote)
    moveSprite(antidote, 1620, 150)


def hide1():
    hideLabel(playPress)
    hideLabel(logo)
    hideLabel(creds)
    hideLabel(dev)
    setBackgroundImage("textures/baord.png")
    showSprite(player)

    def quizFunc1():
        buttons = makeSprite("textures/buttons_nodisp.png")
        pause(500)
        moveLabel(questionLabel, questionsX[quizDispInd], questionsY[quizDispInd])
        moveLabel(multiAns1Label, ans1X[quizDispInd], ans1Y[quizDispInd])
        moveLabel(multiAns2Label, ans2X[quizDispInd], ans2Y[quizDispInd])
        moveLabel(multiAns3Label, ans3X[quizDispInd], ans3Y[quizDispInd])
        moveLabel(multiAns4Label, ans4X[quizDispInd], ans4Y[quizDispInd])
        pause(200)
        showSprite(buttons)
        showLabel(questionLabel)
        showSprite(multiAns1Label)
        showSprite(multiAns2Label)
        showSprite(multiAns3Label)
        showSprite(multiAns4Label)
        changeLabel(questionLabel, questions[quizDispInd])
        changeLabel(multiAns1Label, multiAns1[quizDispInd])
        changeLabel(multiAns2Label, multiAns2[quizDispInd])
        changeLabel(multiAns3Label, multiAns3[quizDispInd])
        changeLabel(multiAns4Label, multiAns4[quizDispInd])


def back():
    hideAll()
    showSprite(Score)
    hideLabel(questionLabel)


def back():
    hideAll()
    hideLabel(questionLabel)
    for vi in range(0, 12):
        showSprite(f"virus{vi}")
    # showSprite(virus1)
    # showSprite(virus2)
    # showSprite(virus3)
    # showSprite(virus4)
    # showSprite(virus5)
    # showSprite(virus6)
    # showSprite(virus7)
    # showSprite(virus8)
    # showSprite(virus9)
    # showSprite(virus10)
    # showSprite(virus11)
    # showSprite(virus12)
    for sp in range(0, 9):
        showSprite(f"soap{sp}")
    # showSprite(soap0)
    # showSprite(soap1)
    # showSprite(soap3)
    # showSprite(soap4)
    # showSprite(soap5)
    # showSprite(soap6)
    # showSprite(soap7)
    # showSprite(soap8)
    # showSprite(soap9)
    showSprite(antidote)

    showSprite(player)
    setBackgroundImage("textures/baord.png")

    showSprite(antidote)
    showSprite(player)
    setBackgroundImage("textures/baord.png")


def quizFunc1():
    buttons = makeSprite("textures/buttons_nodisp.png")
    pause(500)
    print(quizDispInd)
    moveLabel(questionLabel, questionsX[quizDispInd], questionsY[quizDispInd])
    moveLabel(multiAns1Label, ans1X[quizDispInd], ans1Y[quizDispInd])
    moveLabel(multiAns2Label, ans2X[quizDispInd], ans2Y[quizDispInd])
    moveLabel(multiAns3Label, ans3X[quizDispInd], ans3Y[quizDispInd])
    moveLabel(multiAns4Label, ans4X[quizDispInd], ans4Y[quizDispInd])
    pause(200)
    showSprite(buttons)
    showLabel(questionLabel)
    showSprite(multiAns1Label)
    showSprite(multiAns2Label)
    showSprite(multiAns3Label)
    showSprite(multiAns4Label)
    changeLabel(questionLabel, questions[quizDispInd])
    changeLabel(multiAns1Label, multiAns1[quizDispInd])
    changeLabel(multiAns2Label, multiAns2[quizDispInd])
    changeLabel(multiAns3Label, multiAns3[quizDispInd])
    changeLabel(multiAns4Label, multiAns4[quizDispInd])


p = False

answerTouching = False

correctAnswerCounter = 1

life = 3

incorrect = False

while life > 1:

    if spriteClicked(playPress):
        hide1()
        start()
        showSprite(antidote)

    if touching(player, virus0):
        if quizDispInd == 0:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus0)
            moveSprite(virus0, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus1):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 1:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus1)
            moveSprite(virus1, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus2):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 2:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus2)
            moveSprite(virus2, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus3):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 3:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus3)
            moveSprite(virus3, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus4):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 4:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus4)
            moveSprite(virus4, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus5):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 5:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus5)
            moveSprite(virus5, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus6):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 6:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus6)
            moveSprite(virus6, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus7):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 7:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus7)
            moveSprite(virus7, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus8):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 8:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus8)
            moveSprite(virus8, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus9):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 9:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus9)
            moveSprite(virus9, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus10):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 10:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus10)
            moveSprite(virus10, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus11):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 11:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus11)
            moveSprite(virus11, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus12):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 12:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus12)
            moveSprite(virus12, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, virus13):
        quizDispInd += 1
        correctAnswerCounter += 1
        if quizDispInd == 13:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus13)
            moveSprite(virus13, 9999, 9999)
            p = True
            answerTouching = True

    if touching(player, soap0):
        hideSprite(soap0)
        moveSprite(soap0, 9999, 9999)
        score += 10
        changeLabel(Score, "Score : " + str(score))

    if touching(player, soap1):
        hideSprite(soap1)
        moveSprite(soap1, 9999, 9999)
        score += 10
        changeLabel(Score, "Score : " + str(score))

    if touching(player, soap2):
        hideSprite(soap2)
        moveSprite(soap2, 9999, 9999)
        score += 10
        changeLabel(Score, "Score : " + str(score))

    if touching(player, soap3):
        hideSprite(soap3)
        moveSprite(soap3, 9999, 9999)
        score += 10
        changeLabel(Score, "Score : " + str(score))

    if touching(player, soap4):
        hideSprite(soap4)
        moveSprite(soap4, 9999, 9999)
        score += 10

        changeLabel(Score, "Score : " + str(score))

    if touching(player, soap5):
        moveSprite(soap5, 9999, 9999)
        hideSprite(soap5)
        score += 10
        changeLabel(Score, "Score : " + str(score))

    if touching(player, soap6):
        moveSprite(soap6, 9999, 9999)
        hideSprite(soap6)
        score += 10
        changeLabel(Score, "Score : " + str(score))

    if touching(player, soap7):
        moveSprite(soap7, 9999, 9999)
        hideSprite(soap7)
        score += 10
        changeLabel(Score, "Score : " + str(score))

    if touching(player, soap8):
        moveSprite(soap8, 9999, 9999)
        hideSprite(soap8)
        score += 10
        changeLabel(Score, "Score : " + str(score))

    if touching(player, soap9):
        moveSprite(soap9, 9999, 9999)
        hideSprite(soap9)
        score += 10
        changeLabel(Score, "Score : " + str(score))

    tick(120)

    if keyPressed("space"):

        moveSprite(player, xArray[count], yArray[count])
        count = count + 1
        pause(200)

    if count == 24:
        count = count = 0
        start()
    tick(20)

    if p:
        if answerTouching:
            if correctAnswerCounter == 1 and spriteClicked(multiAns3Label):
                score += 10
                back()
            elif correctAnswerCounter == 1 and spriteClicked(multiAns1Label):
                incorrect = True

            elif correctAnswerCounter == 1 and spriteClicked(multiAns2Label):
                incorrect = True

            elif correctAnswerCounter == 1 and spriteClicked(multiAns4Label):
                incorrect = True

            if correctAnswerCounter == 2 and spriteClicked(multiAns2Label):
                score += 10
                back()

            elif correctAnswerCounter == 2 and spriteClicked(multiAns1Label):
                incorrect = True
            elif correctAnswerCounter == 2 and spriteClicked(multiAns3Label):
                incorrect = True
            elif correctAnswerCounter == 2 and spriteClicked(multiAns4Label):
                incorrect = True

            if correctAnswerCounter == 3 and spriteClicked(multiAns1Label):
                score += 10
                back()
            elif correctAnswerCounter == 3 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 3 and spriteClicked(multiAns3Label):
                incorrect = True
            elif correctAnswerCounter == 3 and spriteClicked(multiAns4Label):
                incorrect = True

            if correctAnswerCounter == 4 and spriteClicked(multiAns4Label):
                score += 10
                back()
            elif correctAnswerCounter == 4 and spriteClicked(multiAns1Label):
                incorrect = True
            elif correctAnswerCounter == 4 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 4 and spriteClicked(multiAns3Label):
                incorrect = True

            if correctAnswerCounter == 5 and spriteClicked(multiAns4Label):
                score += 10
                back()
            elif correctAnswerCounter == 5 and spriteClicked(multiAns1Label):
                incorrect = True
            elif correctAnswerCounter == 5 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 5 and spriteClicked(multiAns3Label):
                incorrect = True

            if correctAnswerCounter == 6 and spriteClicked(multiAns4Label):
                score += 10
                back()
            elif correctAnswerCounter == 6 and spriteClicked(multiAns1Label):
                incorrect = True
            elif correctAnswerCounter == 6 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 6 and spriteClicked(multiAns3Label):
                incorrect = True

            if correctAnswerCounter == 7 and spriteClicked(multiAns1Label):
                score += 10
                back()
            elif correctAnswerCounter == 7 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 7 and spriteClicked(multiAns3Label):
                incorrect = True
            elif correctAnswerCounter == 7 and spriteClicked(multiAns4Label):
                incorrect = True

            if correctAnswerCounter == 8 and spriteClicked(multiAns4Label):
                score += 10
                back()
            elif correctAnswerCounter == 8 and spriteClicked(multiAns1Label):
                incorrect = True
            elif correctAnswerCounter == 8 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 8 and spriteClicked(multiAns3Label):
                incorrect = True

            if correctAnswerCounter == 9 and spriteClicked(multiAns2Label):
                score += 10
                back()
            elif correctAnswerCounter == 9 and spriteClicked(multiAns1Label):
                incorrect = True
            elif correctAnswerCounter == 9 and spriteClicked(multiAns3Label):
                incorrect = True
            elif correctAnswerCounter == 9 and spriteClicked(multiAns4Label):
                incorrect = True

            if correctAnswerCounter == 10 and spriteClicked(multiAns3Label):
                score += 10
                back()
            elif correctAnswerCounter == 10 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 10 and spriteClicked(multiAns1Label):
                incorrect = True
            elif correctAnswerCounter == 10 and spriteClicked(multiAns4Label):
                incorrect = True

            if correctAnswerCounter == 11 and spriteClicked(multiAns3Label):
                score += 10
                back()
            elif correctAnswerCounter == 11 and spriteClicked(multiAns1Label):
                incorrect = True
            elif correctAnswerCounter == 11 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 11 and spriteClicked(multiAns4Label):
                incorrect = True

            if correctAnswerCounter == 12 and spriteClicked(multiAns1Label):
                score += 10
                back()
            elif correctAnswerCounter == 12 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 12 and spriteClicked(multiAns3Label):
                incorrect = True
            elif correctAnswerCounter == 12 and spriteClicked(multiAns4Label):
                incorrect = True

            if correctAnswerCounter == 13 and spriteClicked(multiAns1Label):
                score += 10
                back()
            elif correctAnswerCounter == 13 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 13 and spriteClicked(multiAns3Label):
                incorrect = True
            elif correctAnswerCounter == 13 and spriteClicked(multiAns4Label):
                incorrect = True

            if correctAnswerCounter == 14 and spriteClicked(multiAns1Label):
                score += 10
                back()
            elif correctAnswerCounter == 14 and spriteClicked(multiAns2Label):
                incorrect = True
            elif correctAnswerCounter == 14 and spriteClicked(multiAns3Label):
                incorrect = True
            elif correctAnswerCounter == 14 and spriteClicked(multiAns4Label):
                incorrect = True

            if incorrect:
                score -= 10
                changeLabel(Score, "Score : " + str(score))
                back()
                incorrect = False

    if touching(player, antidote):
        break

endWait()
