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
    screen.fill((255,255,255))
    mx,my=mouse.get_pos()
    for x in range(0,801,40):
        for y in range(0,601,40):
            d=hypot(mx-x,my-y)
            d=max(d,1)
            bx=mx-x
            by=my-y
            sx=bx/d*20
            sy=by/d*20
            draw.line(screen,(0,0,0),(x,y),(x+sx,y+sy),2)
            draw.circle(screen,(255,0,0),(x,y),3)
#-----------------------------------------------------
    display.flip()
quit()

