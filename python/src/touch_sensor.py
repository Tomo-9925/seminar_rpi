import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
	while True:
    if (GPIO.input(16) == True):
      print("touch")
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
