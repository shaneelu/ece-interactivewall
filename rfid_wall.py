import serial
import wiringpi2 as wiringpi

serial = serial.Serial("/dev/ttyAMA0", baudrate=9600)
  
from time import sleep  
# wiringpi.wiringPiSetupGpio()  
# wiringpi.pinMode(24, 1)  # sets GPIO 24 to output
# wiringpi.digitalWrite(24, 1) # sets port 24 to 1 (3V3, on)


code = ''
endtag= '590045F232DC'
movetag1= '590043419BC0'
movetag2 = '59004312DDD5'

while True:
    data = serial.read()
    if data == '\r':
        print(code)
        code = ''
    else:
        code = code + data
        if (len(code) == 11):
        	code = code[1:]
        	
	# resetReader()
		
		
def resetReader(){
	# wiringpi.digitalWrite(24, 0) # sets port 24 to 0 (0V, off)  #low
	sleep(10)                    # wait 10s  
	# wiringpi.digitalWrite(24, 1) # sets port 24 to 1 (3V3, on) #high
	sleep(10)                    # wait 10s  
}
