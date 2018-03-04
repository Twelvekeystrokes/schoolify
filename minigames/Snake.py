import pygame
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')

icon = pygame.image.load('C:/Users/User/PycharmProjects/Intro/Apple.png')
pygame.display.set_icon(icon)

pygame.mixer.music.load('C:/Users/User/PycharmProjects/Intro/videoplayback.mp3')

img = pygame.image.load('C:/Users/User/PycharmProjects/Intro/Snakehead.png')
appleimg = pygame.image.load('C:/Users/User/PycharmProjects/Intro/Apple.png')
snakeimg = pygame.image.load('C:/Users/User/PycharmProjects/Intro/Snakebody.png')

gray = (47,79,79)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

pygame.display.update()

clock = pygame.time.Clock()
block_size = 20
AppleThickness = 30
FPS = 13

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False

        gameDisplay.fill(white)
        message_to_screen("Paused",
                          black,
                          -100,
                          size='large')
        message_to_screen("Press C to continue",
                          black,
                          25)
        pygame.display.update()
        clock.tick(10)


def score(score):
    text = smallfont.render("Score: "+str(score), True, white)
    gameDisplay.blit(text, [10,0])


def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0

    return randAppleX,randAppleY


def game_start():

    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                start = False

            gameDisplay.fill(black)
            message_to_screen("AscendancyEight Studios presents",
                              red)

            pygame.display.update()
            clock.tick(15)


def game_intro():

    pygame.mixer.music.play(-1)

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            gameDisplay.fill(white)
            message_to_screen("Snake",
                              green,
                              -100,
                              "large")
            message_to_screen("Arrow keys to move",
                              black,
                              -10, )
            message_to_screen("Eat red apples",
                              black,
                              30,)
            message_to_screen("The more apples you eat, the longer you get",
                              black,
                              70,)
            message_to_screen("If you run into yourself or the borders of the screen, you die!",
                              black,
                              110,)
            message_to_screen("Press C to play, P to pause, or Q to quit",
                              black,
                              210, )

            pygame.display.update()
            clock.tick(15)


def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        #pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
        gameDisplay.blit(snakeimg, (XnY[0],XnY[1]))

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color, y_displace=0, size="small"):

    textSurf, textRect = text_objects(msg, color, size)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():

    global direction
    direction = 'right'

    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",
                              red,
                              y_displace=-50,
                              size="large")
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              y_displace=50,
                              size="small")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change  = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if (lead_x + lead_x_change) >= display_width or (lead_x + lead_x_change) < 0 or (
            lead_y + lead_y_change) >= display_height or (lead_y + lead_y_change) < 0:
            gameOver = True

            # Stop move afer letting go of key (other non snake games
            # if event.type == pygame.KEYUP:
                # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    # lead_x_change = 0
                # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    # lead_y_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(gray)

        #pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,AppleThickness,AppleThickness])
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        score(snakeLength - 1)
        snake(block_size, snakeList)

        pygame.display.update()

        #if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
            #if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
                #randAppleX = round(random.randrange(0, display_width - AppleThickness)) #/10.0)*10.0
                #randAppleY = round(random.randrange(0, display_height - AppleThickness)) #/10.0)*10.0
                #snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

game_start()
game_intro()
gameLoop()
