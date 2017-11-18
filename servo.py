import RPi.GPIO as GPIO # always needed with RPi.GPIO  
from time import sleep  # pull in the sleep function from time module  
  
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  
  
GPIO.setup(18, GPIO.OUT)# set GPIO 18 as output for white led  

  
motor = GPIO.PWM(18, 100)    # create object white for PWM on port 25 at 100 Hertz   
speed = 10
motor.start(speed)              # start white led on 0 percent duty cycle (off)  

  
# now the fun starts, we'll vary the duty cycle to   
# dim/brighten the leds, so one is bright while the other is dim  
  
pause_time = 1           # you can change this to slow down/speed up  
  
while True:
        speed = speed - 1
	motor.ChangeDutyCycle(speed)
	sleep(pause_time)
