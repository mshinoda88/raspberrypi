#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

# ピン番号
PIN_NUM=14
# スリープ時間 単位：秒
SLEEP_TIME=0.2

# GPIOピンの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUM, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        print(GPIO.input(PIN_NUM))
        sleep(SLEEP_TIME)

except KeyboardInterrupt:
    GPIO.cleanup()
