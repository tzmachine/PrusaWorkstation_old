import time
import RPi.GPIO as GPIO
from read_temp import read_temp

#set temp range
g_temp = 36
max_temp = 42

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

#function to calculate the dutycycle, proportional between goal temp and max temp
def calcDutyCycle(r_t, g_t, max_t):
	if r_t <= g_t:
		return 0
	elif r_t >= max_t:
		return 100
	else:
		return	(r_t-g_t)/(max_t-g_t) *100

def setFanSpeed(dc):
	p.ChangeDutyCycle(dc)	

p = GPIO.PWM(14, 25000)  # channel=14 frequency=25000Hz
p.start(0)
GPIO.cleanup()
