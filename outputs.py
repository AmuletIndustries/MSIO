import RPi.GPIO
import Adafruit_GPIO as GPIO

gpio = GPIO.get_platform_gpio()
gpio.setup(25, GPIO.OUT)  # Color RED output


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
