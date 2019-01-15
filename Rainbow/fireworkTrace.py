from pygame import *
from random import *
screen=display.set_mode((800,600))
screen.fill((0,0,0))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    x=randint(0,800)
    y=randint(0,600)
    xx=randint(0,800)
    yy=randint(0,800)
    c=(randint(0,255),randint(0,255),randint(0,255))
    if mb[0]==1:
        draw.line(screen,c,(mx,my),(x,y),1)
    if mb[2]==1:
        screen.fill((0,0,0))
    display.flip()
quit()
    

