__author__ = 'pi'
#This file exposes various LED control functions

import time
import RPi.GPIO as GPIO
import time

#This sets up devices that need to be high on boot.
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(15, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(33, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(35, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(37, GPIO.OUT, initial=GPIO.HIGH)

#this sets up devices that need to be low on boot
def setup2():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

def showColor(color):
    if color == "gold":
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, False)
        return
    elif color == "red":
        GPIO.output(11, True)
        GPIO.output(13, False)
        GPIO.output(15, False)
        return
    else:
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        return

def activatePins(pinArray):
    for pin in pinArray:
        #Making False = OFF, True = ON
        GPIO.output(pin, False)
        print "Set " + str(pin) + " to On. \n"

        time.sleep(3)

        #Then set all pins back to false.
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, True)
        GPIO.output(33, True)
        GPIO.output(35, True)
        GPIO.output(37, True)

def activatePinsTimer(pinArray, seconds):
    for pin in pinArray:
        GPIO.output(pin, True)
        print "Set " + str(pin) + " to On. \n"

    time.sleep(seconds)

    for pin in pinArray:
        GPIO.output(pin, False)
        print "Set " + str(pin) + " to Off. \n"

def on(pinArray):
    for pin in pinArray:
        GPIO.output(pin, True)
        print "Set " + str(pin) + " to On. \n"

def off(pinArray):
    for pin in pinArray:
        GPIO.output(pin, False)
        print "Set " + str(pin) + " to Off. \n"

def cleanup():
    GPIO.cleanup()
