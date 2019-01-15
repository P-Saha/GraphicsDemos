from pygame import *
from random import *
from math import *
c=randint(0,2**24-1)
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    screen.fill((0,250,125))
    mb=mouse.get_pressed()
    mx,my = mouse.get_pos()
    
    for x in range(0,801,20):
        for y in range(0,601,20):
            dist=int(hypot(mx-x,my-y))
            dist=max(dist,1)
            rad=15-1000//dist
            rad=max(rad,1)
            draw.circle(screen,(111,111,111),(x,y),(rad))
#-----------------------------------------------------
    display.flip()
quit()
    
