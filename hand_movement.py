import framebuf

from time import sleep
from gesture import Gesture #https://github.com/rafi021/Pycom-module-Example/blob/master/Grove%20Gesture%20Sensor/lib/gesture.py
import machine
from machine import Pin, I2C

import aiko.event as event
import aiko.oled as oled

i2c = machine.I2C(scl = machine.Pin(25), sda = machine.Pin(26))

try:
    g = Gesture(i2c)
except:
    g = Gesture(i2c)

value = 0

oled.initialise()
oled0 = oled.oleds[0]
oled1 = oled.oleds[1]

left_eye = [
    oled.load_image("images/left_l.pbm"),
    oled.load_image("images/left_m.pbm"),
    oled.load_image("images/left_r.pbm")
]

right_eye = [
    oled.load_image("images/right_l.pbm"),
    oled.load_image("images/right_m.pbm"),
    oled.load_image("images/right_r.pbm")
]

def eye_change():

    value = g.return_gesture()

    if value == 6:
        
        oled0.blit(left_eye[1], 0, 0)
        oled1.blit(right_eye[1], 0, 0)
        oled0.show()
        oled1.show()

        sleep(0.05)
        
        oled0.blit(left_eye[2], 0, 0)
        oled1.blit(right_eye[2], 0, 0)
        oled0.show()
        oled1.show()

    if value == 5:
        
        oled0.blit(left_eye[1], 0, 0)
        oled1.blit(right_eye[1], 0, 0)
        oled0.show()
        oled1.show()

        sleep(0.05)
        
        oled0.blit(left_eye[0], 0, 0)
        oled1.blit(right_eye[0], 0, 0)
        oled0.show()
        oled1.show()
    

def initialise():
    
    oled.oleds_clear(0)
    oled0.blit(left_eye[1], 0, 0)
    oled1.blit(right_eye[1], 0, 0)
    oled0.show()
    oled1.show()

    event.add_timer_handler(eye_change, 100)