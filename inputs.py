import RPi.GPIO as GPIO
import time
import settings

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)

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
