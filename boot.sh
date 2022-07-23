#!/bin/bash
# 激活虚拟环境
# source /home/pi/Desktop/qrcode_detect/venv/bin/activate

# 开启web服务、gpio触发服务、ui服务
(/home/pi/Desktop/qrcode_detect/venv/bin/python /home/pi/Desktop/qrcode_detect/webserver.py) & (/home/pi/Desktop/qrcode_detect/venv/bin/python /home/pi/Desktop/qrcode_detect/server.py) & (/home/pi/Desktop/qrcode_detect/venv/bin/python /home/pi/Desktop/qrcode_detect/app.py)