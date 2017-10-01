
import RPi.GPIO as gpio
import time
#23 right motor enable
#17 right backward
#04 right forward input
#22 left motor enable
#25 left backward
#24 left forward input
#18 led
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(18,gpio.OUT)
gpio.setup(23,gpio.OUT)
gpio.setup(17,gpio.OUT)
gpio.setup(4,gpio.OUT)
gpio.setup(22,gpio.OUT)
gpio.setup(25,gpio.OUT)
gpio.setup(24,gpio.OUT)

#move forward
gpio.output(22,1)
gpio.output(24,1)
gpio.output(23,1)
gpio.output(4,1)
gpio.output(18,1)
time.sleep(3)
gpio.output(22,0)
gpio.output(24,0)
gpio.output(23,0)
gpio.output(4,0)
gpio.output(18,0)
time.sleep(1)

