from pygame import *
screen=display.set_mode((800,600))
screen.fill((255,0,0))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    for i in range(0,601,20):
        draw.line(screen,(0,0,0),(0,i),(800,i))
    for k in range(0,601,40):
        for j in range(20,781,40):
            draw.line(screen,(0,0,0),(j,k-20),(j,k))
    for k in range(-20,581,40):
        for j in range(0,801,40):
            draw.line(screen,(0,0,0),(j,k-20),(j,k))
    
        
    
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
