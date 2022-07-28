import cv2
import time
import OPi.GPIO as GPIO
import orangepi.pi4 as bd
import requests
from requests import request

BOARD = bd.BOARD
requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
s = requests.session()
s.keep_alive = False
try:
    print("服务启动")
    GPIO.setmode(BOARD)
    GPIO.setup(5, GPIO.IN)
    while True:
        swich = GPIO.input(5)
        print(swich)
        if swich == 0:
            print("已检测到物体")
            time.sleep(1)
            resp = request("get","http://192.168.1.102:5000/shot")
            print('已保存数据')
except Exception as e:
    print(e)
cv2.destroyAllWindows()
