import pygame, sys
from pygame.locals import *
from random import *

display_width = 495
display_height = 180

pygame.init()
playing = True;

gameDisplay = pygame.display.set_mode((400, 400))

elapsed = pygame.time.get_ticks()/1000

#while elapsed < 20:
#elapsed = pygame.time.get_ticks()/1000


background = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\lined paper.png')
zero = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\\0.png')
one = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\\1.png')
two = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\\2.png')
three = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\\3.png')
four = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\\4.png')
five = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\\5.png')
six = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\\6.png')
seven = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\\7.png')
eight = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\\8.png')
nine = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\\9.png')
check = pygame.image.load('/Users\junwe\Downloads\schoolify-master\schoolify-master\sprites\grades\checkmark.png')

while elapsed > 0:
    gameDisplay.blit(background, (0,0))
    timeleft = max(5-(elapsed/15), 1)
    elapsed = pygame.time.get_ticks()/1000
    b = randint(10, 99)
    print (b)
    if int(b/10) == 9:
        gameDisplay.blit(nine, (100,100))
    elif int(b/10) == 8:
        gameDisplay.blit(eight, (100,100))
    elif int(b/10) == 7:
        gameDisplay.blit(seven, (100,100))
    elif int(b/10) == 6:
        gameDisplay.blit(six, (100,100))
    elif int(b/10) == 5:
        gameDisplay.blit(five, (100,100))
    elif int(b/10) == 4:
        gameDisplay.blit(four, (100,100))
        
    elif int(b/10) == 3:
        gameDisplay.blit(three, (100,100))
    elif int(b/10) == 2:
        gameDisplay.blit(two, (100,100))
    else:
        gameDisplay.blit(one, (100,100))
    if b%10 == 9:
        gameDisplay.blit(nine, (200,100))
    elif b%10 == 8:
        gameDisplay.blit(eight, (200,100))
    elif b%10 == 7:
        gameDisplay.blit(seven, (200,100))
    elif b%10 == 6:
        gameDisplay.blit(six, (200,100))
    elif b%10 == 5:
        gameDisplay.blit(five, (200,100))
    elif b%10 == 4:
        gameDisplay.blit(four, (200,100))
    elif b%10 == 3:
        gameDisplay.blit(three, (200,100))
    elif b%10 == 2:
        gameDisplay.blit(two, (200,100))
    elif b%10 == 1:
        gameDisplay.blit(one, (200,100))
    else:
        gameDisplay.blit(zero, (200,100))
        
    pygame.display.update()
    
            
    start_ticks=pygame.time.get_ticks()
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    if b > 49:
        should_break = True;
        
        while seconds < timeleft:
            for event in pygame.event.get():
                seconds=(pygame.time.get_ticks()-start_ticks)/1000
                if event.type == KEYDOWN and event.key == K_r:
                    should_break = False
                    gameDisplay.blit(check, (100,75))
                    pygame.display.update()
                    while seconds < timeleft:
                        seconds=(pygame.time.get_ticks()-start_ticks)/1000
                    break
        if should_break == True:
            pygame.quit()
            sys.exit()
    else:
        while seconds < timeleft:

            for event in pygame.event.get():
                seconds=(pygame.time.get_ticks()-start_ticks)/1000
                if event.type == KEYDOWN and event.key == K_r:
                    playing = False
                    break
                seconds=(pygame.time.get_ticks()-start_ticks)/1000
                if seconds < timeleft:
                    break
            if playing == False:
                pygame.quit()
                sys.exit()
                break
            
    if playing == False:
        pygame.quit()
        sys.exit()
    
