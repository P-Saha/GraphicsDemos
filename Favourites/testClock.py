from pygame import *
import datetime
from math import *

screen = display.set_mode((1024,768))
def clock(hour,minute,sec):
    centre=(512,384)
    draw.circle(screen,2**24-1,centre,100)
    for i in range(0,360):
        hourp1=(512+100*sin(radians(i*30)),384+100*cos(radians(i*30)))
        hourp2=(512+90*sin(radians(i*30)),384+90*cos(radians(i*30)))
        draw.line(screen,0,hourp1,hourp2,2)
        minp1=(512+100*sin(radians(i*6)),384+100*cos(radians(i*6)))
        minp2=(512+98*sin(radians(i*6)),384+98*cos(radians(i*6)))
        draw.line(screen,0,minp1,minp2)
    sechand=(512+100*cos(radians(360/60*(sec-15))),384+100*sin(radians(360/60*(sec-15))))
    minhand=(512+100*cos(radians(360/60*(minute-15))),384+100*sin(radians(360/60*(minute-15))))
    hourhand=(512+50*cos(radians(360/12*(hour-3))),384+50*sin(radians(360/12*(hour-3))))
    draw.line(screen,(255,0,0),centre,sechand)
    draw.line(screen,0,centre,minhand)
    draw.line(screen,0,centre,hourhand,3)
    
running=True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
            
    screen.fill((204,117,77))

    now = datetime.datetime.now()
    clock(now.hour, now.minute, now.second)
    display.flip()
    time.wait(100)

quit()
