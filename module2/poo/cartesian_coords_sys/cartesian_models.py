from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            raise TypeError

    def __str__(self):
        return f'({self.x}, {self.y})'

    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return 'quadrant 1'
        if self.x < 0 and self.y > 0:
            return 'quadrant 2'
        if self.x < 0 and self.y < 0:
            return 'quadrant 3'
        if self.x > 0 and self.y < 0:
            return 'quadrant 4'
        if self.x == 0 and self.y == 0:
            return 'coordinate origin'
        if self.x == 0:
            return 'y axis'
        if self.y == 0:
            return 'x axis'

    def vector(self, p):
        return self.x - p.x, self.y - p.y

    def distance(self, p):
        return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)


class Rectangle:
    def __init__(self, init=Point(), final=Point()):
        self.init = init
        self.final = final

    def base(self):
        return abs(self.init.vector(self.final)[0])

    def height(self):
        return abs(self.init.vector(self.final)[1])

    def area(self):
        return self.base() * self.height()
