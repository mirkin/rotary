#!/usr/usr/bin/python
'''
Demo using the rotary encoder
'''

my_rotary=rotary_switch()

def cleanup():
          print 'Terminating'
          my_rotary.cleanup()

try:
    while True:
        pass
finally:
        cleanup()

