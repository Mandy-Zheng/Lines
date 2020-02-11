from display import *
from draw import *
import random


s = new_screen()
c = [ 255, 255, 255 ]
def snow(size,x,y):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(190,255)
    c = [ r, g, b]
    straight=True
    draw_line(x,y,x,y+15*4*size,s,c)
    tempx=x
    tempy=y+15*size
    for j in range(3):
        draw_line(tempx,tempy,tempx+15*size,tempy+15*size,s,c)
        draw_line(tempx-15*size,tempy+15*size,tempx,tempy,s,c)
        tempy=tempy+15*size
    draw_line(x,y,x+10*4*size,y+10*4*size,s,c)
    tempx=x+10*size
    tempy=y+10*size
    for j in range(3):
        draw_line(tempx,tempy,tempx,tempy+15*size,s,c)
        draw_line(tempx,tempy,tempx+15*size,tempy,s,c)
        tempy=tempy+10*size
        tempx=tempx+10*size
    tempx=x+15*size
    tempy=y
    draw_line(x,y,x+15*4*size,y,s,c)
    for j in range(3):
        draw_line(tempx,tempy,tempx+10*size,tempy+10*size,s,c)
        draw_line(tempx,tempy,tempx+10*size,tempy-10*size,s,c)
        tempx=tempx+15*size
    tempx=x+10*size
    tempy=y-10*size
    draw_line(x,y,x+10*4*size,y-10*4*size,s,c)
    for j in range(3):
        draw_line(tempx,tempy,tempx+15*size,tempy,s,c)
        draw_line(tempx,tempy,tempx,tempy-15*size,s,c)
        tempx=tempx+10*size
        tempy=tempy-10*size
    tempx=x
    tempy=y-15*size
    draw_line(x,y,x,y-15*4*size,s,c)
    for j in range(3):
        draw_line(tempx,tempy,tempx-10*size,tempy-10*size,s,c)
        draw_line(tempx,tempy,tempx+10*size,tempy-10*size,s,c)
        tempy=tempy-15*size
    tempx=x-10*size
    tempy=y-10*size
    draw_line(x,y,x-10*4*size,y-10*4*size,s,c)
    for j in range(3):
        draw_line(tempx,tempy,tempx-15*size,tempy,s,c)
        draw_line(tempx,tempy,tempx,tempy-15*size,s,c)
        tempx=tempx-10*size
        tempy=tempy-10*size
    tempx=x-15*size
    tempy=y
    draw_line(x,y,x-15*4*size,y,s,c)
    for j in range(3):
        draw_line(tempx,tempy,tempx-10*size,tempy+10*size,s,c)
        draw_line(tempx,tempy,tempx-10*size,tempy-10*size,s,c)
        tempx=tempx-15*size
    tempx=x-10*size
    tempy=y+10*size
    draw_line(x,y,x-10*4*size,y+10*4*size,s,c)
    for j in range(3):
        draw_line(tempx,tempy,tempx-15*size,tempy,s,c)
        draw_line(tempx,tempy,tempx,tempy+15*size,s,c)
        tempx=tempx-10*size
        tempy=tempy+10*size

#for value in variable:
for i in range(3):
    for a in range(4):
        r=random.randint(0,6)
        if a==0:
            x=random.randint(0,250)
            y=random.randint(0,250)
        if a==1:
            x=random.randint(250,500)
            y=random.randint(0,250)
        if a==2:
            x=random.randint(0,250)
            y=random.randint(250,500)
        if a==3:
            x=random.randint(250,500)
            y=random.randint(250,500)
        if r==0:
            snow(0.75,x,y)
        if r==1:
            snow(1,x,y)
        if r==2:
            snow(1.25,x,y)
        if r==3:
            snow(0.75,x,y)
            snow(1,x,y)
        if r==4:
            snow(1,x,y)
            snow(1.25,x,y)
        if r==5:
            snow(1.25,x,y)
            snow(0.75,x,y)
        if r==6:
            snow(0.75,x,y)
            snow(1,x,y)
            snow(1.25,x,y)
display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
