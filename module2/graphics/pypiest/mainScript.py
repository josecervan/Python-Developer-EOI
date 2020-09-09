from pypiest import *
from graphics import *
from math import pi

if __name__ == '__main__':

    WIDTH = 800
    HEIGHT = 600

    cx = WIDTH / 2
    cy = HEIGHT / 2

    win = GraphWin("Let's get the value of Pi!", WIDTH, HEIGHT)
    win.setBackground(color_rgb(245, 245, 245))

    show_msg(Point(cx, int(75/2)), 'Welcome to PyPiEst Montecarlo!', 'bold', 25, win)
    show_msg(Point(700, 580), 'Version  1.0.0', 'normal', 10, win)

    horzLine(0, 75, WIDTH, color_rgb(0, 0, 0), win)
    horzLine(0, 525, WIDTH, color_rgb(0, 0, 0), win)

    RADIO = 200
    circle(int(WIDTH / 2), int(HEIGHT / 2), RADIO, color_rgb(0, 0, 0), win)
    square(int(WIDTH / 2), int(HEIGHT / 2), RADIO, color_rgb(0, 0, 0), win)

    N_SHOTS = int(5)
    show_msg(Point(100, 200), 'Number\nof\nshots\n\n' + str(N_SHOTS), 'normal', 15, win)
    on_target = montecarlo(N_SHOTS, WIDTH, HEIGHT, RADIO, win)

    est_pi = 4 * on_target / N_SHOTS

    show_msg(Point(230, 550), 'Pi = ' + str(pi), 'normal', 20, win)
    show_msg(Point(230, 580), 'PyPiEst = ' + str(est_pi), 'normal', 20, win)

    win.getMouse()
    win.close()
