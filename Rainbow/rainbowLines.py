from pygame import *
from random import *
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    x=randint(0,800)
    y=randint(0,600)
    xx=randint(0,800)
    yy=randint(0,800)
    c=(randint(0,255),randint(0,255),randint(0,255))
    draw.line(screen,c,(x,y),(xx,yy),2)
    
#-----------------------------------------------------
    display.flip()
quit()
    
#pygame.draw.line(Surface,Color,star.pos,end.pos,width=1)

#Surface-screen is default surface

#Color-Pygame uses RGB tuples for it's colour.
#   e.g.
#       (225,0,0)       -Red
#       (0,255,0)       -Green
#       (255,255,255)   -White
#       (111,111,111)   -Grey
#       (0,0,0)         -Black
#       (255,255,0)     -Yellow
#       (255,0,255)     -Magenta
#       (0,255,255)     -Cyan
