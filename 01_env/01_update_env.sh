#!/bin/bash
## Raspberrypi の環境を更新するプログラムです。
## 必要なライブラリを環境に導入します。

# OS update
sudo apt update && sudo apt upgrade -y 

# install libraries
sudo apt install -y git python3 python3-dev python3-pip python3-rpi.gpio i2c-tools wget zip tree 



