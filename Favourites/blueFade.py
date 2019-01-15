from pygame import *
from random import *
from math import *
g=(0,255,0)

def loop(a,b,d):
    for c in range(a,b,d):
        for j in range(100,701,20):
            draw.line(screen,g,(j,100),(j,120))
            draw.line(screen,g,(j,500),(j,480))
        for k in range(100,501,20):
            draw.line(screen,g,(100,k),(120,k))
            draw.line(screen,g,(700,k),(680,k))
        draw.rect(screen,(0,255,0),(120,120,560,360),2)
        draw.rect(screen,(0,255,0),(100,100,600,400),2)
        draw.rect(screen,(0,0,c),(121,121,558,358))
        time.wait(7)
        display.flip()
            
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
        loop(0,256,1)
        loop(255,-1,-1)
#-----------------------------------------------------
quit()
