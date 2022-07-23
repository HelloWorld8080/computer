import cv2
import time
import sys
import RPi.GPIO as GPIO
import requests
from requests import request

requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
s = requests.session()
s.keep_alive = False
try:
    print("服务启动")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    while True:
        swich = GPIO.input(4)
        if swich == 0:
            print("已检测到物体")
            time.sleep(1)
            resp = request("get","http://192.168.1.100:5000/shot")
            print('已保存数据')
except Exception as e:
    print(e)
cv2.destroyAllWindows()