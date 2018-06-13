#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import socket
import _thread

s_dht11 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_dht11.connect(('192.168.1.111', 8888))
s_dht11.send(b'dht11 connect ok')

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

def dht11_read():
	#time.sleep(1)
	channel =4 #GPIO7
	data = []
	j = 0
	GPIO.setmode(GPIO.BCM)

	time.sleep(1)

	GPIO.setup(channel, GPIO.OUT)
	GPIO.output(channel, GPIO.LOW)
	time.sleep(0.02)
	GPIO.output(channel, GPIO.HIGH)
	GPIO.setup(channel, GPIO.IN)

	while GPIO.input(channel) == GPIO.LOW:
	  continue
	while GPIO.input(channel) == GPIO.HIGH:
	  continue

	while j < 40:
	  k = 0
	  while GPIO.input(channel) == GPIO.LOW:
	    continue
	  while GPIO.input(channel) == GPIO.HIGH:
	    k += 1
	    if k > 100:
	      break
	  if k < 8:
	    data.append(0)
	  else:
	    data.append(1)

	  j += 1

	#print("sensor is working.")
	#print(data)

	humidity_bit = data[0:8]
	humidity_point_bit = data[8:16]
	temperature_bit = data[16:24]
	temperature_point_bit = data[24:32]
	check_bit = data[32:40]

	humidity = 0
	humidity_point = 0
	temperature = 0
	temperature_point = 0
	check = 0

	for i in range(8):
	  humidity += humidity_bit[i] * 2 ** (7-i)
	  humidity_point += humidity_point_bit[i] * 2 ** (7-i)
	  temperature += temperature_bit[i] * 2 ** (7-i)
	  temperature_point += temperature_point_bit[i] * 2 ** (7-i)
	  check += check_bit[i] * 2 ** (7-i)

	tmp = humidity + humidity_point + temperature + temperature_point

	if check == tmp:
	  #print("temperature :", temperature, "*C, humidity :", humidity, "%")
	  s_dht11.send(bytes('temperature: %d' % temperature,'utf-8'))
	  s_dht11.send(bytes('humidity: %d' % humidity,'utf-8'))
	else:
          pass
	  #print("wrong")
	  #print("temperature :", temperature, "*C, humidity :", humidity, "% check :", check, ", tmp :", tmp)

	#GPIO.cleanup()

def hc_sr04_read():
	#print('Distance Measurement In Progress')

	#GPIO.setmode(GPIO.BCM)
	#TRIG = 2
	#ECHO = 3
	#GPIO.setup(TRIG,GPIO.OUT)
	#GPIO.setup(ECHO,GPIO.IN)

	GPIO.setmode(GPIO.BCM)
	TRIG = 2
	ECHO = 3
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	#led

	# 发送 trig 信号  持续 10us 的方波脉冲
	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)


	# 等待低电平结束，然后记录时间。
	while GPIO.input(ECHO) == 0:
		pass
	pulse_start = time.time()

	# 等待高电平结束，然后记录时间。
	while GPIO.input(ECHO) == 1:
		pass
	pulse_end = time.time()
	    
	    
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance,2)
	if distance > 0 and distance < 1000:
	    #print("Distance: {}cm".format(distance))
	    s_dht11.send(bytes('distance_cm: %d' % distance ,'utf-8'))
	    if distance >= 5*1.5 and distance < 10*1.5:
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)
                GPIO.output(26,GPIO.LOW)
                GPIO.output(21,GPIO.LOW)
                GPIO.output(20,GPIO.HIGH)
	    if distance >= 10*1.5 and distance < 15*1.5:
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)
                GPIO.output(26,GPIO.LOW)
                GPIO.output(21,GPIO.HIGH)
                GPIO.output(20,GPIO.HIGH)
	    if distance >= 15*1.5 and distance < 20*1.5:
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)
                GPIO.output(26,GPIO.HIGH)
                GPIO.output(21,GPIO.HIGH)
                GPIO.output(20,GPIO.HIGH)
	    if distance >= 20*1.5 and distance < 25*1.5:
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(19,GPIO.HIGH)
                GPIO.output(26,GPIO.HIGH)
                GPIO.output(21,GPIO.HIGH)
                GPIO.output(20,GPIO.HIGH)
	    if distance >= 25*1.5 and distance < 30*1.5:
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.LOW)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(19,GPIO.HIGH)
                GPIO.output(26,GPIO.HIGH)
                GPIO.output(21,GPIO.HIGH)
                GPIO.output(20,GPIO.HIGH)
	    if distance >= 30*1.5 and distance < 35*1.5:
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(19,GPIO.HIGH)
                GPIO.output(26,GPIO.HIGH)
                GPIO.output(21,GPIO.HIGH)
                GPIO.output(20,GPIO.HIGH)
	    if distance >= 35*1.5:
                GPIO.output(5,GPIO.HIGH)
                GPIO.output(6,GPIO.HIGH)
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(19,GPIO.HIGH)
                GPIO.output(26,GPIO.HIGH)
                GPIO.output(21,GPIO.HIGH)
                GPIO.output(20,GPIO.HIGH)
	    if distance > 0 and distance < 5*1.5:
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.LOW)
                GPIO.output(13,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)
                GPIO.output(26,GPIO.LOW)
                GPIO.output(21,GPIO.LOW)
                GPIO.output(20,GPIO.LOW)

	else:
            pass
	    #print("wrong")
	#GPIO.cleanup()
	#time.sleep(1)

if __name__ == "__main__":
    while True:
        #time.sleep(0.01)
        dht11_read()
        time.sleep(0.1)
        hc_sr04_read()
