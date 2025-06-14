import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
tri=23
echo=24
GPIO.setup(tri,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
try:
    while True:    
        GPIO.output(tri,0)
        time.sleep(2E-6)
        GPIO.output(tri,1)
        time.sleep(10E-6)
        GPIO.output(tri,0)
        while GPIO.input(echo)==0:
            pass
        echostart=time.time()
        while GPIO.input(echo)==1:
            pass
        echostop=time.time()
        travel=echostop-echostart
        distance=1224*travel*3600/1000*4
        print(round(distance,1),'cm') 
        time.sleep(.2)
except KeyboardInterrupt():
    GPIO.cleanup()




