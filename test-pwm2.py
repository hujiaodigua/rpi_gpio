import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  #BCM编号系统
GPIO.setup(23, GPIO.OUT)
  
p = GPIO.PWM(23, 50)  # 通道为 23 频率为 50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
