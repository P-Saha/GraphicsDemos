from pygame import *
from random import *
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    for i in range(0,1500,10):
        draw.line(screen,(0,255,0),(i,0),(0,i))
        draw.line(screen,(0,255,0),(0,i),(1500-i,1500))
        draw.line(screen,(0,255,0),(i,0),(1500,1500-i))
#-----------------------------------------------------
    display.flip()
quit()
    
