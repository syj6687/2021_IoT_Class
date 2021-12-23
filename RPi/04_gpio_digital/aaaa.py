import RPi.GPIO as GPIO
import time

BUZZER = 7 #gpio 설정들
TRIG = 21
ECHO = 20
LED_GREEN=2
LED_YELLOW=3
LED_RED=4



segments = (10,11,12,13,14,15,16,17) #세그먼트 핀 설정


GPIO.setmode(GPIO.BCM) # GPIO.BCM 핀번호 체계로 설정
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT) 
GPIO.setup(LED_GREEN, GPIO.OUT)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

pwm = GPIO.PWM(BUZZER, 1)  #부저 설정 1은 초기값
pwm.start(20)
num = [  #디스플레이 설정                         

    
    [0,1,1,0,0,0,0,1],#1
    [1,1,0,1,1,0,1,1],#2
    [1,1,1,1,0,0,1,1],#3
    [0,1,1,0,0,1,1,1],#4
    [1,0,1,1,0,1,1,1],#5
    [1,0,1,1,1,1,1,1],#6
    [1,1,1,0,0,0,0,1],#7
    [1,1,1,1,1,1,1,1],#8
    [1,1,1,0,0,1,1,1], #9
    [0,0,0,0,0,0,0,0] #거리가 27cm이상일때 전부 꺼짐

]


try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False) # 초음파 발사

        while GPIO.input(ECHO)==0:
            pass
        start = time.time()




        while GPIO.input(ECHO) == 1:
            pass
        stop = time.time()

        duration_time = stop - start
        distance = duration_time * 17160 # 초음파 돌아오는시간 곱하기 17160해서 거리를 구함

        print('Distance : %.1fcm' % distance) # 거리 출력



        if distance <= 10:
            GPIO.output(LED_RED,GPIO.HIGH)#  10cm 보다 가까우면 빨간색 키고 나머지는 끈다
            print("RED_LED_ON")
            GPIO.output(LED_GREEN,GPIO.LOW)
            GPIO.output(LED_YELLOW,GPIO.LOW)

        elif distance <= 20 and distance > 10:
            GPIO.output(LED_YELLOW,GPIO.HIGH)#  20cm 보다 가깝고10cm보다 멀면 노란색 키고 나머지는 끈다
            print("YELLOW_LED_ON")
            GPIO.output(LED_GREEN,GPIO.LOW)
            GPIO.output(LED_RED,GPIO.LOW)

        elif distance <= 40 and distance > 20:
            GPIO.output(LED_GREEN,GPIO.HIGH) #  40cm 보다 가깝고20cm보다 멀면 초록색 키고 나머지는 끈다
            print("GREEN_LED_ON")
            GPIO.output(LED_RED,GPIO.LOW)
            GPIO.output(LED_YELLOW,GPIO.LOW)

        else:
            GPIO.output(LED_GREEN,GPIO.LOW)
            GPIO.output(LED_YELLOW,GPIO.LOW) #40cm이상이면 아무것도 안하기
            GPIO.output(LED_RED,GPIO.LOW)
        time.sleep(0.03)
        for i in range(len(segments)):
            GPIO.output(segments[i],num[0][i])

        if distance <= 10:            
            
            pwm.ChangeFrequency(1000)       # 거리10cm이하이면 따라 소리가 난다
        else:
            pwm.ChangeFrequency(1)


        if distance <= 27:
            if distance <=27 and distance >24:
                for i in range(len(segments)):
                    GPIO.output(segments[i],num[8][i])
                #세그먼트 9 출력
                pass
            elif distance <=24 and distance >21:
                for i in range(len(segments)):
                    GPIO.output(segments[i],num[7][i])
                #세그먼트 8 출력
                pass
            elif distance <=21 and distance >18:
                for i in range(len(segments)):
                    GPIO.output(segments[i],num[6][i])
                #세그먼트 7 출력
                pass
            elif distance <=18 and distance >15:
                for i in range(len(segments)):
                    GPIO.output(segments[i],num[5][i])
                #세그먼트 6 출력
                pass
            elif distance <=15 and distance >12:
                for i in range(len(segments)):
                    GPIO.output(segments[i],num[4][i])
                #세그먼트 5 출력
                pass
            elif distance <=12 and distance >9:
                for i in range(len(segments)):
                    GPIO.output(segments[i],num[3][i])
                #세그먼트 4 출력
                pass
            elif distance <=9 and distance >6:
                for i in range(len(segments)):
                    GPIO.output(segments[i],num[2][i])
                #세그먼트 3 출력
                pass
            elif distance <=6 and distance >3:
                for i in range(len(segments)):
                    GPIO.output(segments[i],num[1][i])
                #세그먼트 2 출력
                pass
            elif distance <=3 and distance >=0:
                for i in range(len(segments)):
                    GPIO.output(segments[i],num[0][i])
                #세그먼트 1 출력
                pass
        else:
            for i in range(len(segments)):
                GPIO.output(segments[i],num[9][i])
                #아무것도 아닐때

            

        




finally:
    GPIO.cleanup()
    GPIO.output(LED_GREEN,GPIO.LOW)
    GPIO.output(LED_YELLOW,GPIO.LOW) #전부 끄고 나간다
    GPIO.output(LED_RED,GPIO.LOW)
    GPIO.output(BUZZER,GPIO.LOW)
    GPIO.output(ECHO,GPIO.LOW)
    GPIO.output(TRIG,GPIO.LOW)
    GPIO.output(segments,GPIO.LOW)
    print('cleanup and exit')
