import RPi.GPIO as GPIO
import time
import settings

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)

def start_key_check(key):
#This function has a timer and can be looped
    keyChange = 0
    time.sleep(0.1)
    if GPIO.input(20):
        key = True
        keyChange = 1
    else:
        key = False
        keyChange = 1

    while keyChange == 1:
        print "Start Key has changed possition."
        keyChange = 0

    return key
