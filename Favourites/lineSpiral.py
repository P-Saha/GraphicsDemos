from pygame import *
from random import *
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    '''for i in range(0,310,10):
        draw.line(screen,(0,255,0),(400-i,300+i),(400+i,300+i))
        draw.line(screen,(0,255,0),(400+i,300-i),(400+i,300+i))
    for j in range(10,310,10):
        draw.line(screen,(0,255,0),(400+j,300-j),(400-j+10,300-j))
        draw.line(screen,(0,255,0),(400-j+10,300-j),(400-j+10,300+j-10))'''
    g=(0,255,0)
    line=10
    x1,y1=400,300
    x2,y2=400,300
    while 0<=y1<=600:
        y2=y1-line
        draw.line(screen,g,(x1,y1),(x2,y2))
        y1=y2
        
        x2=x1+line
        draw.line(screen,g,(x1,y1),(x2,y2))
        x1=x2
        line+=10

        y2=y1+line
        draw.line(screen,g,(x1,y1),(x2,y2))
        y1=y2

        x2=x1-line
        draw.line(screen,g,(x1,y1),(x2,y2))
        x1=x2
        line+=10
        
        
#-----------------------------------------------------
    display.flip()
quit()
    
