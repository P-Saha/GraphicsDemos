from math import *
from pygame import *
from random import *

#---------------------------------------------------------------------
sideUpperBound=30
sideLowerBound=5
sizeDecreaseRange=10
splitProb=3

def lightning(x, y, size, angle,bigy):
    convert = radians(angle)
    x2 = x-size*cos(convert)
    y2 = y+size*sin(convert)
    bigy=max(bigy,y)
    if y2>bigy:
        draw.line(screen,(200,180,0),(x,y),(x2,y2))
    else:
        return
    if size<5 or x2>800 or y2>600:
        return
    lightning(x2,y2,size-randint(1,sizeDecreaseRange),angle+(-1 if randint(0,1)==0 else 1) * randint(sideLowerBound,sideUpperBound),bigy)
    if randint(0,splitProb)==0:
        lightning(x2,y2,size-randint(1,sizeDecreaseRange),angle+(-1 if randint(0,1)==0 else 1) * randint(sideLowerBound,sideUpperBound),bigy)
    if randint(0,splitProb)==0:
        lightning(x2,y2,size-randint(1,sizeDecreaseRange),angle+(-1 if randint(0,1)==0 else 1) * randint(sideLowerBound,sideUpperBound),bigy)

#---------------------------------------------------------------------

screen = display.set_mode((800,600))

running = True

while running:

    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False

    screen.fill((0,0,0))
    lightning(400, 0, 100, randint(60,100),0)
    display.flip()

    time.wait(500)

quit()
