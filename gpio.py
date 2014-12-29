import RPi.GPIO as GPIO
import time

# !!! Warning: Please read the manual because the GPIO pins are very sensitive and you can easily destroy your Raspberry !!!

GPIO.setmode(GPIO.BCM)  # for GPIO numbers or GPIO.BOARD if you like to count pins
GPIO.setup(23, GPIO.IN, pull_up_down=PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=PUD_UP)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)

while True:
    if GPIO.input(23):
        print "GPIO 23 == high"
        GPIO.output(25, GPIO.LOW)
    if GPIO.input(24):
        print "GPIO 24 == high"
        GPIO.output(25, GPIO.HIGH)
    time.sleep(1)               # wait 1 second 

# at the end you should clean up
#GPIO.cleanup()

# there are good tutorials with interrupts, just look for GPIO.add_event_detect