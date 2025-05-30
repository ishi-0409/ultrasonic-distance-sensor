import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
import ADC0834
pwmpin=4
ADC0834.setup()
GPIO.setup(pwmpin,GPIO.OUT)
pwm=GPIO.PWM(pwmpin,50)
pwm.start(0)
try:
    while True:
        X=ADC0834.getResult(0)
        print('Xvalue',X)
        pwmvalue=10/255*(X)+2
        print(pwmvalue)
        pwm.ChangeDutyCycle(pwmvalue)
        sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
