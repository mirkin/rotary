#!/usr/bin/python
import RPi.GPIO as GPIO

class RGBLED(object):
    'Operate an RGP LED via GPIO'

    COMMON_ANODE='COMMON_ANODE'
    COMMON_CATHODE='COMMON_CATHODE'
    colors={
        'red':      0xFF0000,
        'green':    0x00FF00,
        'blue':     0x0000FF,
        'yellow':   0xFFFF00,
        'cyan':     0x00FFFF,
        'lilac':    0xFF00FF,
        'orange':   0xFF8C00,
        'pink':     0xFF1493,
    }

    def __init__(self,PIN_RED=7,PIN_GREEN=8,PIN_BLUE=25,type='COMMON_ANODE',
                 color=0x9933FF):
        '''
        PIN_RED     -- GPIO pin connected to red terminal
        PIN_GREEN   -- GPIO pin connected to green terminal
        PIN_BLUE    -- GPIO pin connected to blue terminal
        type        -- type of LED COMMON_ANODE or COMMON_CATHODE
        color       -- HEX value of RGB colour to start with
        '''
        self.PIN_RED=PIN_RED
        self.PIN_GREEN=PIN_GREEN
        self.PIN_BLUE=PIN_BLUE
        self.type=type
        self.gpio_setup()
        self.color=color

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

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,c):
        self.__color=c
        # get colour values in range 0-255
        self.__red=(c & 0xFF0000)>>16
        self.__green=(c & 0xFF00)>>8
        self.__blue=c & 0xFF
        # normalize to 0-100
        red=(self.__red/255.0)*100
        blue=(self.__blue/255.0)*100
        green=(self.__green/255.0)*100
        if self.type=='COMMON_ANODE':
            #lower means brighter
            red=100-red
            green=100-green
            blue=100-blue
        self.dimmer_red.ChangeDutyCycle(red)
        self.dimmer_green.ChangeDutyCycle(green)
        self.dimmer_blue.ChangeDutyCycle(blue)


    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, red):
        self.__red=red
        self.color((red<<16) | (self.__color & 0x00FFFF))
        #self.__color=(red<<16) | (self.__color & 0x00FFFF)

    def get_red(self):
        return (self.color & 0xFF0000)>>16

    def get_green(self):
        return (self.color & 0xFF00)>>8

    def get_blue(self):
        return (self.color & 0xFF)

