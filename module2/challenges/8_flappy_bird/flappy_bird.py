from microbit import *
import random


# game constants
DELAY = 20                  # ms between each frame
FRAMES_PER_WALL_SHIFT = 20  # number of frames between each time a wall moves a pixel to the left
FRAMES_PER_NEW_WALL = 100   # number of frames between each new wall
FRAMES_PER_SCORE = 100      # number of frames between score rising by 1


# make an image that represent a pipe to dodge
def make_pipe():
    i = Image("00004:00004:00004:00004:00004")
    gap = random.randint(0, 3)  # random wall gap position
    i.set_pixel(4, gap, 0)      # blast a hole in the pipe
    i.set_pixel(4, gap + 1, 0)  # make hole bigger
    return i


# scroll welcome message and start countdown
display.scroll("READY")
for i in range(3, 0, -1):
    display.show(str(i))
    sleep(1e3)

display.clear()

# set position of bird
y = 50

# set rate of falling
speed = 0

# set initial score
score = 0

# number of frames
frame = 0

# create first pipe 
i = make_pipe()
          
while True:
    frame += 1

    # show pipe
    display.show(i)
    
    # flap if a button was pressed
    if button_a.was_pressed():
        speed = -8
    if button_b.was_pressed():
        display.scroll("Scr: " + str(score))
    
    # accelerate to terminal velocity
    speed += 1
    if speed > 2:
        speed = 2
        
    # move bird, but not off the edge
    y += speed
    if y > 99:
        y = 99
    elif y < 0:
        y = 0
    
    # draw bird
    led_y = int(y/20)
    display.set_pixel(1, led_y, 9)

    # check for collision
    if i.get_pixel(1, led_y) != 0:
        display.show(Image.SAD)
        sleep(500)
        display.scroll("Scr: " + str(score))
        break

    # move wall left
    if frame % FRAMES_PER_WALL_SHIFT == 0:
        i = i.shift_left(1)

    # create new wall
    if frame % FRAMES_PER_NEW_WALL == 0:
        i = make_pipe()

    # increase score
    if frame % FRAMES_PER_SCORE == 0:
        score += 1

    sleep(DELAY)