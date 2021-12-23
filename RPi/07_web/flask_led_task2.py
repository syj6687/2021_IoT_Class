import RPi.GPIO as GPIO
from flask import Flask, render_template

#Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)


LED_PIN_RED = 21
LED_PIN_BLUE = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_RED, GPIO.OUT)
GPIO.setup(LED_PIN_BLUE, GPIO.OUT)

@app.route("/")
def hello():
    return render_template("led2.html")

@app.route("/led/<op>")
def led_op(op):
    if op == "redon":
        GPIO.output(LED_PIN_RED, GPIO.HIGH)
        return "RED LED ON"
    elif op == "redoff":
        GPIO.output(LED_PIN_RED, GPIO.LOW)
        return "RED LED OFF"
    elif op == "blueon":
        GPIO.output(LED_PIN_BLUE, GPIO.HIGH)
        return "BLUE LED ON"
    elif op == "blueoff":
        GPIO.output(LED_PIN_BLUE, GPIO.LOW)
        return "BLUE LED OFF"
    else:
        return "Error"


# 터미널에서 직접 실행시킨 경우
if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()