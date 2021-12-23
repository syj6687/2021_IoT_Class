import RPi.GPIO as GPIO
import time
#               A B C D E F G
SEGMENT_PINS = [2,3,4,5,6,7,8]
DIGIT_PINS = [10,11,12,13]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

data = [  #디스플레이 설정                         
    [0,1,1,0,0,0,0,0],#1
    [1,1,0,1,1,0,1,0],#2
    [1,1,1,1,0,0,1,0],#3
    [0,1,1,0,0,1,1,0],#4
    [1,0,1,1,0,1,1,0],#5
    [1,0,1,1,1,1,1,0],#6
    [1,1,1,0,0,0,0,0],#7
    [1,1,1,1,1,1,1,0],#8
    [1,1,1,0,0,1,1,0],#9
    [1,1,1,1,1,1,0,0] #0
]

def display(digit,number):
    #해당 자릿수 핀만 LOW
    for i in range(len(DIGIT_PINS)):
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW) # 0~6
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)

    for i in range(len(SEGMENT_PINS)):  #0~6
        GPIO.output(SEGMENT_PINS[i], data[number][i])
    time.sleep(0.001)
def show(a,b,c,d):
    display(1,a)
    display(2,b)
    display(3,c)
    display(4,d)

try:
    while True:
        show(2,0,2,1)

finally:
    GPIO.cleanup()
    print("clenup and exit")