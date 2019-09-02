#!/usr/bin/env python3
import requests
import RPi.GPIO as GPIO
import subprocess
import time
import datetime

# ifttt で slack 連携用に設定したイベント名
ifttt_event_name="raspi-lesson"
# ifttt で連携するアカウントの秘密鍵
ifttt_private_key="your_private_key"

# GPIOピンの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# メッセージを設定する
MESSAGE_1 = "I\'m home! "
MESSAGE_2 = "from me. "

# ボタンが押されたらメッセージを設定してリクエストを送る
try:
    while True:
        if GPIO.input(21):
            print ("Sending message..")
            MESSAGE_3 = datetime.datetime.now().strftime("%F%m%d%H%M%S")
            data = {"value1": MESSAGE_1, "value2": MESSAGE_2, "value3": MESSAGE_3 }
            url = "https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(ifttt_event_name,ifttt_private_key)
            response = requests.post(url, data)
            print ("Done!: " + MESSAGE_1 + MESSAGE_2 + MESSAGE_3)
except KeyboardInterrupt:
    GPIO.cleanup()

