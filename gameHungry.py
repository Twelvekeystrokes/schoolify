import pygame, sys, time
from pygame.locals import *
# constants
FPS = 30
WINWIDTH = 400
WINHEIGHT = 400
SPACE = 'space'
RECTHEIGHT = 200
RECTWIDTH = 350

DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

#images
sprite = pygame.image.load('/Users\Steph\OneDrive\Documents\GitHub\schoolify\sprites\\food\\burger.png')
garbageLeft = pygame.image.load('/Users\Steph\OneDrive\Documents\GitHub\schoolify\sprites\\food\\leftgarbage.png')
garbageRight = pygame.image.load('/Users\Steph\OneDrive\Documents\GitHub\schoolify\sprites\\food\\rightgarbage.png')
background = pygame.image.load('/Users\Steph\OneDrive\Documents\GitHub\schoolify\sprites\\food\\food background.png')

# colours
WHITE = (255, 255, 255)
BLACK = (0  , 0  , 0 )

def main():
    #global variables
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    
    pygame.init()
    FPSCLOCK = pygame.time.Clock() # apparently necessary
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Multi-Game') # window title
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32) # font

    # constants
    DISPLAYSURF.fill(WHITE)
    LEFT = -1
    RIGHT = 1
    
    # variables
    playerObj = {
        'direction': LEFT,
        'x': WINWIDTH / 2,
        'y': WINHEIGHT / 2 - 75 / 2, #sprite height
        'speed': 1
        }

    # texts
    introText = BASICFONT.render('press spacebar to keep it up', True, WHITE)

    # draws rectangle
    #drawRectangle(RECTWIDTH, RECTHEIGHT, WINWIDTH, WINHEIGHT)
    while True:
        DISPLAYSURF.blit(background, (0,0))
        DISPLAYSURF.blit(garbageLeft, (25, 150))
        DISPLAYSURF.blit(garbageRight, (325, 150))
        #drawRectangle(RECTWIDTH, RECTHEIGHT, WINWIDTH, WINHEIGHT)
        if playerObj['x'] <= 50 or playerObj['x'] >= 275:
            terminate()

        DISPLAYSURF.blit(sprite, (playerObj['x'] + playerObj['speed'] * playerObj['direction'], playerObj['y']))
        playerObj['x'] += playerObj['speed'] * playerObj['direction']
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN and event.key == K_SPACE:
                if playerObj['direction'] == LEFT:
                    playerObj['direction'] = RIGHT
                elif playerObj['direction'] == RIGHT:
                    playerObj['direction'] = LEFT
                    
        playerObj['speed'] = min(10, 1.5 + pygame.time.get_ticks()/10000)
                    
        FPSCLOCK.tick(FPS)
        pygame.display.update()

        

#def drawRectangle(rw, rh, ww, wh):
#    pygame.draw.rect(DISPLAYSURF, BLACK, ((ww - rw) / 2, (wh - rh) / 2, rw, rh))
        
def terminate():
    pygame.quit()
    sys.exit()


main()
