import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)

def start_key_check(key):
#This function has a timer and can be looped
  key = False
  time.sleep(0.1)
  if GPIO.input(20):
    key = True
  else:
    key = False
  return key
