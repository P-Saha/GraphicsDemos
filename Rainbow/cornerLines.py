from pygame import *
from random import *
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    if mb[0]==1:
        c=(randint(0,255),randint(0,255),randint(0,255))
        if mx<400 and my<300:
            draw.line(screen,c,(mx,my),(0,0))
        if mx>400 and my>300:
            draw.line(screen,c,(mx,my),(800,600))
        if mx<400 and my>300:
            draw.line(screen,c,(mx,my),(0,600))
        if mx>400 and my<300:
            draw.line(screen,c,(mx,my),(800,0))
        
#-----------------------------------------------------
    display.flip()
quit()
    
