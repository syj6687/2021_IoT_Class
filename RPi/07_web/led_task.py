from flask import Flask
import RPi.GPIO as GPIO

RED_LED_PIN = 5
GREEN_LED_PIN = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/led/red/on">REDLEDON</a>
        <a href="/led/red/off">REDLEDOFF</a>
        <a href="/led/green/on">GREENLEDON</a>
        <a href="/led/green/off">GREENLEDOFF</a>
    '''

@app.route("/led/<color>/<op>")
def led_op(color,op):

    if color == 'red':
        if op == 'on':
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            return '''        
            <p>RED LED ON</p>
            <a href='/'>Go Home<a>
            '''

        elif op == 'off':
            GPIO.output(RED_LED_PIN, GPIO.LOW)
            return '''
            <p>RED LED OFF</p>
            <a href='/'>Go Home<a>
            '''

    if color == 'green':
        if op == 'on':
            GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
            return '''        
            <p>GREEN LED ON</p>
            <a href='/'>Go Home<a>
            '''

        elif op == 'off':
            GPIO.output(GREEN_LED_PIN, GPIO.LOW)
            return '''
            <p>GREEN LED OFF</p>
            <a href='/'>Go Home<a>
            '''





if __name__ == "__main__":
    try:

        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()