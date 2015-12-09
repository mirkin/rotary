#!/usr/bin/python

'''
Rotary enocoder COM-10982 uses 2bit grey code

00
10
11
01

'''
import RPi.GPIO as GPIO

class RotaryEncoder:

    states=[0,-1,1,0,1,0,0,-1,-1,0,0,1,0,1,-1,0]

    def __init__(self,PIN_1=5,PIN_2=13,PIN_PUSH=6,bounce=2,debug=False):
        '''
        PIN_1       --  GPIO pin connected to terminal 1
        PIN_2       --  GPIO pin connected to terminal 2
        PIN_PUSH    --  GPIO pin connected to push button
        bounce      --  value to use for debouncing the rotary encoder
        '''
        self.PINS=[PIN_1,PIN_2]
        self.PIN_PUSH=PIN_PUSH
        self.bounce=bounce
        self.prev_state=0
        self.value=0
        self.debug=debug
        self.push_callback=None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN_PUSH,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.PIN_PUSH,GPIO.BOTH,self.pushed,
                              bouncetime=self.bounce)

        for x in range(2):
            GPIO.setup(self.PINS[x],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(self.PINS[x],GPIO.BOTH,self.update_state,
                                  bouncetime=self.bounce)

    def pushed(self,channel):
        if self.debug:
            print('push '+str(GPIO.input(self.PIN_PUSH)))
        if self.push_callback is not None:
            self.push_callback(GPIO.input(self.PIN_PUSH))


    def update_state(self,channel):
        self.prev_state <<=2
        self.prev_state |=GPIO.input(self.PINS[0])<<1
        self.prev_state |=GPIO.input(self.PINS[1])
        self.prev_state &= 0x0f
        self.value+=RotaryEncoder.states[self.prev_state]
        if self.debug:
            print(self.value)

    def add_push_callback(self,callback):
        '''
        run callback when button is pressed
        callback will be called with 1 or 0 depending on press or release
        '''
        self.push_callback=callback
