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
    mx,my = mouse.get_pos()
    screen.fill((0))
    for i in range(0,801,80):
        draw.line(screen,0x00FF00,(mx-50+i/8,my-50),(i,0))
        draw.line(screen,0x00FF00,(mx-50+i/8,my+50),(i,600))
    for i in range(0,601,60):
        draw.line(screen,0x00FF00,(mx-50,my-50+i/6),(0,i))
        draw.line(screen,0x00FF00,(mx+50,my-50+i/6),(800,i))
#-----------------------------------------------------
    display.flip()
quit()
    
