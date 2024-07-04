Multiple Python scripts that control the PrusaWorkstation with a Raspberry Pi. It uses a self-build breakout board with a 24V DC Power supply.
It can control 4x24V Outputs, several GPIO Pins, and a 24V 4-pin Fan header.
In addition, it uses a webcam to send images of the chamber via the Prusa Connect API to the Prusa Connect Server. It also reads out the temperature and reports it in the set image.
Furthermore, the script utilizes the temperature to keep the temperature limit. For that, the intake fan's PWM duty cycle is set accordingly. Everything is accessible through a web interface running on the Raspberry Pi.

Changelog

v1
- four buttons in the web interface to control the four 24v DC outputs
- button to toggle auto temperature control on/off
- Prusa Connect API camera
- temperature readout with a 1-wire sensor

v1.1
- serial connection to the printer
- custom M118 E1 addition to the Gcode to trigger the filtration of the chamber, after the print is done, it runs for 10min until it the filtration is stopped
