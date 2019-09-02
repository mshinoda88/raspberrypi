#!/usr/bin/env python3
# GPIO4を出力としてLEDに給電する

# import libraries of GPIO 
import RPi.GPIO as GPIO
# import time library
from time import sleep

# ピン番号
PIN_NUM=4
# スリープ時間 単位：秒
SLEEP_TIME=0.5

# モードの指定 
#  GPIO.setupmode(GPIO.BOARD|GPIO.BCM)
#  GPIO.BOARD -> 物理ピン番号(左上からの連番)
#  GPIO.BCM   -> 役割ピン番号(broadcomが命名しているもの)
GPIO.setmode(GPIO.BCM)

# ピンの設定
#  GPIO.setup(channel, GPIO.in|GPIO.out)
#  GPIO.in : 入力
#  GPIO.out: 出力
GPIO.setup(PIN_NUM, GPIO.OUT)

# ピンの操作
#  GPIO.output(channel, GPIO.HIGH) : 点灯
#  GPIO.output(channel, GPIO.LOW)  : 消灯
#  val = GPIO.input(channel) : 点灯しているのか、消灯しているのか取得できる
#
#  GPIO.HIGHはTrue, 1 と同義
#  GPIO.LOWはFalse, 0 と同義
 
try:
    while True:
        GPIO.output(PIN_NUM, GPIO.HIGH)
        sleep(SLEEP_TIME)
        GPIO.output(PIN_NUM, GPIO.LOW)
        sleep(SLEEP_TIME)
 
except KeyboardInterrupt:
    GPIO.cleanup()

