#!/usr/usr/bin/python
'''
Demo using the rotary encoder
'''
import RGBLED as LED
import RotaryEncoder as RE
import time


def cleanup():
    print 'Terminating'

def pushed(val):
    print('pushed: '+str(val))

my_rotary=RE.RotaryEncoder(5,13,6,2,True)
my_rotary.add_push_callback(pushed)
my_led=LED.RGBLED(7,8,25,'COMMON_ANODE',0xFF1493)


try:
    while True:
        time.sleep(0.01)
        pass
finally:
        cleanup()

