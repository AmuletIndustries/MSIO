import RPi.GPIO
import Adafruit_GPIO as GPIO
import settings

gpio = GPIO.get_platform_gpio()
gpio.setup(25, GPIO.OUT)  # Color RED out
gpio.setup(24, GPIO.OUT)  # Color GREEN out
gpio.setup(23, GPIO.OUT)  # Color BLUE out


def light_red_on(key):
    if key:
        gpio.output(25, True)
        print("RED light set to 100%")
    else:
        print("red_light_on was called but KEY is not on")


def light_red_off(key):
    if key:
        gpio.output(25, False)
        print("RED light set to 0%")
    else:
        print("red_light_off was called but KEY is not on")


def light_green_on(key):
    if key:
        gpio.output(24, True)
        print("GREEN light set to 100%")
    else:
        print("green_light_on was called but KEY is not on")


def light_green_off(key):
    if key:
        gpio.output(24, False)
        print("GREEN light set to 0%")
    else:
        print("green_light_off was called but KEY is not on")


def light_blue_on(key):
    if key:
        gpio.output(23, True)
        print("BLUE light set to 100%")
    else:
        print("blue_light_on was called but KEY is not on")


def light_blue_off(key):
    if key:
        gpio.output(23, False)
        print("BLUE light set to 0%")
    else:
        print("blue_light_off was called but KEY is not on")
