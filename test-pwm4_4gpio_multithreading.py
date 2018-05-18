import _thread
import time
import os
import sys
import socket
import RPi.GPIO as GPIO

#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect(('192.168.0.101', 7777))
#s.send(b'start_led_connect ok')

''''led接的是低电平有效，与L298N控制电机相反'''
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

control_flag = b'null'
speed = 0

def Left_Motor(speed):
        global control_flag
        print('Left_Motor')
        #启动左电机
        IN1.start(0)
        IN2.start(0)
        
        while True:
                if control_flag == b'w': #直行
                        #左电机正转
                        IN1.ChangeDutyCycle(50)
                        IN2.ChangeDutyCycle(100) #全高电平
                        
                elif  control_flag == b'a': #左转
                        #左电机正转
                        IN1.ChangeDutyCycle(50)
                        IN2.ChangeDutyCycle(100)      
                          
                elif  control_flag == b'd': #右转
                        #左电机不转
                        IN1.ChangeDutyCycle(100)
                        IN2.ChangeDutyCycle(100)
                
                elif  control_flag == b's': #倒车
                        #左电机反转
                        IN1.ChangeDutyCycle(100)
                        IN2.ChangeDutyCycle(25)
                
                elif  control_flag == b'q': #停车
                        #左电机不转
                        IN1.ChangeDutyCycle(100)
                        IN2.ChangeDutyCycle(100)

def Right_Motor(speed):
        global control_flag
        print('Right_Motor')
        #启动右电机
        IN3.start(0)
        IN4.start(0)
        while True:
                if control_flag == b'w': #直行
                        #右电机正转
                        IN3.ChangeDutyCycle(50)
                        IN4.ChangeDutyCycle(100)
                        
                elif  control_flag == b'a': #左转
                        #右电机不转
                        IN3.ChangeDutyCycle(100)
                        IN4.ChangeDutyCycle(100)  
                        
                elif  control_flag == b'd': #右转
                        #右电机正转
                        IN3.ChangeDutyCycle(50)
                        IN4.ChangeDutyCycle(100)
                
                elif  control_flag == b's': #倒车
                        #右电机反转
                        IN3.ChangeDutyCycle(100)
                        IN4.ChangeDutyCycle(25)    
                
                elif  control_flag == b'q': #停车
                        #右电机不转
                        IN3.ChangeDutyCycle(100)
                        IN4.ChangeDutyCycle(100)

if __name__ == "__main__":
    try:
        _thread.start_new_thread( Left_Motor, (speed,))
        _thread.start_new_thread( Right_Motor, (speed,))
    except Exception as err:
        print("error:unable to start thread")
        print(err)
    
    control_flag = b'w'
    time.sleep(1)
    control_flag = b'a'
    time.sleep(1)
    control_flag = b'd'
    time.sleep(1)
    control_flag = b's'
    time.sleep(1)
    control_flag = b'q'
    time.sleep(1)
  
    IN1.stop()
    IN2.stop()
    IN3.stop()
    IN4.stop()
    GPIO.cleanup()
    print('Over')
    sys.exit(0)

