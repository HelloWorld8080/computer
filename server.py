import time
import requests
from requests import request
try:
    print("服务启动")
    while True:
        trigger = request("get","http://127.0.0.1:5000/hasDetectCode")
        if trigger.text != "0":
            print("已检测到物体")
            request("get","http://127.0.0.1:5000/shot")
            print('已保存数据')
            time.sleep(1)
except Exception as e:
    print(e)