import RPi.GPIO as GPIO

LED = 5
import spidev
import time

spi = spidev.SpiDev()

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

spi.open(0,0)



spi.max_speed_hz = 100000


def analog_read(channel):

    ret = spi.xfer2([1,(8+channel) << 4,0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        ldr_value = analog_read(0)
        print("LDR Value: %d" % ldr_value)
        time.sleep(0.5)
        if(ldr_value < 512):
            GPIO.output(LED, GPIO.HIGH)
        if(ldr_value > 512):
            GPIO.output(LED, GPIO.LOW)


finally:
    spi.close()