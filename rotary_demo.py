#!/usr/usr/bin/python
'''
Demo using the rotary encoder
'''
import RGBLED as LED
import RotaryEncoder as RE
import time
import random

def cleanup():
    print 'Terminating'

def pushed(val):
    print('pushed: '+str(val))
    if val==1:
        cols=my_led.colors.values()
        col=random.choice(cols)
        my_led.color=col

def value_changed(val):
    print('Value changed: '+str(val))

my_rotary=RE.RotaryEncoder(5,13,6,2,False)
my_rotary.add_push_callback(pushed)
my_rotary.add_value_listener(value_changed)
my_led=LED.RGBLED(7,8,25,'COMMON_ANODE',0xFF1493)


try:
    while True:
        time.sleep(0.01)
        pass
finally:
        cleanup()

