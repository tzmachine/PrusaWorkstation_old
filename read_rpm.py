import RPi.GPIO as GPIO
import time

TACH_PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(TACH_PIN, GPIO.IN)

try:
    while True:
        pin_state = GPIO.input(TACH_PIN)
        print(f"GPIO {TACH_PIN} state: {pin_state}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Test beendet")
finally:
    GPIO.cleanup()
