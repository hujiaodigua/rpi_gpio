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
ENA = 17
GPIO.setmode(GPIO.BCM)  #BCM编号系统
GPIO.setup(IN1, GPIO.OUT)
#IN1= GPIO.PWM(IN1, 2000)  # 通道为 18 频率为 2000Hz
GPIO.setup(IN2, GPIO.OUT)
#IN2 = GPIO.PWM(IN2, 2000)  # 通道为 23 频率为 2000Hz
GPIO.setup(ENA, GPIO.OUT)
ENA= GPIO.PWM(ENA, 2000)  # 通道为 17接 ENA 频率为 2000Hz
ENA.ChangeDutyCycle(dc)


#设置右电机
IN3, IN4 = 24, 25
ENB = 22
GPIO.setmode(GPIO.BCM)  #BCM编号系统
GPIO.setup(IN3, GPIO.OUT)
#IN3= GPIO.PWM(IN3, 2000)  # 通道为 24 频率为 2000Hz
GPIO.setup(IN4, GPIO.OUT)
#IN4 = GPIO.PWM(IN4, 2000)  # 通道为 25 频率为 2000Hz
GPIO.setup(ENB, GPIO.OUT)
ENB= GPIO.PWM(ENB, 2000)  # 通道为 22 接 ENA 频率为 2000Hz
ENB.ChangeDutyCycle(dc)

control_flag = b'null'
speed = 0
dcA = 0
dcB = 0

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.101', 7777))
s.send(b'connect ok')

def Left_Motor(speed):
        global control_flag
        print('Left_Motor')
        #启动电机
        ENA.start(0)
        ENB.start(0)
        
        while True:
				if control_flag != b's':
				
					GPIO.output(IN1,GPIO.HIGH)
					GPIO.output(IN2,GPIO.LOW)
					GPIO.output(IN3,GPIO.HIGH)
					GPIO.output(IN4,GPIO.LOW)
					
					if control_flag == b'w': #直行
						dcA = 55
						dcB = 55
							
					elif  control_flag == b'd': #右转
						dcA = 55
						dcB = 35
							  
					elif  control_flag == b'a': #左转
						dcA = 35
						dcB = 55
					
					
					elif  control_flag == b'q': #停车
						dcA = 0
						dcB = 0
				
				if  control_flag == b's': #倒车
					GPIO.output(IN1,GPIO.LOW)
					GPIO.output(IN2,GPIO.HIGH)
					GPIO.output(IN3,GPIO.LOW)
					GPIO.output(IN4,GPIO.HIGH)
					dcA = 40
					dcB = 40

def Right_Motor(speed):
        global control_flag
        print('Right_Motor')
        #启动右电机
        IN3.start(0)
        IN4.start(0)
        while True:
                if control_flag == b'w': #直行
                        #右电机正转
                        IN3.ChangeDutyCycle(dc)
                        IN4.ChangeDutyCycle(0)
                        
                elif  control_flag == b'd': #右转
                        #右电机不转
                        IN3.ChangeDutyCycle(0)
                        IN4.ChangeDutyCycle(0)  
                        
                elif  control_flag == b'a': #左转
                        #右电机正转
                        IN3.ChangeDutyCycle(dc)
                        IN4.ChangeDutyCycle(0)
                
                elif  control_flag == b's': #倒车
                        #右电机反转
                        IN3.ChangeDutyCycle(0)
                        IN4.ChangeDutyCycle(dc)    
                
                elif  control_flag == b'q': #停车
                        #右电机不转
                        IN3.ChangeDutyCycle(0)
                        IN4.ChangeDutyCycle(0)

#def tcp_recv_control_flag(speed):
#        global control_flag
#        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#        s.connect(('192.168.0.101', 7777))
#        s.send(b'connect ok')
#        
#        while True:
#                control_flag = s.recv(20)
#                if control_flag == b'cutoff':
#                        IN1.stop()
#                        IN2.stop()
#                        IN3.stop()
#                        IN4.stop()
#                        GPIO.cleanup()
#                        print('Over')
#                        sys.exit(0)
#                        break
        
if __name__ == "__main__":
    try:
        _thread.start_new_thread( Left_Motor, (speed,))
        #_thread.start_new_thread( Right_Motor, (speed,))
    except Exception as err:
        print("error:unable to start thread")
        print(err)

    #s.send(("w: 直行,a: 左转,d: 右转,s: 倒车,q: 停车").encode('utf-8')) #python3 send只支持ASC2编码，而中文是utf编码，所以收端要解码
    s.send(('\r\nw:up, a:left, d:right, s:down, q:stop\r\ncutoff:cut connect').encode('utf-8'))

    while True:
            control_flag = s.recv(20)
            if control_flag == b'cutoff':
                s.send(b'cut connect')
                IN1.stop()
                IN2.stop()
                IN3.stop()
                IN4.stop()
                GPIO.cleanup()
                print('Over')
                sys.exit(0)
                break

#    control_flag = b'w'
#    time.sleep(1)
#    control_flag = b'a'
#    time.sleep(1)
#    control_flag = b'd'
#    time.sleep(1)
#    control_flag = b's'
#    time.sleep(1)
#    control_flag = b'q'
#    time.sleep(1)
  
#    IN1.stop()
#    IN2.stop()
#    IN3.stop()
#    IN4.stop()
#    GPIO.cleanup()
#    print('Over')
#    sys.exit(0)

