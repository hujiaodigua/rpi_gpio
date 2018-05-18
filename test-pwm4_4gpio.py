import _thread
import time
import os
import sys
import socket
import RPi.GPIO as GPIO

''''led接的是低电平有效'''
#设置左电机
IN1, IN2 = 18, 23
GPIO.setmode(GPIO.BCM)  #BCM编号系统
GPIO.setup(IN1, GPIO.OUT)
IN1= GPIO.PWM(IN1, 50)  # 通道为 23 频率为 50Hz
GPIO.setup(IN2, GPIO.OUT)
IN2 = GPIO.PWM(IN2, 50)  # 通道为 23 频率为 50Hz

#设置右电机
IN3, IN4 = 24, 25
GPIO.setmode(GPIO.BCM)  #BCM编号系统
GPIO.setup(IN3, GPIO.OUT)
IN3= GPIO.PWM(IN3, 50)  # 通道为 23 频率为 50Hz
GPIO.setup(IN4, GPIO.OUT)
IN4 = GPIO.PWM(IN4, 50)  # 通道为 23 频率为 50Hz

#启动左电机
IN1.start(0)
IN2.start(0)

#启动右电机
IN3.start(0)
IN4.start(0)

for i in range(1):

        #直行--w
                #左电机正转
                IN1.ChangeDutyCycle(50)
                IN2.ChangeDutyCycle(100) #全高电平
        
                #右电机正转
                IN3.ChangeDutyCycle(50)
                IN4.ChangeDutyCycle(100)
                time.sleep(2)
                
        #左转--a
                #左电机正转
                IN1.ChangeDutyCycle(50)
                IN2.ChangeDutyCycle(100)
        
                #右电机不转
                IN3.ChangeDutyCycle(100)
                IN4.ChangeDutyCycle(100)
                time.sleep(2)
                
        #右转--d
                #左电机不转
                IN1.ChangeDutyCycle(100)
                IN2.ChangeDutyCycle(100)
        
                #右电机正转
                IN3.ChangeDutyCycle(50)
                IN4.ChangeDutyCycle(100)
                time.sleep(2)
                
        #倒车--s
                #左电机反转
                IN1.ChangeDutyCycle(100)
                IN2.ChangeDutyCycle(25)
        
                #右电机反转
                IN3.ChangeDutyCycle(100)
                IN4.ChangeDutyCycle(25)
                time.sleep(2)
                
        #停车--q
                #左电机不转
                IN1.ChangeDutyCycle(100)
                IN2.ChangeDutyCycle(100)
        
                #右电机不转
                IN3.ChangeDutyCycle(100)
                IN4.ChangeDutyCycle(100)
                time.sleep(2)
        
IN1.stop()
IN2.stop()
IN3.stop()
IN4.stop()
GPIO.cleanup()
print('Over')
        
