from pygame import *
from random import *
from math import *

def tree(x,y,ang,size,var,colour):
    x2=x+size*cos(radians(ang))
    y2=y-size*sin(radians(ang))
    variance=var//4
    cvar=255//max(1,size//10)
    pinkvar=randint(100,255)
    draw.line(screen,(cvar,cvar-20,cvar-20),(x,y),(x2,y2),int(size**(1/3)))
    if size>5:
        tree(x2,y2,ang-randint(30-variance,30+variance),size-10,var,colour)
        tree(x2,y2,ang+randint(0-variance,variance),size-10,var,colour)
        tree(x2,y2,ang+randint(30-variance,30+variance),size-10,var,colour)
    else:
        draw.circle(screen,(255,pinkvar,pinkvar),(int(x2),int(y2)),5)

screen=display.set_mode((1024,768))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
    screen.fill((0,0,0))
    tree(512,700,90,100,100,0)  
    display.flip()
quit()
