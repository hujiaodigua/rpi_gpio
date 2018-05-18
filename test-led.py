# -*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  #BCM编号系统
GPIO.setup(18,GPIO.OUT)

while 1:
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(18,GPIO.LOW)
    time.sleep(0.25)

