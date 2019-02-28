#!/usr/bin/python
import RPi.GPIO as GPIO
import time
#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel,GPIO.IN)
GPIO.setup(channel,GPIO.OUT)
 
def callback(channel):
        if GPIO.input(channel):
                print "Movement Detected!"
				
		GPIO.output(11,True)
		time.sleep(1)
		GPIO.cleanup()
        else:
                print "Movement Detected!"
		GPIO.output(11,True)
		time.sleep(1)
		GPIO.cleanup()
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)
