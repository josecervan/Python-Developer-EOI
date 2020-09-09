from graphics import *
from math import cos, sin, sqrt
from random import randint

def horzLine(x1, y1, x2, color, win):
    for x in range(x1, x2):
        p = Point(x, y1)
        p.setFill(color)
        p.draw(win)

def vertLine(x, y1, y2, color, win):
    for y in range(y1, y2):
        p = Point(x,y)
        p.setFill(color)
        p.draw(win)

def circle(cx, cy, r, color, win):
    # loop over 360 degree arc plotting pixels
    for i in range(0, 1000):
        x = cos(i) * r + cx
        y = sin(i) * r + cy

        p = Point(x, y)
        p.setFill(color)
        p.draw(win)
        
def square(cx, cy, r, color, win):
    # left side
    vertLine(cx - r, cy - r, cy + r, color, win)

    # top side
    horzLine(cx - r,  cy - r, cx + r, color, win)

    # bottom side
    horzLine(cx - r, cy + r, cx + r, color, win)

    # right side
    vertLine(cx + r, cy - r, cy + r, color, win)

def montecarlo(n_shots, width, height, radio, win):

    cx = int(width / 2)
    cy = int(height / 2)

    on_target = 0

    for shot in range(n_shots):

        x = randint(cx - radio, cx + radio)
        y = randint(cy - radio, cy + radio)

        p = Point(x, y)

        if isOnTarget(x, y, cx, cy, radio):
            on_target += 1
            p.setFill(color_rgb(0, 200, 0))
        else:
            p.setFill(color_rgb(255, 0, 0))

        p.draw(win)

    return on_target

def isOnTarget(x, y, cx, cy, r):
    return dist(x, y, cx, cy) <= r

def dist(x1, y1, x2, y2):
    return sqrt(((x2-x1)**2) + ((y2 - y1)**2))

def show_msg(p, msg, style, font, win):

    t = Text(p, msg)
    t.setTextColor(color_rgb(0, 0, 0))
    t.setSize(font)
    t.setStyle(style)
    t.setFace('courier')
    t.draw(win)
