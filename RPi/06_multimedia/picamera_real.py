import picamera
import time

path = '/home/pi/src6/06_multimedia'

camera = picamera.PiCamera()
now_str = time.strftime("%Y%m%d_%H%M%S")
try:
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.rotation = 180

    while(1):
        a = int(input("photo:1, video:2, exit:9 > "))
        if(a == 1):
            camera.capture('photo_%s.jpg' % now_str)
        elif(a == 2):
            camera.start_recording('video%s.h264' % now_str)
            b = 'asdfasdf'
            while(1):
                b  = str(input("press enter to stop recoding.."))
                if(b != 'asdfasdf'):
                    camera.stop_recording()
                    break
        elif(a == 9):
            break

finally:
    camera.stop_preview()