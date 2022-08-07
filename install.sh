myPath="/etc/sysconfig"

systemctl stop qrcode-server
systemctl stop qrcode-webserver

mkdir $myPath
touch $myPath/qrcodeDetectEx

echo "QRCODE_SERVER=$(dirname $(readlink -f "$0"))/server-boot.sh" > $myPath/qrcodeDetectEx
echo "QRCODE_WEBSERVER=$(dirname $(readlink -f "$0"))/webserver-boot.sh" >> $myPath/qrcodeDetectEx

mkdir /usr/lib/systemd/system

cp -r $(dirname $(readlink -f "$0"))/qrcode-server.service /usr/lib/systemd/system
cp -r $(dirname $(readlink -f "$0"))/qrcode-webserver.service /usr/lib/systemd/system
chmod 777 $(dirname $(readlink -f "$0"))/webserver/webserver
chmod 777 $(dirname $(readlink -f "$0"))/server/server
systemctl daemon-reload

echo "server path: $(dirname $(readlink -f "$0"))"
echo "qrcodeserver install success"