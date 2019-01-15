from pygame import *
from random import *
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    if mb[0]==1:
        for i in range(-40,20,10):
            draw.circle(screen,(0,255,0),(mx+i,my+20),4)
            draw.circle(screen,(0,255,0),(mx-i,my-20),4)
            draw.circle(screen,(0,255,0),(mx-20,my+i),4)
            draw.circle(screen,(0,255,0),(mx+20,my-i),4)
#-----------------------------------------------------
    display.flip()
quit()
    
