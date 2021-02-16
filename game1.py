from pygame_functions import *
import random
from array import *

#add in instruction slides available everywhere
#add in the score system
#add in the life system


xArray = [88, 88, 88, 88, 88, 313, 543, 543, 543, 543, 543, 758, 983, 983, 983, 983, 983, 1208, 1423, 1423, 1423, 1423,1423, 1640]
yArray = [110, 300, 480, 670, 855, 855, 855, 670, 480, 300, 110, 110, 110, 300, 480, 670, 855, 855, 855, 670, 480, 300,110, 90]

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
creds = makeLabel("An Informative game developed for educating kids about personal hygine", 25, 680, 821, WHITE)
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

quizDispInd = 0
count = 0

multiAns1 = ['is not important',
             'Not harmful to the human body',
             'Putting on clean clothes after <br> running hard<br> at your soccer game',
             'Improved self-esteem', 'Caring for and cleaning our bodies<br> to promote good health and happiness',
             'Ice cubes in a tray',
             'Attacks',
             'Food is easier to remove from your<br> mouth at those times',
             'Viruses replicating themselves',
             '0 degrees fahrenheit',
             'It makes your teeth more brittle',
             'Immune system',
             'Most food has germs in it',
             'Teens are more likely to get dirty'
             ]

multiAns2 = ['Does not help with keeping us well',
             'Very small, microscopic living things<br> that can enter your body and make you sick',
             'Eating without washing your hands',
             'better heath',
             'Washing our hands',
             'Cars in a parking lot',
             'Ignores',
             "That's when most people<br> eat the most",
             'Bacteria digesting food',
             '32 degrees fahrenheit',
             'It makes your nails too short',
             'Circulatory system',
             'You may not have enough napkins',
             'Teens have oilier skin'
             ]
multiAns3 = ['Is a collection of habits people perform<br>to keep themselves<br> clean and their bodies healthy',
             'Not alive',
             'Brushing your teeth once a month',
             'Others will have a<br> better perception of you',
             'Doing something<br> to improve our self-esteem',
             'Trees in a park',
             'Nurtures',
             "It's easier to remember<br> to do at those times",
             'Skin glands secreting oils',
             '100 degrees fahrenheit',
             'It transfers bacteria between<br> your mouth and hands',
             'Nervous system',
             'You might touch your<br> mouth while you eat',
             'Teens have a stronger sense of smell'
             ]

multiAns4 = ['Increases the number of<br> germs that enter our bodies',
             'So big that you can obviously see them and<br> prevent them from entering your body and<br> making you sick',
             'Not taking a shower after you <br> play outside in the mud',
             'All of the answers are correct.',
             'All of the answers are correct.',
             'Grains of sand on a beach',
             'Multiplies',
             'Bacteria continue to digest<br> food in your mouth at night',
             'A reaction between oxygen<br> and body secretion',
             '212 degrees fahrenheit',
             'It prevents bacteria from<br> digesting food in your mouth',
             'Respiratory system',
             'The food may not have been<br> prepared in a clean environment',
             'Teens are more concerned about<br> their appearance'
             ]

questions = ["(fill in the blank) Personal hygiene___",
             "(fill in the blank) Germs are ____",
             'Which of the following is an example of having good personal hygiene?',
             'What is a benefit of practicing good personal hygiene?',
             "What do we mean when we say 'good personal hygiene'?",
             'The number of germs on your hands is comparable to the number of',
             '(fill in the blank) Good personal hygiene _____ harmful germs on your body',
             'Which is the most likely reason for brushing your teeth in<br> the morning and before bed?',
             'Bad breath and body odor are produced by:',
             'Which water temperature is ideal for washing your hands?',
             'How can biting your nails be harmful to your health?',
             'Poor hygiene has the most direct effect on which body system?',
             'Why is it important to wash your hands before meals?',
             'Teenagers should probably shower more often than younger kids because:'
             ]

questionsX = [515, 515, 148, 352, 352, 180, 90, 384, 464, 308, 308, 260, 372, 94]
questionsY = [157, 157, 162, 162, 162, 168, 160, 122, 166, 158, 158, 158, 158, 172]
ans1X = [238, 159, 159, 136, 218, 108, 260, 134, 160, 200, 150, 220, 188, 154]
ans2X = [144, 89, 150, 136, 264, 236, 252, 186, 192, 192, 164, 216, 132, 228]
ans3X = [1273, 1464, 1328, 1320, 1378, 1358, 1450, 1376, 1382, 1378, 1350, 1408, 1376, 1302]
ans4X = [1370, 1355, 1346, 1346, 1346, 1346, 1460, 1350, 1364, 1382, 1334, 1398, 1314, 1336]
ans1Y = [539, 539, 539, 528, 538, 528, 540, 534, 544, 544, 542, 542, 546, 544]
ans2Y = [884, 868, 882, 880, 876, 882, 884, 860, 876, 876, 880, 880, 880]
ans3Y = [518, 544, 554, 552, 530, 546, 538, 552, 550, 538, 544, 526, 554]
ans4Y = [873, 873, 866, 866, 888, 888, 892, 870, 874, 888, 862, 884, 870, 872]

xArraySoap = [70, 70, 70, 70, 300, 520, 520, 520, 520, 520, 750, 970, 970, 970, 970, 970, 1190, 1410, 1410, 1410, 1410,1410]
yArraySoap = [330, 510, 700, 880, 880, 880, 700, 510, 330, 140, 140, 140, 330, 510, 700, 880, 880, 880, 700, 510, 300,140]

xArrayVirus = [70, 70, 70, 300, 520, 520, 520, 520, 520, 750, 970, 970, 970, 970, 970, 1190, 1410, 1410, 1410, 1410,141]
yArrayVirus = [480, 660, 850, 850, 850, 670, 480, 300, 110, 110, 110, 290, 480, 660, 850, 850, 850, 670, 480, 290, 110]

p = False

def instState():
    setBackgroundImage('textures/instBoard.PNG')
    instButtons = makeSprite('textures/instBoard.PNG')
    instQuiz = makeSprite('textures/instButtons.png')




def start():
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


questionLabel = makeLabel(questions[quizDispInd], 55, questionsX[quizDispInd], questionsY[quizDispInd], WHITE,
                          'Calibri', 'clear')
multiAns1Label = makeLabel(multiAns1[quizDispInd], 29, ans1X[quizDispInd], ans1Y[quizDispInd], WHITE, 'Calibri',
                           'clear')
multiAns2Label = makeLabel(multiAns2[quizDispInd], 29, ans2X[quizDispInd], ans2Y[quizDispInd], WHITE, 'Calibri',
                           'clear')
multiAns3Label = makeLabel(multiAns3[quizDispInd], 29, ans3X[quizDispInd], ans3Y[quizDispInd], WHITE, 'Calibri',
                           'clear')
multiAns4Label = makeLabel(multiAns4[quizDispInd], 29, ans4X[quizDispInd], ans4Y[quizDispInd], WHITE, 'Calibri',
                           'clear')
score = 0
Score = makeLabel(f"score{score}", 5,5, 5, WHITE, 'Calibri', 'clear')


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


def back():
    hideAll()
    hideLabel(questionLabel)
    for vi in range(0,12):
        showSprite(f'virus{vi}')
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
    for sp in range(0,9):
        showSprite(f'soap{sp}')
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


from pygame_functions import *

xTemp = 1000
yTemp = 500

while True:

    if keyPressed("right"):
        xTemp += 10
        moveSprite(Score, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    if keyPressed("left"):
        xTemp -= 10
        moveSprite(Score, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    if keyPressed("up"):
        yTemp -= 10
        moveSprite(Score, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    if keyPressed("down"):
        yTemp += 10
        moveSprite(Score, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    tick(120)

    if spriteClicked(playPress):
        hide1()
        start()
        showSprite(antidote)

    if touching(player, virus0):
        showSprite(buttons)
        quizFunc1()
        hideSprite(virus0)
        moveSprite(virus0, 9999, 9999)

        print(quizDispInd)
        print("quizDispInd" + str(quizDispInd))
        p = True

    if touching(player, virus1):
        quizDispInd += 1
        if quizDispInd == 1:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus1)
            moveSprite(virus1, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus2):
        quizDispInd += 1
        if quizDispInd == 2:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus2)
            moveSprite(virus2, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus3):
        quizDispInd += 1
        if quizDispInd == 3:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus3)
            moveSprite(virus3, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus4):
        quizDispInd += 1
        if quizDispInd == 4:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus4)
            moveSprite(virus4, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus5):
        quizDispInd += 1
        if quizDispInd == 5:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus5)
            moveSprite(virus5, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus6):
        quizDispInd += 1
        if quizDispInd == 6:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus6)
            moveSprite(virus6, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus7):
        quizDispInd += 1
        if quizDispInd == 7:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus7)
            moveSprite(virus7, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus8):
        quizDispInd += 1
        if quizDispInd == 8:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus8)
            moveSprite(virus8, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus9):
        quizDispInd += 1
        if quizDispInd == 9:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus9)
            moveSprite(virus9, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus10):
        quizDispInd += 1
        if quizDispInd == 10:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus10)
            moveSprite(virus10, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus11):
        quizDispInd += 1
        if quizDispInd == 11:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus11)
            moveSprite(virus11, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus12):
        quizDispInd += 1
        if quizDispInd == 12:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus12)
            moveSprite(virus12, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, virus13):
        quizDispInd += 1
        if quizDispInd == 13:
            showSprite(buttons)
            quizFunc1()
            hideSprite(virus13)
            moveSprite(virus13, 9999, 9999)
            print(quizDispInd)
            print("quizDispInd" + str(quizDispInd))
            p = True

    if touching(player, soap0):
        hideSprite(soap0)
        moveSprite(soap0, 9999, 9999)
        score += 10

    if touching(player, soap1):
        hideSprite(soap1)
        moveSprite(soap1, 9999, 9999)
        score += 10

    if touching(player, soap2):
        hideSprite(soap2)
        moveSprite(soap2, 9999, 9999)
        score += 10

    if touching(player, soap3):
        hideSprite(soap3)
        moveSprite(soap3, 9999, 9999)
        score += 10

    if touching(player, soap4):
        hideSprite(soap4)
        moveSprite(soap4, 9999, 9999)
        score += 10

    if touching(player, soap5):
        moveSprite(soap5, 9999, 9999)
        hideSprite(soap5)
        score += 10

    if touching(player, soap6):
        moveSprite(soap6, 9999, 9999)
        hideSprite(soap6)
        score += 10

    if touching(player, soap7):
        moveSprite(soap7, 9999, 9999)
        hideSprite(soap7)
        score += 10

    if touching(player, soap8):
        moveSprite(soap8, 9999, 9999)
        hideSprite(soap8)
        score += 10

    if touching(player, soap9):
        moveSprite(soap9, 9999, 9999)
        hideSprite(soap9)
        score += 10

    tick(120)

    if keyPressed("space"):
        print(str(count))
        moveSprite(player, xArray[count], yArray[count])
        count = count + 1
        pause(200)

    if count == 24:
        count = count = 0
        start()
    tick(20)

    if p:
        if keyPressed("g"):
            print("djbfhdf")
            moveLabel(questionLabel, 9999, 9999)
            back()
        if keyPressed("b"):
            print("djbfhdf")
            moveLabel(questionLabel, 9999, 9999)
            back()
        if keyPressed("r"):
            print("djbfhdf")
            moveLabel(questionLabel, 9999, 9999)
            back()
        if keyPressed("y"):
            print("djbfhdf")
            moveLabel(questionLabel, 9999, 9999)
            back()
            p = False
    if touching(player, antidote):
        break

endWait()
