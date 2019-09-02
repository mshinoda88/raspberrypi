#!/usr/bin/env python3
from subprocess import getoutput
from slacker import Slacker

# slack API トークン
slack_api_token = "xoxp-XXX"
# slack で投稿先のチャンネル名
slack_channel_name="seminar_raspi-testspace"

MESSAGE_1 = "メッセージ送信てすと"


# SlackAPIを使ってメッセージをslackに投稿する
print ("Sending message..")
slacker = Slacker(slack_api_token)
channel_name = "#" + slack_channel_name
slacker.chat.post_message(channel_name, MESSAGE_1)

print ("Done! Check slack channel")
