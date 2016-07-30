import RPi.GPIO
import Adafruit_GPIO as GPIO
import settings
import time

gpio = GPIO.get_platform_gpio()
gpio.setup(25, GPIO.OUT)  # Color RED out
gpio.setup(24, GPIO.OUT)  # Color GREEN out
gpio.setup(23, GPIO.OUT)  # Color BLUE out


def light_red_on(key):
    if key:
        gpio.output(25, True)
        print("RED light set to 100%")
        red_on_loop()
    else:
        print("red_light_on was called but KEY is not on")


def light_red_off():
    gpio.output(25, False)
    print("RED light set to 0%")


def light_green_on(key):
    if key:
        gpio.output(24, True)
        print("GREEN light set to 100%")
        green_on_loop()
    else:
        print("green_light_on was called but KEY is not on")


def light_green_off():
    gpio.output(24, False)
    print("GREEN light set to 0%")


def light_blue_on(key):
    if key:
        gpio.output(23, True)
        print("BLUE light set to 100%")
        blue_on_loop()
    else:
        print("blue_light_on was called but KEY is not on")


def light_blue_off():
    gpio.output(23, False)
    print("BLUE light set to 0%")


def red_on_loop():
    print("RED ON loop started")
    for x in range(1, 60):
        x += 1
        time.sleep(0.1)
    light_red_off()


def green_on_loop():
    print("GREEN ON loop started")
    for x in range(1, 60):
        x += 1
        time.sleep(0.1)
    light_green_off()


def blue_on_loop():
    print("BLUE ON loop started")
    for x in range(1, 60):
        x += 1
        time.sleep(0.1)
    light_blue_off()
