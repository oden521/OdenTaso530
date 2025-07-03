# ライン公式で天気用を取得する
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv('LINE_ACCSESS_TOKEN')

import linebot.v3.message
import pprint
import json

configuration = linebot.v3.message.Configuration(
    access_token=os.getenv('LINE_ACCSESS_TOKEN')
)


message = '{\"to\":\"ここにユーザーIDを入力する\",\"messages\":[{\"type\":\"text\",\"text\":\"\"}]}'
message_dict = json.loads(message)

message = json.loads(message)

message['messages'][0]['text'] = "Hello World!"

with linebot.v3.messaging.ApiClient(configuration) as api_client:
    api_instance = linebot.v3.messaging.MessagingApi(api_client)
    push_message_request = linebot.v3.messaging.PushMessageRequest.from_dict(message_dict)

    try:
        print("calling messageingApi->push_message with:\n")
        
        api_response = api_instance.push_message(push_message_request)
        print("The response of MessagingApi->push_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagingApi->push_message: %s\n" % e)