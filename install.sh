myPath="/etc/sysconfig"

systemctl stop qrcode-server
systemctl stop qrcode-webserver

mkdir $myPath
touch $myPath/qrcodeDetect1

echo "QRCODE_SERVER=$(dirname $(readlink -f "$0"))/server-boot.sh" > $myPath/qrcodeDetect1
echo "QRCODE_WEBSERVER=$(dirname $(readlink -f "$0"))/webserver-boot.sh" >> $myPath/qrcodeDetect1

mkdir /usr/lib/systemd/system

cp -r $(dirname $(readlink -f "$0"))/qrcode-server.service /usr/lib/systemd/system
cp -r $(dirname $(readlink -f "$0"))/qrcode-webserver.service /usr/lib/systemd/system
chmod 777 $(dirname $(readlink -f "$0"))/webserver.py
chmod 777 $(dirname $(readlink -f "$0"))/server.py
systemctl daemon-reload

echo "server path: $(dirname $(readlink -f "$0"))"
echo "qrcodeserver install success"