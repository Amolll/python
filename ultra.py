import RPi.GPIO as GPIO
import time

try:
	GPIO.setmode(GPIO.BOARD)
	PIN_TRIGGER=7 #choose any
	PIN_ECHO=11  #choose any
	GPIO.setup(PIN_TRIGGER, GPIO.OUT)
	GPIO.setup(PIN_ECHO, GPIO.IN)
	GPIO.output(PIN_TRIGGER, GPIO.LOW)
	#GPIO.output(PIN_ECHO, GPIO.LOW)
	print("Waiting for sensor to settle..")
	time.sleep(2)
	i=0
	while i<1:
		print("Calculating distance")
		GPIO.output(PIN_TRIGGER, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(PIN_TRIGGER, GPIO.LOW)
		

		while GPIO.input(PIN_ECHO)==0:
			pulse_start_time=time.time()
		while GPIO.input(PIN_ECHO)==1:
			pulse_end_time=time.time()

		pulse_duration=pulse_end_time - pulse_start_time
		distance=round(pulse_duration*17150, 2)
		print("Distance:",distance/100, "n")
		i=i+1
finally:
	GPIO.cleanup()



