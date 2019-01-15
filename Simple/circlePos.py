from pygame import *
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    print(mx,my,mb)
    if mb[0]==1:
        draw.circle(screen,(170,255,50),(mx,my),10)
    if mb[2]==1:
        draw.circle(screen,(0,0,0),(mx,my),20)
    
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
