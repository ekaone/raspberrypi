# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
print "Led on"
GPIO.output(18, GPIO.HIGH)
time.sleep(2)
print "Led off"
GPIO.output(18, GPIO.LOW)
