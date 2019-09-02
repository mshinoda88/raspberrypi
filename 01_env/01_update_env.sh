#!/bin/bash
## Raspberrypi の環境を更新するプログラムです。
## 必要なライブラリを環境に導入します。

# ラズベリーパイ ソフトウェア 設定ツール (raspi-config)
# で各種設定をします。raspi-configのコマンドを実行すると、青い設定画面が立ち上がります。
sudo raspi-config

# OS update
sudo apt update && sudo apt upgrade -y 

# install libraries
sudo apt install -y git python3 python3-dev python3-pip python3-rpi.gpio i2c-tools wget zip tree 



