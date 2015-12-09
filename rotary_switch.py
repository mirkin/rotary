#!/usr/bin/python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 background=dark
'''
Rotary enocoder COM-10982 uses 2bit grey code

00
10
11
01

'''
import RPi.GPIO as GPIO
import time
import RGBLED
states=[0,-1,1,0,1,0,0,-1,-1,0,0,1,0,1,-1,0]
prev_state=0
PINS=[5,13]
PIN_PUSH=6
PIN_RED=7
PIN_GREEN=8
PIN_BLUE=25
bounce=2
GPIO.setmode(GPIO.BCM)
value=100

def alex(channel):
    global prev_state,states,value
    prev_state <<=2
    prev_state |=GPIO.input(PINS[0])<<1
    prev_state |=GPIO.input(PINS[1])
    prev_state &= 0x0f
    value+=states[prev_state]
    print(value)
    #print states[prev_state]
    #print(str(GPIO.input(PINS[0]))+''+str(GPIO.input(PINS[1])))
    #print "{0:b}".format(prev_state)

def pushed(channel):
    print('push '+str(GPIO.input(PIN_PUSH)))

for x in range(2):
    GPIO.setup(PINS[x],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(PINS[x],GPIO.BOTH,alex,bouncetime=bounce)

GPIO.setup(PIN_PUSH,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(PIN_PUSH,GPIO.BOTH,pushed,bouncetime=bounce)
GPIO.setup(PIN_RED,GPIO.OUT,initial=0)

my_led=RGBLED.RGBLED(7,8,25,'COMMON_ANODE',0xFF1493)
try:
    while True:
        time.sleep(0.01)
        my_led.set_color(0xFF0000)
        #pass
except KeyboardInterrupt:
    print('Cleaning Up')
    GPIO.cleanup()
