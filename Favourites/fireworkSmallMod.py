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
    screen.fill((0,0,0))
    if mb[0]==1:
        for i in range (40):
            c=randint(0,2**24-1)
            draw.line(screen,c,(mx,my),(mx+randint(-50,50),my+randint(-50,50)),2)     
    
#-----------------------------------------------------
    display.flip()
quit()
    
