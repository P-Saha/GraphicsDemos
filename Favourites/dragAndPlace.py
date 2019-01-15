from pygame import *
from random import *
screen=display.set_mode((800,600))
running=True
screen.fill((255,200,200))
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            pic=screen.copy()
#-----------------------------------------------------
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    pink=(255,200,200)
    blue=(200,200,255)
    grey=(111,111,111)
    
    if mb[0]==1:
        screen.blit(pic,(0,0))
        draw.circle(screen,blue,(mx,my),20)
        draw.circle(screen,grey,(mx,my),20,2)
        
#-----------------------------------------------------
    display.flip()
quit()
    
