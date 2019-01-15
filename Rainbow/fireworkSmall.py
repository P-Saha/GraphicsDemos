from pygame import *
from random import *
from math import * 
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    c=randint(0,2**24-1)
    if mb[0]==1:
        draw.line(screen,c,(mx,my),(mx+randint(-20,20),my+randint(-20,20)),2)
    if mb[2]==1:
        screen.fill((0,0,0))
#-----------------------------------------------------
    display.flip()
quit()
    
