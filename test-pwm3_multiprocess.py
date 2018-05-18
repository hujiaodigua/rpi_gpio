import os
import sys
import multiprocessing
import socket

import time
import RPi.GPIO as GPIO

  
#p = GPIO.PWM(18, 50)  # 通道为 18 频率为 50Hz
#p.start(0)
#try:
#    while 1:
#        control_data = s.recv(20)
#        if control_data == b'start':
#            s.send(b'start ok')
#            GPIO.output(18,GPIO.LOW)
            #for dc in range(100, -1, -5):
            #    p.ChangeDutyCycle(dc)
            #    time.sleep(0.1)
            #for dc in range(0, 101, 5):
            #    p.ChangeDutyCycle(dc)
            #    time.sleep(0.1)
#        if control_data == b'end':
#            s.send(b'end ok')
#            GPIO.output(18,GPIO.HIGH)
#except KeyboardInterrupt:
#    pass
#p.stop()
#GPIO.cleanup()

def start_led(control_data):
    control_data = b'null'
    print('start_led')
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.101', 7777))
    s.send(b'start_led_connect ok')
    while 1:
        control_data = s.recv(20)
        if control_data == b'start':
            s.send(b'start ok')


def end_led(control_data):
    control_data = b'null'
    print('end_led')
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.101', 7778))
    s.send(b'end_led_connect ok')
    while 1:
        control_data = s.recv(20)
        if control_data == b'end':
            s.send(b'end ok')


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)  #BCM编号系统
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    
    
    p1 = multiprocessing.Process(target = start_led, args = (control_data,))
    p2 = multiprocessing.Process(target = end_led, args = (control_data,))

    p1.start()
    p2.start()
