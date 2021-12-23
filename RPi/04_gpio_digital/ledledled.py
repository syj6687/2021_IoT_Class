import RPi.GPIO as GPIO

LED_RED = 9
LED_YELLOW = 8
LED_GREEN = 7
SWITCH_1 = 21
SWITCH_2 = 22
SWITCH_3 = 23

GPIO.setmode(GPIO.BCM) # GPIO.BCM 핀번호 체계로 설정

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT) 
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(SWITCH_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
GPIO.setup(SWITCH_3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
# 내부 풀다운 저항 pull_up_down = GPIO.PUD_DOWN

try:
    while True:
        val1 = GPIO.input(SWITCH_1) 
        val2 = GPIO.input(SWITCH_2)
        val3 = GPIO.input(SWITCH_3)
        if val1 == 1: # val1 - switch1 값이 눌리면 Red LED on
            GPIO.output(LED_RED, val1) 
            print('RED LED ON')
        elif val2 == 1: # val2 - switch2 값이 눌리면 Yellow LED on
            GPIO.output(LED_YELLOW, val2)
            print('YELLOW LED ON')
        elif val3 == 1: # val3 - switch3 값이 눌리면 Green LED on
            GPIO.output(LED_GREEN, val3)
            print('GREEN LED ON')
        else:
            GPIO.output(LED_RED, 0) 
            GPIO.output(LED_YELLOW, 0) 
            GPIO.output(LED_GREEN, 0) 
            print('All LED OFF')
        
finally:
    GPIO.cleanup()
    print('cleanup and exit')
