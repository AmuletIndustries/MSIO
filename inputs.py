import RPi.GPIO
import Adafruit_GPIO as GPIO
import time

# GPIO.setmode(GPIO.BOARD)
gpio = GPIO.get_platform_gpio()

gpio.setup(20, GPIO.IN)
gpio.setup(21, GPIO.IN)
gpio.setup(26, GPIO.IN)
gpio.setup(16, GPIO.IN)


def start_key_check(key):
    # This function has a timer and is looped
    time.sleep(0.5)
    if gpio.input(20):
        key = True
    else:
        key = False

    return key


def red_switch(redSwitch):
    # This function has a timer and is looped
    # WARNING the timer of this function is short!
    time.sleep(0.05)
    if gpio.input(21):
        redSwitch = True
        print("redSwitch set to True")

    return redSwitch


def green_switch(greenSwitch):
    # This function has a timer and is looped
    # WARNING the timer of this function is short!
    time.sleep(0.05)
    if gpio.input(26):
        greenSwitch = True
        print("greenSwitch set to True")

    return greenSwitch


def blue_switch(blueSwitch):
    # This function has a timer and is looped
    # WARNING the timer of this function is short!
    time.sleep(0.05)
    if GPIO.input(16):
        blueSwitch = True
        print("blueSwitch set to True")

    return blueSwitch
