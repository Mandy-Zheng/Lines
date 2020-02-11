from display import *
import math
def draw_line( x0, y0, x1, y1, screen, color ):
    if(x0 >= x1):
        temp=int(x0)
        x0=int(x1)
        x1=temp
        temp=int(y0)
        y0=int(y1)
        y1=temp
    else:
        x0=int(x0)
        y0=int(y0)
        x1=int(x1)
        y1=int(y1)
    diffx=x1-x0
    diffy=y1-y0
    if (diffx == 0):
        if(y0 >= y1):
            temp=int(y0)
            y0=int(y1)
            y1=temp
        while(y0 <= y1):
            plot(screen,color,x0,y0)
            y0=y0+1
    else:
        slope=diffy/diffx
        if (slope>0 and slope <1):
            d=2*diffy-diffx
            while (y0 <= y1):
                plot(screen,color,x0,y0)
                if d >= 0:
                    y0=y0+1
                    d=d-2*diffx
                x0=x0+1
                d=d+2*diffy

        elif (slope>= 1):
            d=diffy-2*diffx
            while (y0 <= y1):
                plot(screen,color,x0,y0)
                if (d <= 0):
                    x0=x0+1
                    d=d+2*diffy
                y0=y0+1
                d=d-2*diffx

        elif (slope < 0 and slope >= -1):
            d=2*diffy+diffx
            while (y0 >= y1):
                plot(screen,color,x0,y0)
                if d >= 0:
                    y0=y0-1
                    d=d-2*diffx
                x0=x0+1
                d=d-2*diffy
        elif (slope < -1):
            d=diffy+2*diffx
            while (y0 >= y1):
                plot(screen,color,x0,y0)
                if d <= 0:
                    x0=x0+1
                    d=d-2*diffy
                y0=y0-1
                d=d-2*diffx
        else:
            while(x0 <= x1):
                plot(screen,color,x0,y0)
                x0=x0+1
