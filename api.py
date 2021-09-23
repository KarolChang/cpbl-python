# ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 連線取得 json 檔案
import urllib.request as req
import urllib.parse as parse
import json

# url
url = "https://www.cpbl.com.tw/box/getlive"

def fetchDatas(gameSno, kindCode, year, dataType):
  postData = {
    "__RequestVerificationToken": "3NC86UWUiD6IRFc_9uJDrXL77k6m-Cbix_OI-iaapfu_sCxP90WGiKKFIJDW09ZjfdJCqtsOa3Jz-H1c0VuxjsKIfjI1",
    "GameSno": gameSno,
    "KindCode": kindCode,
    "Year": year
  }

  postDataString = parse.urlencode(postData)
  postDataEncode = postDataString.encode('ascii') 

  request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
  }, method='POST', data=postDataEncode)

  with req.urlopen(request) as res:
    data = res.read().decode('utf-8')
  
  data = json.loads(data)
  data = data[dataType]

  return data



# 寫入 json 檔案
# with open("datas/curt-game-detail-json.json", mode="w") as file:
#   file.write(CurtGameDetailJson)

# with open("datas/first-sno-json.json", mode="w") as file:
#   file.write(FirstSnoJson)

# with open("datas/game-detail-json.json", mode="w") as file:
#   file.write(GameDetailJson)

# with open("datas/live-log-json.json", mode="w") as file:
#   file.write(LiveLogJson)

# with open("datas/pitching-json.json", mode="w") as file:
#   file.write(PitchingJson)

# with open("datas/scoreboard-json.json", mode="w") as file:
#   file.write(ScoreboardJson)

# with open("datas/video-json.json", mode="w") as file:
#   file.write(VideoJson)


# 所有的資料
# BattingJson = data['BattingJson']
# CurtGameDetailJson = data['CurtGameDetailJson']
# FirstSnoJson = data['FirstSnoJson']
# GameDetailJson = data['GameDetailJson']
# LiveLogJson = data['LiveLogJson']
# PitchingJson = data['PitchingJson']
# ScoreboardJson = data['ScoreboardJson']
# VideoJson = data['VideoJson']