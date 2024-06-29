import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)


def connect_to_printer(port='/dev/ttyACM0', baudrate=115200, timeout=2):
    try:
        ser = serial.Serial(port, baudrate, timeout)
        print(f"Connected to {port} at {baudrate} baudrate")
        return ser
    except serial.SerialException as e:
        print(f"Could not connect to {port}: {e}")
        return None

ser =  connect_to_printer()

global printing
printing = False

while True:
        line = ser.readline().decode('utf-8').strip()
        if line.startswith('echo:'):
            message = line[len('echo:'):].strip()  # Entferne 'echo:' und führende/trailing Leerzeichen
            print(message)
            if "Filter ein" in message:
                print("Filter eingeschaltet!")
                # wenn M118 mit dieser Nachricht während des Druckes kommt, so bleibt der Lüfter eingeschaltet,
                # da printing == True, zudem wartet der RPi nach dem Befehl 3min
                if printing == False :
                    time.sleep(60)
                    GPIO.output(12, GPIO.HIGH)
                    printing = True
                else: 
                    GPIO.output(12, GPIO.HIGH)

            if "Filter aus" in message:
                print("Filter ausgeschaltet!")
                # wenn M118 mit dieser Nachricht während des Druckes kommt, so bleibt der Lüfter ausgeschaltet, da printing == False
                # zudem wartet der RPi nach dem Befehl 10min, bevor der Lüfter ausgeschaltet wird
                if printing == True :
                    time.sleep(180)
                    GPIO.output(12, GPIO.LOW)
                    printing = False
                else: 
                    GPIO.output(12, GPIO.LOW)
GPIO.cleanup()
