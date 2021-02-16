from pygame_functions import *
import random
screenSize(1920, 1080)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

'''
https://study.com/academy/practice/quiz-worksheet-personal-hygiene.html
https://www.brainpop.com/health/personalhealth/personalhygiene/quiz/
https://quizizz.com/admin/quiz/56a13ae99add0a34079ce31a/personal-hygiene-review
https://www.dayjob.com/food-hygiene-quiz-829/
'''

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


ans1 = ['is not important',
        'Does not help with keeping us well',
        'Is a collection of habits people perform<br>to keep themselves clean and their bodies healthy',
        'Increases the number of germs that enter our bodies']

ans2 = ['Not harmful to the human body',
        'Very small, microscopic living things<br> that can enter your body and make you sick',
        'Not alive',
        'So big that you can obviously see them and<br> prevent them from entering your body and<br> making you sick']

ans3 = ['Putting on clean clothes after <br> running hard at your soccer game',
        'Eating without washing your hands',
        'Brushing your teeth once a month',
        'Not taking a shower after you <br> play outside in the mud']


ans4 = ['Improved self-esteem','better heath','Others will have a<br> better perception of you','All of the answers are correct.']
ans5 = ['Caring for and cleaning our bodies<br> to promote good health and happiness','Washing our hands','Doing something<br> to improve our self-esteem','All of the answers are correct.']
ans6 = ['Ice cubes in a tray','Cars in a parking lot','Trees in a park', 'Grains of sand on a beach']
ans7 = ['Attacks','Ignores','Nurtutres','Multiplies']
ans8 = ['Food is easier to remove from your<br> mouth at those times',"That's when most people<br> eat the most","It's easier to remember<br> to do at those times",'Bacteria continue to digest food in your mouth at night']
ans9 = ['Viruses repicating themselves','Bacteria digesting food','Skin glands secreting oils','A reaction between oxygen and body secretion']
ans10 = ['0 degrees fahrenheit','32 degrees fahrenheit','100 degrees fahrenheit','212 degrees fahrenheit']
ans11 = ['It makes your teeht more brittle','It makes your nails too short','It transfers bacteria between your mouth and hands','It prevents bacteria from digesting food in your mouth']
ans12 = ['Immune system','Circulatory system','Nervous system','Respiratory system']
ans13 = ['Most food has germs in it','You may not have enough napkins','You might touch your mouth while you eat','The food may not have been prepared in a clean enviornment']
ans14 = ['Teens are more likely to get dirty','Teens have oiler skin','Teens have a stronger sense of smell','Teens are more concerned about thier apprearance']

question1 = questions[0]
question2 = questions[1]
question3 = questions[2]
question4 = questions[3]
question5 = questions[4]
question6 = questions[5]
question7 = questions[6]
question8 = questions[7]
question9 = questions[8]
question10 = questions[9]
question11 = questions[10]
question12 = questions[11]
question13 = questions[12]
question14 = questions[13]

questionLabel = makeLabel(question8, 55, 384, 122, WHITE,'Calibri')

multiAns1Label = makeLabel(ans8[0], 29, 134, 534, WHITE, 'Calibri','clear')

multiAns2Label = makeLabel(ans8[1], 29, 192, 868, WHITE, 'Calibri','clear')

multiAns3Label = makeLabel(ans8[2], 29, 1450, 546, WHITE, 'Calibri','clear')

multiAns4Label = makeLabel(ans8[3], 29, 1460, 892, WHITE, 'Calibri','clear')

buttons = makeSprite("textures/buttons_nodisp.png")

xTemp = 1000
yTemp = 500

showSprite(buttons)
showLabel(questionLabel)
showSprite(multiAns1Label)
showSprite(multiAns2Label)
showSprite(multiAns3Label)
showSprite(multiAns4Label)



while True:
    if keyPressed("right"):
        xTemp += 2
        moveLabel(multiAns2Label, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    if keyPressed("left"):
        xTemp -= 2
        moveLabel(multiAns2Label, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    if keyPressed("up"):
        yTemp -= 2
        moveLabel(multiAns2Label, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    if keyPressed("down"):
        yTemp += 2
        moveLabel(multiAns2Label, xTemp, yTemp)
        print(f"x:{xTemp} y:{yTemp}")
        tick(120)
    tick(120)
