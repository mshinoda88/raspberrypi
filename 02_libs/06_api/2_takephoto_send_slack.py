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

print ("Taking photo...")

subprocess.getoutput("raspistill -w 400 -h 300 -o test.jpg -ev 3 -ISO 800")

print ("Done! Now sending photo...")

slacker = Slacker(slack_api_token)
channel_name = "#" + slack_channel_name
result = slacker.files.upload(file_path,channels=[slack_channel_id])
slacker.pins.add(channel=slack_channel_id, file_=result.body['file']['id'])

print ("Done! Check slack channel")

