from pygame import *
from random import *
screen=display.set_mode((1000,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    mb=mouse.get_pressed()
    mx,my = mouse.get_pos()
    dist=int(((500-mx)**2 + (300-my)**2)**0.5)
    dist=max(dist,1)
    c=randint(0,2**24-1)
    if mb[0]==1:
        draw.circle(screen,(c),(mx,my),int(dist/6))
    if mb[2]==1:
        screen.fill((0,0,0))
    
    #draw.circle(screen,(0,255,0),vertex,3)
    #draw.circle(screen,(0,255,0),vertex2,3) 
#-----------------------------------------------------
    display.flip()
quit()
    
