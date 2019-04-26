import RPi.GPIO as GPIO  
import time  
import signal  
import atexit  

class Speed():
	SLOW = 1
	FAST = 2
	STOP = 0

def stop():
	right_servo.ChangeDutyCycle(6)
	left_servo.ChangeDutyCycle(6)
	

def rotate_left():
	print "rotate left"
	left_servo.ChangeDutyCycle(6)
	right_servo.ChangeDutyCycle(5.4)
	
def rotate_right():
	print "rotate right"
	right_servo.ChangeDutyCycle(6)
	left_servo.ChangeDutyCycle(6.6)
	
def forward(speed):
	if speed == Speed.SLOW :
		print "slow fwd"
		right_servo.ChangeDutyCycle(5.4)
		left_servo.ChangeDutyCycle(6.6)
	elif speed == Speed.FAST :
		print "fast pwd back"
		right_servo.ChangeDutyCycle(20)
		left_servo.ChangeDutyCycle(1)
	else :
		print "stop"
		right_servo.ChangeDutyCycle(6)
		left_servo.ChangeDutyCycle(6)
	
def back(speed):
	if speed == Speed.SLOW :
		print "slow back"
		right_servo.ChangeDutyCycle(6.8)
		left_servo.ChangeDutyCycle(5.4)
	elif speed == Speed.FAST :
		print "fast back"
		right_servo.ChangeDutyCycle(20)
		left_servo.ChangeDutyCycle(1)
	else :
		print "stop"
		right_servo.ChangeDutyCycle(6)
		left_servo.ChangeDutyCycle(6)

	
atexit.register(GPIO.cleanup)
left_servo_pin = 8
right_servo_pin = 7

GPIO.setmode(GPIO.BCM)  
GPIO.setup(left_servo_pin, GPIO.OUT, initial=False)
GPIO.setup(right_servo_pin, GPIO.OUT, initial=False)
left_servo = GPIO.PWM(left_servo_pin,50) #50HZ  
left_servo.start(0) 
right_servo = GPIO.PWM(right_servo_pin,50) #50HZ  
right_servo.start(0) 
time.sleep(2)  

while (True):
#	back(Speed.SLOW)
#	time.sleep(5)
#	forward(Speed.SLOW)
#	time.sleep(5)
#	back(Speed.FAST)
#	time.sleep(5)
#	forward(Speed.FAST)
#	time.sleep(5)
	rotate_left()
	time.sleep(3)
	rotate_right()
	time.sleep(3)
	stop()
	time.sleep(3)


#while(True): 
#	for i in range(0,180):
#		print i
#		DC=1./18.*(i)+2
#		print DC
#		p1.ChangeDutyCycle(7)
#		print DC
#		p2.ChangeDutyCycle(2)
#		time.sleep(.25)
#	for i in range(180,0,-1):
#		DC=1./18.*(i)+2
#		print DC
#		p1.ChangeDutyCycle(DC)
#		print DC
#		p2.ChangeDutyCycle(DC)
#		time.sleep(.25)
#	print "next"


