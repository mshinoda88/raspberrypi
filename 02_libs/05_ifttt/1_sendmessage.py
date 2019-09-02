#!/usr/bin/env python3
import requests

# ifttt で slack 連携用に設定したイベント名
ifttt_event_name="raspi-lesson"
# ifttt で連携するアカウントの秘密鍵
ifttt_private_key="your_private_key"

# ラズパイから送りたいメッセージを３つ設定する
MESSAGE_1 = "test1 "
MESSAGE_2 = "test2 "
MESSAGE_3 = "test3 "
print ("sending: " + MESSAGE_1 + MESSAGE_2 + MESSAGE_3)

# IFTTTにリクエストを送る
data = {"value1": MESSAGE_1,
         "value2": MESSAGE_2,
         "value3": MESSAGE_3 }

url = "https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(ifttt_event_name,ifttt_privete_key)
print(url)
response = requests.post(url, data)

print ("done")

