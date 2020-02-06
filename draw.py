from display import *
import math
def draw_line( x0, y0, x1, y1, screen, color ):
    slope=(y1-y0)/(x1-x0)
    if (slope>0 and slope <1):
        d=math.sqrt(5/4)
        while (x0 <= x1):
            plot(screen,color,x,y)
            if d >= 0:
                y0=y0+1
                d=d+-1*2*(x1-x0)
            x0=x0+1
            d=d+(y1-y0)
