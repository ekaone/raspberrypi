# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

while True:
 GPIO.output(18, GPIO.HIGH)
 sleep(1)
 GPIO.output(18, GPIO.LOW)
 sleep(1) 
