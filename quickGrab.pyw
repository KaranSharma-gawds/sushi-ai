from PIL import ImageGrab
import os
import time

# Globals
x_pad = 341
y_pad = 272

def screen_grab():
    box = (x_pad, y_pad, x_pad+700, y_pad+600)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

if __name__ == '__main__':
    screen_grab()
    # pass
# 341x272(start)
# 1140x871(end)