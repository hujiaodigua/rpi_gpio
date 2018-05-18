import _thread
import time
import os
import sys
import socket
import RPi.GPIO as GPIO

#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect(('192.168.0.101', 7777))
#s.send(b'start_led_connect ok')

right, left = 23, 18
GPIO.setmode(GPIO.BCM)  #BCM编号系统
GPIO.setup(right, GPIO.OUT)
right= GPIO.PWM(right, 50)  # 通道为 23 频率为 50Hz
GPIO.setup(left, GPIO.OUT)
left = GPIO.PWM(left, 50)  # 通道为 23 频率为 50Hz

transf = 0 #-2, -1, 0 ,1, 2.
dc = 0
#if control_data == b'start':
def set_speed(speed):
        """ speed = 1 # -1, 0, 1
        """
        global dc
        if speed == -1:
            pass
        elif speed == 0:
            dc = 0
        elif speed == 1:
            dc = 50
control_data = 0
def start_led(control_data):
    global transf, dc
    print('start_led')
    right.start(0)
    while True:
        if transf == -2:
             right.ChangeDutyCycle(dc*0.8)
        elif transf == -1:
            right.ChangeDutyCycle(dc*0.6)
        elif transf == 0:
             right.ChangeDutyCycle(dc)
        elif transf == 1:
             right.ChangeDutyCycle(dc*0.4)
        elif transf == 2:
             right.ChangeDutyCycle(dc*0.2)
            
def end_led(control_data):
    global transf, dc
    print('end_led')
    left.start(0)
    while True:
        if transf == -2:
             left.ChangeDutyCycle(dc*0.2)
        elif transf == -1:
            left.ChangeDutyCycle(dc*0.4)
        elif transf == 0:
             left.ChangeDutyCycle(dc)
        elif transf == 1:
             left.ChangeDutyCycle(dc*0.6)
        elif transf == 2:
             left.ChangeDutyCycle(dc*0.8)


if __name__ == "__main__":
    try:
        _thread.start_new_thread(start_led, (control_data,))
        _thread.start_new_thread(end_led, (control_data,))
    except Exception as err:
        print("error:unable to start thread")
        print(err)
    set_speed(1)
    
    for i in range(3):
        for e in [-2, -1, 0 ,1, 2]:
            transf = e
            print(transf)
            time.sleep(0.5)
    right.stop()
    left.stop()
    GPIO.cleanup()
    print('Over')

