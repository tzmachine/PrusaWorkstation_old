from flask import Flask, render_template, jsonify, request
import RPi.GPIO as GPIO
import time
import subprocess
from control_fan import setFanSpeed, calcDutyCycle
from read_temp import read_temp

app = Flask(__name__)

# GPIO setup
GPIO.setmode(GPIO.BCM)
pins = [6, 12, 5, 0]
pin_states = {6: False, 12: False, 5: False, 0: False}

g_temp = 30
max_temp = 42

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

auto_mode_enabled = False

GPIO.setup(14, GPIO.OUT)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

GPIO.output(6, GPIO.HIGH)

@app.route('/')
def index():
    temp = read_temp()
    return render_template('index.html', pin_states=pin_states, temperature=temp, auto_mode_enabled=auto_mode_enabled)

@app.route('/toggle/<int:pin>', methods=['POST'])
def toggle_pin(pin):
    if pin in pins:
        current_state = GPIO.input(pin)
        GPIO.output(pin, not current_state)
        pin_states[pin] = not current_state
    return jsonify({'state': pin_states[pin]})

@app.route('/toggle_auto_mode', methods=['POST'])
def toggle_auto_mode():
    global auto_mode_enabled
    auto_mode_enabled = not auto_mode_enabled
    if auto_mode_enabled:
        setFanSpeed(0)
        while auto_mode_enabled:
            temp = read_temp()
            dc = calcDutyCycle(temp,g_temp, max_temp)
            print(dc, temp)
            setFanSpeed(dc)
            time.sleep(5)
    else:
        setFanSpeed(0)
        pass
    return jsonify({'success': True, 'auto_mode_enabled': auto_mode_enabled})

@app.route('/temperature')
def get_temperature():
    temp = read_temp()
    return str(temp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
