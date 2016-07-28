import RPi.GPIO
import Adafruit_GPIO as GPIO
import time

# GPIO.setmode(GPIO.BOARD)
gpio = GPIO.get_platform_gpio()

gpio.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
gpio.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
gpio.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
gpio.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def start_key_check():
    # This function has a timer and is looped
    time.sleep(0.05)
    if gpio.input(20):
        print("Key is ON")
        global key
        key = True
    else:
        global key
        key = False
        print("Key is OFF")


def red_switch():
    # This function has a timer and is looped
    # WARNING the timer of this function is short!
    time.sleep(0.05)
    if gpio.input(19):
        global redSwitch
        redSwitch = True
        print("redSwitch set to True")
        return True
    else:
        print("redSwitch set to False")
        return False


def green_switch():
    # This function has a timer and is looped
    # WARNING the timer of this function is short!
    time.sleep(0.05)
    if gpio.input(26):
        global greenSwitch
        greenSwitch = True
        print("greenSwitch set to True")
        return True
    else:
        print("greenSwitch set to False")
        return False


def blue_switch():
    # This function has a timer and is looped
    # WARNING the timer of this function is short!
    time.sleep(0.05)
    if gpio.input(16):
        global blueSwitch
        blueSwitch = True
        print("blueSwitch set to True")
        return True
    else:
        print("blueSwitch set to False")
        return False
