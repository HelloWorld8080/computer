from requests import request
import time
import shutil
import json
from pathPro import ROOT
import os

trigger = ""
pathdir= ""
print("扫码服务启动")
while True:
    try:
        req=request("get","http://127.0.0.1:5000/hasDetectCode")
        data = json.loads(req.text)
        trigger = data['trigger']
        pathdir = data['pathdir']
        if trigger != "0":
            print("已检测到物体")
            request("get","http://127.0.0.1:5000/saveResults?pathdir="+pathdir)
            print('已保存数据')
            time.sleep(1)
    except Exception as e:
        print("trigger:",trigger," pathdir:",pathdir)
        if os.path.exists(os.path.join(ROOT,pathdir)):
            shutil.rmtree(os.path.join(ROOT,pathdir))
        print("webserver未启动或崩溃，请重启启webserver服务")
        time.sleep(1)
