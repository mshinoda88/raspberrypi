#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
import subprocess
from datetime import datetime

# ピン番号
PIN_NUM=14
# スリープ時間 単位：秒
SLEEP_TIME=1.0
# 画像配置ディレクトリ
file_dir = "./"

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUM, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
        while True:
            if(GPIO.input(PIN_NUM)):
                timestamp_format = datetime.now().strftime("%F%m%d%H%M%S")
                print("Detected! :"+ timestamp_format)
                filename = "test_" + timestamp_format + ".jpg"
                file_path = "{0}{1}".format(file_dir, filename)

                print("Taking photo")
                time.sleep(SLEEP_TIME)
                subprocess.getoutput("raspistill -w 400 -h 300 -o {0} -t 1".format(file_path))

                print("Done! Filename :" + filename)
                time.sleep(5)

            else:
                print(GPIO.input(PIN_NUM))
                time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
     GPIO.cleanup()

