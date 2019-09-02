#!/bin/bash
# This program will edit network configuration file
# to connect wi-fi network.

SSID=$1
PASSWD=$2
CONF_PATH="./wpa_supplicant.conf"
IF=wlan0

if [ $# -lt 2 ]; then
  echo "$0 <SSID> <PASSWD>"
  exit 1
fi

cp ${CONF_PATH} ${CONF_PATH}.org
cat ${CONF_PATH}|sed -e "s/_SSID_/${SSID}/g" \
  |sed -e "s/_PASSWD_/${PASSWD}/g" \
  > ${CONF_PATH}.new
mv ${CONF_PATH}.new ${CONF_PATH}

cat ${CONF_PATH} 
echo "sudo cp ${CONF_PATH} /etc/wpa_supplicant/wpa_supplicant.conf"
echo "sudo ifdown $IF"
echo "sudo ifup $IF"
#sudo cp ${CONF_PATH} /etc/wpa_supplicant/wpa_supplicant.conf
#sudo ifdown $IF
#sudo ifup $IF
exit 0
