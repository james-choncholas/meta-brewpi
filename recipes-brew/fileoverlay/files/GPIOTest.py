import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

i = 0;

while i < 20:
    GPIO.setup(35, GPIO.OUT)
    GPIO.output(35, True)
    time.sleep(2)
    GPIO.output(35, False)
    time.sleep(2)
    i = i + 1
