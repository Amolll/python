import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
TRIG=4
ECHO=18
LED=21
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def red_light():
	for x in range(5):             # Loop will run only five times
		GPIO.output(LED, GPIO.HIGH) # Turn LED ON
					#print ('LED ON')
		time.sleep(0.1)          # Delay of 1 sec
		GPIO.output(LED, GPIO.LOW) # Turn LED OFF
					#print('LED OFF')
		time.sleep(0.1)

def get_distance():
	GPIO.output(TRIG,True)
	time.sleep(0.0001)
	GPIO.output(TRIG,False)
	while GPIO.input(ECHO)==False:
		start=time.time()
	while GPIO.input(ECHO)==True:
		end=time.time()
	sig_time = end - start
	
	#cm
	distance=sig_time/0.000058
	print('distance: {}cm'. format(distance))
	return distance

while True:
	
	distance1=get_distance()
	time.sleep(0.05)
		
	if distance1<30:
		red_light()
			
	elif distance1>30:
		red_light()
		
	


