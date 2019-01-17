#sierp:
#    -triangle
#    -sierp
#    -sierp
#    -sierp
from pygame import *
screen=display.set_mode((1024,1000))
def tri(x,y,size):
    h=(size**2-(size/2)**2)**.5
    points=[(x,y),(x+size,y),(x+size/2,y-h)]
    draw.polygon(screen,(255,255,0),points,1)
    display.flip()
def sierp(x,y,size):
    tri(x,y,size)
    if size>3:
        sierp(x,y,size/2)
        sierp(x+size/2,y,size/2)
        h=size*0.433
        sierp(x+size/4,y-h,size/2)

         
running=True
sierp(200,700,600)
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
    
    
    display.flip()
quit()
