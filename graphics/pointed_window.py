from graphics import *
from random import randint

def main():
    width = 640
    height = 480

    win = GraphWin("Exercise-02, Points", width, height)
    win.setBackground(color_rgb(0, 0, 0))

    # Draw 10,000 points in the window
    # Each of a random color and at a
    # random position.
    for i in range(10000):
        # Get random position

        x = randint(0, width)
        if x >= 0 and x <= width / 2:
            y = randint(0, height / 2)
        elif x >= width / 2 and x <=width:
            y = randint(height / 2, height)

        p = Point(x, y)

        # Get random color
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        p.setFill(color_rgb(r, g, b))
        p.draw(win)

    win.getMouse()
    win.close()

main()
