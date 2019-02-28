#!/usr/bin/python
import RPi.GPIO as GPIO
import time
#import sleep
 
#GPIO SETUP
channel = 17
led_pin = 21   
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)
#GPIO.setup(channel, GPIO.IN
 
def callback(channel):

	if GPIO.input(channel):
		print "Please check Your Bike..."
	else:
		print "Someone is trying to break the bike HandleLock" 
		for x in range(10):             # Loop will run only five times
			GPIO.output(led_pin, GPIO.HIGH) # Turn LED ON
			time.sleep(0.1) 		# Delay of 1 sec
			GPIO.output(led_pin, GPIO.LOW)  # Turn LED OFF
			time.sleep(0.2)                 # Delay of 1 sec
#GPIO.cleanup()
				
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)

