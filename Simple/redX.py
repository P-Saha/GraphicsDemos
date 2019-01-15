
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
        draw.line(screen,(255,0,0),(mx+20,my-20),(mx-20,my+20),1)
        draw.line(screen,(255,0,0),(mx-20,my-20),(mx+20,my+20),1)
    if mb[2]==1:
        draw.circle(screen,(0,255,0),(mx,my),20,1)
#-----------------------------------------------------
    display.flip()
quit()
    
