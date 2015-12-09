#!/usr/usr/bin/python
'''
Demo using the rotary encoder
'''
import RGBLED as LED
import RotaryEncoder as RE
import time

my_rotary=RE.RotaryEncoder(5,13,6,2,True)
my_led=LED.RGBLED(7,8,25,'COMMON_ANODE',0xFF1493)

def cleanup():
          print 'Terminating'

try:
    while True:
        time.sleep(0.01)
        pass
finally:
        cleanup()

