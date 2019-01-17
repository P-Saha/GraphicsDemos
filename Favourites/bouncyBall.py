from pygame import *

screen = display.set_mode((1024, 600))
boxx, boxy = 512,384
vx=2
vy=-5
mass=2
running = True
myClock = time.Clock()

while running:
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

    keys = key.get_pressed()
    if keys[27]: break
    if mb[0]==1:
        vy-=.50
    vy+=.25
    boxx+=vx
    boxy+=vy
    if boxy>600 or boxy<0:
        vy*=-1
    if boxx<0 or boxx>1024:
        vx*=-1
    screen.fill((0,0,0))
    draw.circle(screen, (255,0,0), (int(boxx),int(boxy)), 15)
            
    display.flip()

    myClock.tick(60)                        
    
quit()
