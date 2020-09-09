from graphics import *
from random import randint
import sys

def main(width, height, n_points):

    win = GraphWin("Exercise-02, Points", width, height)
    win.setBackground(color_rgb(0, 0, 0))

    x1 = int(width / 4)
    x2 = int(3 * width / 4)

    y1 = int(height / 4)
    y2 = int(3 * height / 4)

    for i in range(n_points):

        # x = randint(x1, x2)
        # y = randint(y1, y2)

        x = randint(int(round((1 / 3) * width)), int(round((2 / 3) * width)))

        y = randint(int(round((1 / 3) * height)), int(round((2 / 3) * height)))

        p = Point(x, y)

        # Get random color
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        p.setFill(color_rgb(r, g, b))
        p.draw(win)

    win.getMouse()
    win.close()

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Uso: python center.py <width> <height> <n_points>')

    else:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        n_points = int(sys.argv[3])
        main(width, height, n_points)

    print('Bye!')