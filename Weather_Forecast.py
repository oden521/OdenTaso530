# ライン公式で天気用を取得する
import os
from dotenv import load_dotenv
from pathlib import Path

import requests
# ライブラリのインポート

import json
# API取得のためにjsonのインポート

from datetime import datetime, timedelta

#scheduleのインポート
import schedule
import time

#.envファイルの読み込み
env_path = Path(__file__).resolve().parent.parent/ '.env'
load_dotenv(dotenv_path=env_path)

# 環境変数からAPIキーを取得
api_key = os.getenv('OPENWEATHERMAP_API_KEY')

#都市名の指定 
city_name = 'Fukuoka'

# フラグ時間の設定
# flag_run_Time1 = "08:00"
# flag_run_Time2 = "19:00"

def get_weathre():

    print("天気情報を取得します。")

    #APIのエンドポイントとパラメータを設定
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    #地名を指定
    query_city = f"q={city_name}"
    #単位を指定
    query_units = "units=metric"
    #言語を指定
    query_lang = "lang=ja"

    from datetime import datetime   

    url = f"{base_url}?{query_city}&{query_units}&{query_lang}&appid={api_key}"
    print("URL:", url)
    return url

def job():
    try:
        now = datetime.now()
    # 現在の日時を取得
        getFalagTime = now.strftime("%H:%M")


        print(now.strftime("%Y年%m月%d日 %H:%M:%S" + "の天気情報:"))

        # 関数の呼び出し
        url = get_weathre()
        response = requests.get(url)

        # レスポンスの確認
        print("レスポンス:", response)
        print(response.json())
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))

        data = response.json()
   
        if data["cod"]:

        # 天気情報の表示
            print(str(data["name"]) + "の天気は" + str(data["weather"][0]["description"]) + "です。")
            print("気温は" + str(data["main"]["temp"]) + "℃です。")

        else:
            print("天気情報の取得に失敗しました。")
            exit(1)
    except Exception as e:
            print("エラーが発生しました:", e)
            print("APIキーが正しいか、またはネットワーク接続を確認してください。")
            exit(1)

# スケジュールの設定
print("スケジュールを実行します。")

job()

# スケジュールの設定
# schedule.every().day.at(flag_run_Time).do(job)
# schedule.every().day.at(flag_run_Time2).do(job)


#スケジュール実行ループ
while True:
    schedule.run_pending()
    time.sleep(1)
    

