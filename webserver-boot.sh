#!/bin/bash
# 激活虚拟环境
# source /home/orangepi/Desktop/qrcode_detect/venv/bin/activate

# 开启web服务、gpio触发服务、ui服务
# export MVCAM_SDK_PATH=/home/orangepi/Desktop/qrcode_detect/MVS

# export MVCAM_COMMON_RUNENV=/home/orangepi/Desktop/qrcode_detect/MVS/lib
# export LD_LIBRARY_PATH=/home/orangepi/Desktop/qrcode_detect/MVS/lib/aarch64:$LD_LIBRARY_PATH

#  /home/orangepi/Desktop/qrcode_detect/venv/bin/python /home/orangepi/Desktop/qrcode_detect/webserver.py

export MVCAM_SDK_PATH=$(dirname $(readlink -f "$0"))/webserver/MVS

export MVCAM_COMMON_RUNENV=$(dirname $(readlink -f "$0"))/webserver/MVS/lib
export LD_LIBRARY_PATH=$(dirname $(readlink -f "$0"))/webserver/MVS/lib/aarch64:$LD_LIBRARY_PATH

$(dirname $(readlink -f "$0"))/webserver/webserver
# $(dirname $(readlink -f "$0"))/venv/bin/python $(dirname $(readlink -f "$0"))/webserver.py
echo $(dirname $(readlink -f "$0"))
echo "webserver boot success"