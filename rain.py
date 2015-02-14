#!/usr/bin/env python

# Import the library functions we need
import time
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()

# Setup the LedBorg GPIO pins
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3
wiringpi.pinMode(PIN_RED, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_GREEN, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_BLUE, wiringpi.GPIO.OUTPUT)

# Set the colour channels (1 is on, 0 is off) and the time delay in seconds
red = 0
green = 0
blue = 1


# Set the LedBorg colour
wiringpi.digitalWrite(PIN_RED, red)
wiringpi.digitalWrite(PIN_GREEN, green)
wiringpi.digitalWrite(PIN_BLUE, blue)
print 'LedBorg on'
