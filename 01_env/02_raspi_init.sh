#!/bin/bash
## Raspberrypi の環境を更新するプログラムです。
## 必要なライブラリを環境に導入します。

# ラズベリーパイ ソフトウェア 設定ツール (raspi-config)
# で各種設定をします。raspi-configのコマンドを実行すると、青い設定画面が立ち上がります。
echo "sudo raspi-config"

# WiFi country config
sudo raspi-config noint do_wifi_country JP

# ロケール設定
# (ja_JP.UTF-8を選ぶ)
#apt install -y aptitude
#aptitude install -y language-pack-ja
sudo raspi-config noint do_change_locale ja_JP.UTF-8
sudo locale-gen
#sudo apt install -y jfbterm

#export LANG=ja_JP.UTF-8 
#update-locale LANG=ja_JP.UTF-8
#dpkg-reconfigure locales

# Timezoneの設定
# （Asia/Tokyoを選ぶ)
#dpkg-reconfigure tzdata
#sudo timedatectl set-timezone Asia/Tokyo
#timedatectl
sudo raspi-config noint do_change_timezone Asia/Tokyo



