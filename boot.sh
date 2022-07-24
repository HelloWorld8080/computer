#!/bin/bash
# 激活虚拟环境
# source /home/orangepi/Desktop/qrcode_detect/venv/bin/activate

# 开启web服务、gpio触发服务、ui服务
(/home/orangepi/Desktop/qrcode_detect/venv/bin/python /home/orangepi/Desktop/qrcode_detect/webserver.py) & (/home/orangepi/Desktop/qrcode_detect/venv/bin/python /home/orangepi/Desktop/qrcode_detect/server.py) & (/home/orangepi/Desktop/qrcode_detect/venv/bin/python /home/orangepi/Desktop/qrcode_detect/app.py)