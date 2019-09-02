#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

# ピン番号
#  状態出力
PIN_NUM_OUT=4
#  状態入力
PIN_NUM_IN=21

# スリープ時間 単位：秒
SLEEP_TIME=1.0

# GPIOピンの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUM_OUT, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PIN_NUM_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 0.2秒おきにGPIOの値を出力するループ
try:
    while True:
        if GPIO.input(PIN_NUM_IN):
            print("Switch ON")
            GPIO.output(PIN_NUM_OUT , 1)
            sleep(SLEEP_TIME)
        else :
            GPIO.output(PIN_NUM_OUT , 0)
            sleep(SLEEP_TIME)    
except KeyboardInterrupt:
# 最後にGPIOの設定をクリアしておく
    GPIO.cleanup()

