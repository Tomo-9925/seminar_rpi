import RPi.GPIO as GPIO
import sys
import dht11
import time
import datetime
# import Adafruit_DHT

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=20)
result = instance.read()

try:
	while True:
	    result = instance.read()
	    if result.is_valid():
	        print("Last valid input: " + str(datetime.datetime.now()))
	        print("Temperature: %-3.1f C" % result.temperature)
	        print("Humidity: %-3.1f %%" % result.humidity)
	    time.sleep(6)
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

# Adafruit_DHTを使用する場合

# humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, '20')
# if humidity is not None and temperature is not None:
#     print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
# else:
#     print('Failed to get reading. Try again!')
#     sys.exit(1)
