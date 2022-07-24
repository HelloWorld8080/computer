# 安装pip以及创建虚拟环境
## 安装pip
sudo apt-get -y install python3-pip
## 创建并激活虚拟环境
apt install -y python3.10-venv
python3 -m venv venv
source ./venv/bin/activate (退出虚拟环境:deactivate)
# 在venv虚拟环境下安装相关依赖包
pip install -r requirements.txt

