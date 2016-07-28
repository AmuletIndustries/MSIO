import RPi.GPIO
import Adafruit_GPIO as GPIO
import time

# GPIO.setmode(GPIO.BOARD)
gpio = GPIO.get_platform_gpio()

gpio.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def loop():
    while True:
        time.sleep(0.05)
        if gpio.input(19):
            print("ON")
        else:
            print("OFF")


loop()
