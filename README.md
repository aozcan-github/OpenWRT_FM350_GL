Commands cheatsheet,

python -m pip install pyserial

wget https://github.com/aozcan-github/OpenWRT_FM350_GL/raw/refs/heads/main/fm350.py -P /root/\
wget https://github.com/aozcan-github/OpenWRT_FM350_GL/raw/refs/heads/main/fm350.sh -O /etc/init.d/fm350\
chmod +x /etc/init.d/fm350

/etc/init.d/fm350 stop\
/etc/init.d/fm350 start\
/etc/init.d/fm350 status

=============

opkg update

opkg install kmod-usb-net-rndis usb-modeswitch kmod-usb-serial kmod-usb-serial-option kmod-usb-serial-wwan kmod-usb-net-cdc-ether kmod-usb-net kmod-mii kmod-usb-serial-ch341 kmod-usb-uhci luci-proto-qmi luci-proto-mbim kmod-usb-net-qmi-wwan kmod-usb-serial-qualcomm picocom usbutils minicom

echo 0e8d 7126 > /sys/bus/usb-serial/drivers/generic/new_id\
minicom -D /dev/ttyUSB2

AT+CGDCONT=1,"IPV4V6","telstra.internet",,0,0,0,0,0,0,0\
AT+CGACT=1,1\
AT+CGPADDR=1

ifconfig eth2 down\
ifconfig eth2 19.199.199.99\
ifconfig eth2 up\
ip route add default via 19.199.199.1 dev eth2

susb && lsusb -t\
ls /dev/ttyUSB*

echo 0e8d 7126 > /sys/bus/usb-serial/drivers/generic/new_id\
stty -echo -opost -F /dev/ttyUSB2\
echo -e -n "AT+CGDCONT=1,\"IPV4V6\",\"telstra.internet\",,0,0,0,0,0,0,0\r\n" > /dev/ttyUSB2\
echo -e -n "AT+CGACT=1,1\r\n" > /dev/ttyUSB2\
echo -e -n "AT+CGPADDR=1\r\n" > /dev/ttyUSB2\
cat /dev/ttyUSB2
