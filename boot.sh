#!/bin/bash
# 激活虚拟环境
# source /home/orangepi/Desktop/qrcode_detect/venv/bin/activate

# 开启web服务、gpio触发服务、ui服务

sudo apt-get -y install libzbar-dev=0.23.92-4build2
sudo dpkg -i ./lib/MVS-2.1.1_aarch64_20220511.deb