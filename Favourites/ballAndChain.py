from pygame import *
from random import *
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    screen.fill((0,0,0))
    mx,my=mouse.get_pos()
    dist=((400-mx)**2+(300-my)**2)**0.5
    dist=max(dist,1)
    sx=(mx-400)*10/dist
    sy=(my-300)*10/dist
    x,y=400,300
    for i in range(int(dist/10)):
        x+=sx
        y+=sy
        draw.circle(screen,(0,255,0),(int(x),int(y)),3)
    draw.circle(screen,(255,0,0),(mx,my),10)
    draw.circle(screen,(255,0,0),(400,300),10)
    #draw.circle(screen,(0,255,0),vertex,3)
    #draw.circle(screen,(0,255,0),vertex2,3) 
#-----------------------------------------------------
    display.flip()
quit()
    
