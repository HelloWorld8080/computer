# git环境配置
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git clone -b qrcodeDetect https://github.com/HelloWorld8080/computer.git qrcode_detect
# 安装pip以及创建虚拟环境
## 安装pip
sudo apt-get -y install python3-pip
## 创建并激活虚拟环境
apt install -y python3.10-venv
python3 -m venv venv
source ./venv/bin/activate (退出虚拟环境:deactivate)
# 在venv虚拟环境下安装相关依赖包
sudo apt-get -y install libzbar-dev
pip install -r requirements.txt
dpkg -i ./lib/MVS-2.1.1_aarch64_20220511.deb
