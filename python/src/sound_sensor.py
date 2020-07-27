import RPi.GPIO as GPIO
import sys
import time
import datetime

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

try:
  while True:
    if (GPIO.input(21) == True):
      print("Last valid input: " + str(datetime.datetime.now()))
      print("Detect Sound")
      time.sleep(3)
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
