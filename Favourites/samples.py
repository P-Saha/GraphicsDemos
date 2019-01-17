from pygame import *
from random import *
from math import *
colours=[]
for i in range(20):
    colour=(randint(0,255),randint(0,255),randint(0,255))
    colours.append(colour)
def sections(a,b,c):
    if mb[0]==1 and mx>a and mx<b:
        d=colours[c]
        draw.line(screen,d,(mx,my),(randint(mx-20,mx+20),randint(my-20,my+20)))
screen=display.set_mode((800,600))
running=True
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-----------------------------------------------------
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    for j in range(0,800,40):
        k=j//40
        draw.rect(screen,colours[k],(j,280,40,40))
        sections(j,j+40,j//40)
    if mb[2]==1:
        screen.fill((0,0,0))
        for j in range(0,800,40):
            k=j//40
            draw.rect(screen,colours[k],(j,280,40,40))        
#-----------------------------------------------------
    display.flip()
quit()
