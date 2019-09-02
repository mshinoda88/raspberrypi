#!/usr/bin/env python3
# 設定秒数ごとにGPIOの値を出力して標準出力するサンプル

import RPi.GPIO as GPIO
import time

# 出力する間隔：単位 秒
SLEEP_TIME=0.2
# 入力ピン番号
PIN_NUM=21

# GPIOピンの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 指定時間ごとにGPIOの値を出力する
try:
    while True:
        print(GPIO.input(PIN_NUM))
        time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
    GPIO.cleanup()

