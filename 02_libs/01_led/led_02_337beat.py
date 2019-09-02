#!/usr/bin/env python3
# Let the LED flash to the 3-3-7 beat.

# import libraries of GPIO 
import RPi.GPIO as GPIO
# import time library
from time import sleep

# ピン番号
PIN_NUM=4
# スリープ時間 単位：秒
SLEEP_TIME_S=0.2
SLEEP_TIME_L=0.4

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
 
try:
    for i in range(3):
        for j in range(2):	
            for k in range(3):
                GPIO.output(PIN_NUM, GPIO.HIGH)
                sleep(SLEEP_TIME_S)
                GPIO.output(PIN_NUM, GPIO.LOW)
                sleep(SLEEP_TIME_S)
            sleep(SLEEP_TIME_L)

        for j in range(7):
            GPIO.output(PIN_NUM, GPIO.HIGH)
            sleep(SLEEP_TIME_S)
            GPIO.output(PIN_NUM, GPIO.LOW)
            sleep(SLEEP_TIME_S)
        sleep(SLEEP_TIME_L)
 
except KeyboardInterrupt:
    GPIO.cleanup()

