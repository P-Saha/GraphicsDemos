from pygame import *
from random import *
from math import *

def loop(a,b,c):
        for c in range(a,b,c):   
            screen.fill((0,0,0))
            for x in range(0,801,40):
                for y in range(40,601-40,20):
                    co=randint(0,2**24-1)
                    draw.line(screen,co,(x,y),(x+20,y+c))
                    draw.line(screen,co,(x,y),(x-20,y+c))
            time.wait(30)
            display.flip()
            
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
        loop(20,-20,-1)
        loop(-20,20,1)
#-----------------------------------------------------
quit()
