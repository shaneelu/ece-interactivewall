int top_scan_pin
int bottom_scan_pin

GPIO.setup(top_scan_pin, GPIO.INPUT)
GPIO.setup(bottom_scan_pin, GPIO.INPUT)

def stop():
    print('stopping the scanner when it reaches the bottom')
    GPIO.output(enablePin1, GPIO.HIGH)

GPIO.add_event_detect(bottom_scan_pin, GPIO.RISING, callback=stop)
GPIO.add_event_detect(top_scan_pin, GPIO.RISING, callback=stop)

def reset():

