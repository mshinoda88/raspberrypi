#!/usr/bin/env python3

from datetime import datetime
from time import sleep
import RPi.GPIO as GPIO
import requests
import subprocess
from slacker import Slacker

# slack API トークン
slack_api_token = "xoxp-XXX"
# slack で投稿先のチャンネル名
slack_channel_name="seminar_raspi-testspace"
# slack で投稿先のチャンネルのチャンネルID
slack_channel_id='CM8MA9QS2'

# アップロードファイルパス
file_path = "./test.jpg"

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(14, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        if(GPIO.input(14)):
            timestamp_format = datetime.now().strftime('%Y%m%d%H%M%S')
            print("Detected! :"+ timestamp_format)

            #LEDを光らせる
            GPIO.output(4 , 1)
            sleep(1)
            GPIO.output(4 , 0)

            # 写真を撮ってslackに投稿する
            subprocess.getoutput("raspistill -w 400 -h 300 -o {0} -t 1".format(file_path))
            slacker = Slacker(slack_api_token)
            channel_name = "#" + slack_channel_name
            result = slacker.files.upload(file_path, channels=[slack_channel_id])
            slacker.pins.add(channel=slack_channel_id, file_=result.body['file']['id'])
            slacker.chat.post_message(slack_channel_name, timestamp_format)
            sleep(5)
        else:
            print(GPIO.input(14))
            sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

