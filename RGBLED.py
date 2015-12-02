#!/usr/bin/python
import RPi.GPIO as GPIO

class RGBLED:
    'Operate an RGP LED via GPIO'

    COMMON_ANODE='COMMON_ANODE'
    COMMON_CATHODE='COMMON_CATHODE'

    def __init__(self,PIN_RED=7,PIN_GREEN=8,PIN_BLUE=25,type='COMMON_ANODE',color=0x9933FF):
        self.PIN_RED=PIN_RED
        self.PIN_GREEN=PIN_GREEN
        self.PIN_BLUE=PIN_BLUE
        self.type=type
        self.color=color
        self.gpio_setup()
        self.set_color(self.color)

    def gpio_setup(self):
        GPIO.setmode(GPIO.BCM)
        #set RGB pins as outputs
        GPIO.setup(self.PIN_RED,GPIO.OUT)
        GPIO.setup(self.PIN_GREEN,GPIO.OUT)
        GPIO.setup(self.PIN_BLUE,GPIO.OUT)
        #pulse width modulation frequency
        self.dimmer_red=GPIO.PWM(self.PIN_RED,50)
        self.dimmer_blue=GPIO.PWM(self.PIN_BLUE,50)
        self.dimmer_green=GPIO.PWM(self.PIN_GREEN,50)
        self.dimmer_red.start(50)
        self.dimmer_green.start(50)
        self.dimmer_blue.start(50)

    def set_color(self,c):
        self.color=c
        # get colour values in range 0-255
        red=(c & 0xFF0000)>>16
        green=(c & 0xFF00)>>8
        blue=c & 0xFF
        # normalize to 0-100
        red=(red/255.0)*100
        blue=(blue/255.0)*100
        green=(green/255.0)*100
        if self.type=='COMMON_ANODE':
            #lower means brighter
            red=100-red
            green=100-green
            blue=100-blue
        self.dimmer_red.ChangeDutyCycle(red)
        self.dimmer_green.ChangeDutyCycle(green)
        self.dimmer_blue.ChangeDutyCycle(blue)
