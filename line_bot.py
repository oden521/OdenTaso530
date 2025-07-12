# ライン公式で天気用を取得する
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv('LINE_ACCSESS_TOKEN')

from linebot.v3.messaging import MessagingApi, PushMessageRequest, TextMessage
from linebot.v3.configuration import Configuration
from linebot.v3.http_client import api_client
import pprint
import json

configuration = Configuration(
    access_token=access_token
)


message = '{\"to\":\"ここにユーザーIDを入力する\",\"messages\":[{\"type\":\"text\",\"text\":\"\"}]}'
message_dict = json.loads(message)

message = json.loads(message)

message['messages'][0]['text'] = "Hello World!"

# APIクライアントとメッセージ送信
with api_client(configuration) as api_client:
    messaging_api = MessagingApi(api_client)

    push_message_request = PushMessageRequest(
        to=USER_ID,
        messages=[
            TextMessage(text="Hello World!")
        ]
    )
    try:
        
        response = messaging_api.push_message(push_message_request)
        print("✅ メッセージ送信成功:", response)

    except Exception as e:
        print("❌ メッセージ送信失敗:", e)
        print("Exception when calling MessagingApi->push_message: %s\n" % e)