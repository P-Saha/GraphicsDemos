from pygame import *
from random import *
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    screen.fill((255, 255, 255))
    draw.line(screen, (0, 0, 0), (400, 100), (400, 500), 2)
    draw.line(screen, (0, 0, 0), (200, 300),  (600, 300), 2)

    for i in range(0, 200, 10):
        draw.line(screen, (0, 0, 0), (400+i, 100+i), (400+i, 300))
        draw.line(screen, (0, 0, 0), (400+i, 500-i), (400+i, 300))
        draw.line(screen, (0, 0, 0), (400-i, 100+i), (400-i, 300))
        draw.line(screen, (0, 0, 0), (400-i, 500-i), (400-i, 300))
        
    
        
#-----------------------------------------------------
    display.flip()
quit()
