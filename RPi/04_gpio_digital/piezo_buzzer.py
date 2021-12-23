import RPi.GPIO as GPIO
import time

BUZZER_PIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)


try:
    
        pwm.ChangeFrequency(100)
        time.sleep(0.5)
finally:
    pwm.stop()
GPIO.cleanup()