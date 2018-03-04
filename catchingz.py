import pygame
import random
from pygame.locals import *
from random import *

pygame.init()

display_width = 400
display_height = 400
zero_x = 0
zero_y = 0

gameDisplay = pygame.display.set_mode((display_width,display_height))
# pygame.display.seticon('Z')


imgInstagram = pygame.image.load('/Users/joshua/sHacks/images/instagram.png')
imgFacebook = pygame.image.load('/Users/joshua/sHacks/images/facebook.png')
imgSnapchat = pygame.image.load('/Users/joshua/sHacks/images/snapchat.png')
imgTwitter = pygame.image.load('/Users/joshua/sHacks/images/snapchat.png')
pillow = pygame.image.load('/Users/joshua/sHacks/images/pillow.png')


clock = pygame.time.Clock()

gray = (169,169,169)




def obstacleGen():
    randColumn = randint(1, 3)
    return randColumn

def randImage():
    image = randint(1, 3)
    if (image == 1):
        return imgInstagram
    elif (image == 2):
        return imgFacebook
    else:
        return imgSnapchat

def gameZ():
    gameStop = False
    obstacle_y = 0
    fallSpeed = 1.5
    obsColumn = 2
    playerColumn = 2
    time = 0
    img = randImage()
    while not gameStop: #cause they're trash
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                gameStop = True
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    if (playerColumn > 1):
                        playerColumn -= 1
                elif (event.key == pygame.K_RIGHT):
                    if (playerColumn < 3):
                        playerColumn += 1

        if (obstacle_y > zero_y + 700):
            obsColumn = obstacleGen()
            obstacle_y = zero_y - 80
            img = randImage()

        if obsColumn == playerColumn and obstacle_y >= zero_y + 270 and obstacle_y < 400 + zero_y:
            gameStop = True        
        
        obstacle_y += fallSpeed
        obstacle_x = zero_x + (obsColumn - 1) * 133 + 27

        gameDisplay.fill(gray)

        gameDisplay.blit(img, (obstacle_x, obstacle_y))
        gameDisplay.blit(pillow, ((zero_x + (playerColumn - 1) * 133 + 27),
                                   (zero_y + 320)))

        pygame.display.update()

        clock.tick(60)
        fallSpeed = min(6, 1.5 + pygame.time.get_ticks()/15000)
 
    pygame.quit()
    
gameZ()
