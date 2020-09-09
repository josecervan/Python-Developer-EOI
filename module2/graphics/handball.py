#!/usr/bin/env python3

"""
Prog:   ex-12_01.py

Auth:   R. Morgan

Desc:   Demonstrate how to use John Zelle's
        graphics.py library to do simple
        animation of a pendulum.

Lic:    This code is placed in the public domain.

"""

from graphics import *
from math import *

width = 640
height = 480


class Paddle():
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.w = 10
        self.h = 50
        self.win = win
        self.rect = Rectangle(Point(self.x, self.y), Point(self.x + self.w, self.y + self.h))
        self.rect.setFill('white')

    def getX(self):
        return self.rect.p1.getX()

    def getY(self):
        return self.rect.p1.getY()

    def getW(self):
        return self.w

    def getH(self):
        return self.h

    def move(self, xspeed, yspeed):
        self.rect.move(xspeed, yspeed)

    def draw(self):
        self.rect.draw(self.win)

    def undraw(self):
        self.rect.undraw()


class Ball():
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.xspeed = 3
        self.yspeed = 1
        self.r = 10
        self.win = win
        self.cir = Circle(Point(self.x, self.y), self.r)
        self.cir.setFill('white')

    def set_speed(self, xspeed, yspeed):
        self.xspeed = xspeed
        self.yspeed = yspeed

    def move(self):
        self.cir.move(self.xspeed, self.yspeed)
        p1 = self.cir.getP1()
        self.x = p1.getX()
        self.y = p1.getY()

    def draw(self):
        self.cir.draw(self.win)

    def undraw(self):
        self.cir.undraw()

    def check_collision(self, pad):
        print("Xspeed: ", self.xspeed, "Yspeed: ", self.yspeed)
        xbound = self.within_x_bounds(pad)
        ybound = self.within_y_bounds(pad)

        if xbound and ybound:
            if xbound:
                self.xspeed = -self.xspeed
            if ybound:
                self.yspeed = -self.yspeed
            self.move()
            return True

        return False

    def within_x_bounds(self, pad):
        if self.xspeed < 0:
            if (self.x < pad.getX() + pad.getW()) and (self.x > pad.getX()):
                return True
            else:
                return False
        else:
            if (self.x + self.r >= pad.getX()) and (self.x <= pad.getX() + pad.getW()):
                return True
            else:
                return False

    def within_y_bounds(self, pad):
        if self.y + self.r >= pad.getY() and self.y <= pad.getY() + pad.getH():
            return True
        else:
            return False

    def check_edges(self, width, height):
        p1 = self.cir.getP1()
        if p1.getX() < 0 or p1.getX() + self.r > width:
            self.xspeed = -self.xspeed;
        if p1.getY() < 0 or p1.getY() + self.r > height:
            self.yspeed = -self.yspeed;


def main():
    win = GraphWin("Handball", width, height)
    win.setBackground('black')

    xspeed = 0.1
    yspeed = 0.1

    # initial placement of paddle
    pad = Paddle(10, (height / 2) - 25, win)
    # Draw paddles.
    pad.draw()

    ball = Ball(width / 2, height / 2, win)
    ball.set_speed(xspeed, yspeed)
    ball.draw()

    while 1:
        # get imput if any
        k = win.checkKey()
        if k == 'a':
            if pad.getY() < 0:
                pad.move(0, 0)
            else:
                pad.move(0, -20)
            print('Pad1: Move Up', pad.getX(), pad.getY())

        if k == 'z':
            if pad.getY() > height - 50:
                pad.move(0, 0)
            else:
                pad.move(0, 20)
            print('Pad1: Move down', pad.getX(), pad.getY())

        ball.check_edges(width, height)
        ball.move()

        if ball.check_collision(pad):
            print("Ball hit paddle")

    win.getMouse()
    win.close()


main()