import RPi.GPIO as GPIO
import time
import settings

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(16, GPIO.IN)

def start_key_check(key):
#This function has a timer and is looped
    time.sleep(0.5)
    if GPIO.input(20):
        key = True
    else:
        key = False

    return key

def red_switch(redSwitch):
#This function has a timer and is looped
#WARNING the timer of this function is short!
    time.sleep(0.05)
    if GPIO.input(21):
        redSwitch = True
        print "redSwitch set to True"

    return redSwitch
def green_switch(greenSwitch):
#This function has a timer and is looped
#WARNING the timer of this function is short!
    time.sleep(0.05)
    if GPIO.input(26):
        redSwitch = True
        print "greenSwitch set to True"

    return greenSwitch

def red_switch(blueSwitch):
#This function has a timer and is looped
#WARNING the timer of this function is short!
    time.sleep(0.05)
    if GPIO.input(16):
        blueSwitch = True
        print "blueSwitch set to True"

    return blueSwitch
