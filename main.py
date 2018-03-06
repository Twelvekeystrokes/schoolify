import pygame, random, sys, time, os
from random import *
from pygame.locals import *
from math import *

dh = 800
dw = 800

canvas = pygame.display.set_mode((display_width, display_height))

path = os.getcwd() + '/sprites/'

########################
# IMAGE ASSETS

## endgame
endFood = pygame.image.load(path + 'endscreen/endgamefood1.png')
congrats = pygame.image.load(path + 'endscreen/congratulations.png')
endGrade1 = pygame.image.load(path + 'endscreen/endgamegrade1.png')
endGrade2 = pygame.image.load(path + 'endscreen/endgamegrade2.png')
endSleep1 = pygame.image.load(path + 'endscreen/endgamesleep1.png')
endSleep2 = pygame.image.load(path + 'endscreen/endgamesleep2.png')
endSocial1 = pygame.image.load(path + 'endscreen/endgamesocial1.png')
endSocial2 = pygame.image.load(path + 'endscreen/endgamesocial2.png')

## food game
bgFood = pygame.image.load(path + 'food/food background.png')
foodBurger = pygame.image.load(path + 'food/burger.png')
garbageLeft = pygame.image.load(path + 'food/leftgarbage.png')
garbageRight = pygame.image.load(path + 'food/rightgarbage.png')

## sleep game
bgSleep = pygame.image.load(path + 'sleep/background.png')
iconFacebook = pygame.image.load(path + 'sleep/fb.png')
iconInstagram = pygame.image.load(path + 'sleep/instagram.png')
iconTwitter = pygame.image.load(path + 'sleep/twitter.png')
iconSnapchat = pygame.image.load(path + 'sleep/snapchat.png')
playerPillow = pygame.image.load(path + 'sleep/pillow.png')

## grades game
bgGrades = pygame.image.load(path + 'grades/lined paper.png')
gradeNumbers = []
for i in range(10):
    gradeNumbers.append(pygame.image.load(path + 'grades/' + str(i) + '.png'))
gradeCorrect = pygame.image.load(path + 'grades/checkmark.png')
gradeWrong = pygame.image.load(path + 'grades/X.png')

## speech game

bgSpeech = pygame.image.load(path + 'speech/background.png')
downText = []
upText = []
heart = pygame.image.load(path + 'speech/heart.png')
for i in range(1, 6):
    downText.append(pygame.image.load(path + 'speech/down' + str(i) + '.png'))
    upText.append(pygame.image.load(path + 'speech/up' + str(i) + '.png'))
downText.append(pygame.image.load(path + 'speech/down6.png'))

## infoBoxes
infoFood = pygame.image.load(path + 'infoFood.png')
infoGrades = pygame.image.load(path + 'infoGrades.png')
infoSpeech = pygame.image.load(path + 'infoSpeech.png')
infoSleep = pygame.image.load(path + 'infoSleep.png')
bgInfo = pygame.image.load(path + 'introbackground.png')

## border

border1 = pygame.image.load(path + 'frame1.png')
border2 = pygame.image.load(path + 'frame2.png')

#
#########################

white = (255, 255, 255)
gray = (169, 169, 169)
black = (0, 0, 0)

clock = pygame.time.Clock()

playing = True
gameStop = False

LEFT = -1
RIGHT = 1
foodPlayer = {
    'direction': LEFT,
    'x': 600,
    'y': 200 - 75/2,
    'speed': 1
    }

pause_time = 0
gradeIntro = False
foodIntro = False
sleepIntro = False
speechIntro = False
foodThreshold = 15
sleepThreshold = 25
speechThreshold = 45

def pausedGame():
    global pause_time
    paused = True
    pause_start = pygame.time.get_ticks()/1000
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                paused = False
    pause_time = pygame.time.get_ticks()/1000 - pause_start

################# INFORMATION FOR GAMES
#

def introGrades():
    canvas.blit(bgInfo, (25, 25))
    canvas.blit(infoGrades, (25, 25))
    canvas.blit(border2, (0, 0))
    pygame.display.update()
    pausedGame()

def introSpeech():
    canvas.blit(bgInfo, (425, 425))
    canvas.blit(infoSpeech, (425, 425))
    canvas.blit(border1, (0, 0))
    pygame.display.update()
    pausedGame()
    
def introFood():
    canvas.blit(bgInfo, (425, 25))
    canvas.blit(infoFood, (425, 25))
    canvas.blit(border1, (0, 0))
    pygame.display.update()
    pausedGame()

def introSleep():
    canvas.blit(bgInfo, (25, 425))
    canvas.blit(infoSleep, (25, 425))
    canvas.blit(border2, (0, 0))
    pygame.display.update()
    pausedGame()


#
#################

def time():
    global pause_time
    return pygame.time.get_ticks()/1000 - pause_time

def background():
    canvas.blit(bgGrades, (0,0))
    canvas.blit(bgFood, (400, 0))
    canvas.blit(bgSleep, (0, 400))

def randIcon():
    x = randint(1, 4)
    if x == 1:
        return iconFacebook
    elif x == 2:
        return iconSnapchat
    elif x == 3:
        return iconTwitter
    else:
        return iconInstagram

def randUp():
    return upText[randint(0, 4)]

def randDown():
    return downText[randint(0, 5)]

def game():
    global playing, gameStop, gradeIntro, foodIntro, sleepIntro, speechIntro, foodPlayer, foodThreshold
    global sleepThreshold, speechThreshold
    foodEnd = False
    sleepEnd = False
    speechEnd = False
    challenge = False
    challengeThreshold = 0
    timePassed = 0
    startTime = 0
    firstNum = randint(0, 9)
    secondNum = randint(0, 9)
    if firstNum >= 5:
        gradeEnd = True
    else:
        gradeEnd = False
    correct = False
    speech = False
    obstacle_y = 400
    sleepIcon = {
        'x': 0,
        'y': 400,
        'column': randint(1, 3),
        'fallSpeed': 1.5,
        }
    playerColumn = randint(1, 3)
    img = randIcon()
    text = randUp()
    up = 1
    textTime = 0
    textPassed = 0
    textStart = 0
    heart_y = -80
    firstgo = True
    timeEnd = False
    
    while playing:
        while not gameStop: #because steam is better
            if time() > 120:
                gameStop = True
                timeEnd = True
                
            canvas.blit(bgSleep, (0, 400))
        
            if time() >= sleepThreshold or challenge: ## sleepGame
                if not sleepIntro and not challenge:
                    introSleep()
                    sleepIntro = True
                if sleepIcon['y'] > 900:
                    sleepIcon['column'] = randint(1, 3)
                    sleepIcon['y'] = 320
                    img = randIcon()

                if sleepIcon['column'] == playerColumn and sleepIcon['y'] >= 670 and sleepIcon['y'] < 800:
                    sleepEnd = True
                    gameStop = True

                sleepIcon['y'] += sleepIcon['fallSpeed']
                sleepIcon['x'] = (sleepIcon['column'] - 1) * 133 + 27
                canvas.blit(img, (sleepIcon['x'], sleepIcon['y']))
                canvas.blit(playerPillow, ((playerColumn - 1) * 133 + 27, 720))
                sleepIcon['fallSpeed'] = max(1.5, min(7.5, 1.5 + time()/10 - sleepThreshold))
                if challenge:
                    sleepIcon['fallSpeed'] = max(3, min(14, 3 + time()/8))
            
            ####
                
            canvas.blit(bgGrades, (0,0))
            canvas.blit(bgSpeech, (400, 400))
            canvas.blit(bgFood, (400, 0))

            

            ## gradeGame
            
            gradesTime = ceil(max(5 - (time()/15), 1.5))
            if challenge:
                gradesTime = ceil(max(3 - time()/10, 0.75))

            if timePassed > gradesTime:
                correct = False
                if gradeEnd:
                    canvas.blit(gradeWrong, (80, 50))
                    canvas.blit(border1, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    gameStop = True
                    break
                else:
                    startTime = time()
                    firstNum = randint(0, 9)
                    secondNum = randint(0, 9)
                    if firstNum >= 5:
                        gradeEnd = True
                        
            timePassed = time() - startTime              
    
            ## gradesDisplay

            if (firstNum == 0):
                canvas.blit(gradeNumbers[secondNum], (140, 80))
            else:
                canvas.blit(gradeNumbers[firstNum], (80, 80))
                canvas.blit(gradeNumbers[secondNum], (200, 80))

            if correct:
                canvas.blit(gradeCorrect, (80, 50))
            
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    playing = False
                    gameStop = True
                            
                ## KEYPRESSES
                if event.type == KEYDOWN:
                    ## grades
                    if event.key == K_r:
                        if firstNum >= 5:
                            gradeEnd = False
                            correct = True
                        else:
                            gradeEnd = True
                            timePassed = gradesTime + 1
                        
                    ## food
                    if event.key == K_SPACE:
                        foodPlayer['direction'] *= -1
                        foodPlayer['speed'] = max(2, min(7, 2 + time()/12 - foodThreshold/5))
                        if challenge:
                            foodPlayer['speed'] += time()/5

                    ## sleep
                    if event.key == K_LEFT:
                        playerColumn = max(1, playerColumn - 1)
                    if event.key == K_RIGHT:
                        playerColumn = min(3, playerColumn + 1)
                    # to play all the games immediately with a higher difficulty
                    if event.key == K_i:
                        if challengeThreshold < 10:
                            challengeThreshold += 1
                        else:
                            challenge = True

                    ## speech
                    if event.key == K_UP:
                        heart_y = 485
                        if up == 1:
                            speechEnd = False
                        else:
                            speechEnd = True
                            
                    if event.key == K_DOWN:
                        heart_y = 675
                        if up == 0:
                            speechEnd = False
                        else:
                            speechEnd = True

                    ## pause
                    if event.key == K_p:
                        pausedGame()
                #    
                #######

            
            if time() >= foodThreshold or challenge: ## foodGame
                if not foodIntro and not challenge:
                    introFood()
                    foodIntro = True
                canvas.blit(garbageLeft, (425, 150))
                canvas.blit(garbageRight, (725, 150))
                if foodPlayer['x'] <= 450 or foodPlayer['x'] >= 675:
                    foodEnd = True
                    gameStop = True
                canvas.blit(foodBurger, (foodPlayer['x'] + foodPlayer['speed'] * foodPlayer['direction'], foodPlayer['y']))
                foodPlayer['x'] += foodPlayer['speed'] * foodPlayer['direction']

            ## speechGame
            
            textTime = ceil(min(max(8 - time()/7 + speechThreshold/7, 3) + 8, 8)) 
            if challenge:
                textTime = ceil(max(4 - time()/5, 1.5))

            textPassed = time() - textStart
            if time() >= speechThreshold or challenge: 
                if not speechIntro and not challenge:
                    introSpeech()
                    speechIntro = True
                    speechEnd = True
                    firstgo = True
                if textPassed > textTime:
                    speech = False
                    if speechEnd and not firstgo:
                        gameStop = True
                        break
                    elif speechEnd:
                        firstgo = False
                    up = randint(0, 1)
                    if not speechEnd:
                        if up == 0:
                            text = randDown()
                        else:
                            text = randUp()
                        speechEnd = True
                    heart_y = -50
                    textStart = time()
                    textPassed = 0
                    
                heart_x = 750
                canvas.blit(text, (400, 400))
                canvas.blit(heart, (heart_x, heart_y))
                
            ## borders

            if time() - floor(time()) < 0.16:
                canvas.blit(border1, (0, 0))
            elif time() - floor(time()) < 0.32:
                canvas.blit(border2, (0, 0))
            elif time() - floor(time()) < 0.48:
                canvas.blit(border1, (0, 0))
            elif time() - floor(time()) < 0.64:
                canvas.blit(border2, (0, 0))
            elif time() - floor(time()) < 0.8:
                canvas.blit(border1, (0, 0))
            elif time() - floor(time()) < 1:
                canvas.blit(border2, (0, 0))

            if not gradeIntro:
                introGrades()
                gradeIntro = True        
            
            pygame.display.update()
            clock.tick(60)

        canvas.fill((255, 255, 255))
        pygame.time.delay(3000)
        if timeEnd:
            canvas.blit(congrats, (257, 258))
        elif foodEnd:
            canvas.blit(endFood, (257, 258))
        elif sleepEnd:
            x = randint(1, 2)
            if x == 1:
                canvas.blit(endSleep1, (257, 258))
            else:
                canvas.blit(endSleep2, (257, 258))
        elif speechEnd:
            x = randint(1, 2)
            if x == 1:
                canvas.blit(endSocial1, (257, 258))
            else:
                canvas.blit(endSocial2, (257, 258))
        elif gradeEnd:
            x = randint(1, 2)
            if x == 1:
                canvas.blit(endGrade1, (257, 258))
            else:
                canvas.blit(endGrade2, (257, 258))
                
        pygame.display.update()
        pygame.time.delay(10000)
        pygame.quit()
        break

pygame.init()
game()
