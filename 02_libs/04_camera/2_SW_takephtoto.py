#!/usr/bin/env python3
import RPi.GPIO as GPIO
import subprocess
import time
import datetime

# ピン番号
PIN_NUM=21
# スリープ時間 単位：秒
SLEEP_TIME=1.0

# GPIOピンの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

file_dir = "./"

try:
    while True:
        if GPIO.input(PIN_NUM): 
            # 現在時間をファイル名に追加する
            timestamp = datetime.datetime.now()
            timestamp_format = timestamp.strftime("%F%m%d%H%M%S")
            filename = "test_" + timestamp_format + ".jpg"
            file_path = "{0}{1}".format(file_dir, filename)
            print("Taking photo")
            time.sleep(SLEEP_TIME)
            subprocess.getoutput("raspistill -w 400 -h 300 -o {0} -t 1".format(file_path))
            print("Done! Filename:" + filename)
except KeyboardInterrupt:
    GPIO.cleanup()

