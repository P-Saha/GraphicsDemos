from pygame import *
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    draw.line(screen,(255,0,0),(0,0),(100,200),2)
    draw.rect(screen,(0,255,255),(400,100,100,50))
                                #(x,y,width,height)
    draw.circle(screen,(255,50,100),(50,300),50,5)
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
