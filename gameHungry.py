import pygame, sys
from pygame.locals import *

FPS = 30
WINWIDTH = 400
WINHEIGHT = 400
SPACE = 'space'
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

# colours
WHITE = (255, 255, 255)
BLACK = (0  , 0  , 0 )


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Multi-Game')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)
    introText = BASICFONT.render('press spacebar to keep it up', True, WHITE)
    moveSpeed = 20
    const_x = WINWIDTH / 2
    current_y = WINHEIGHT / 2
    DISPLAYSURF.fill(WHITE)
    RECTHEIGHT = 350
    RECTWIDTH = 200
    drawRectangle(RECTWIDTH, RECTHEIGHT, WINWIDTH, WINHEIGHT)
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            pygame.display.update()

        

def drawRectangle(rw, rh, ww, wh):
    pygame.draw.rect(DISPLAYSURF, BLACK, #((re[2] - re[0]) / 2, (re[3] - re[1]) / 2, re[0], re[1]))
                     ((ww - rw) / 2, (wh - rh) / 2, rw, rh))
        
def terminate():
    pygame.quit()
    sys.exit()


    

main()
