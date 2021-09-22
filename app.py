# 使用 flask
from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 連線取得 json 檔案 (函式)
# def getData(GameSno, KindCode, Year) {
#   # ssl
#   import ssl
#   ssl._create_default_https_context = ssl._create_unverified_context
#   import urllib.request as req
#   import urllib.parse as parse
#   import json

#   url = "https://www.cpbl.com.tw/box/getlive"
#   postData = {
#     "__RequestVerificationToken": "3NC86UWUiD6IRFc_9uJDrXL77k6m-Cbix_OI-iaapfu_sCxP90WGiKKFIJDW09ZjfdJCqtsOa3Jz-H1c0VuxjsKIfjI1",
#     "GameSno": GameSno,
#     "KindCode": KindCode,
#     "Year": Year
#   }

#   postDataString = parse.urlencode(postData)
#   postDataEncode = postDataString.encode('ascii') 

#   request = req.Request(url, headers={
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
#   }, method='POST', data=postDataEncode)

#   with req.urlopen(request) as res:
#     data = res.read().decode('utf-8')

#   data = json.loads(data)
#   LiveLogJson = data['LiveLogJson']
#   ScoreboardJson = data['ScoreboardJson']

#   # 寫入 json 檔案
#   with open("datas/live-log-json.json", mode="w") as file:
#     file.write(LiveLogJson)

#   with open("datas/scoreboard-json.json", mode="w") as file:
#     file.write(ScoreboardJson)

#   # 讀取檔案
#   import json
#   with open("datas/live-log-json.json", mode="r") as file:
#     liveLogJson = json.load(file)
#   with open("datas/scoreboard-json.json", mode="r") as file:
#     scoreboardJson = json.load(file)
  
#   return {
#     liveLogJson,
#     scoreboardJson
#   }
# }

# 連線取得 json 檔案
# ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
import urllib.parse as parse
import json

url = "https://www.cpbl.com.tw/box/getlive"
postData = {
  "__RequestVerificationToken": "3NC86UWUiD6IRFc_9uJDrXL77k6m-Cbix_OI-iaapfu_sCxP90WGiKKFIJDW09ZjfdJCqtsOa3Jz-H1c0VuxjsKIfjI1",
  "GameSno": "202",
  "KindCode": "A",
  "Year": "2021"
}

postDataString = parse.urlencode(postData)
postDataEncode = postDataString.encode('ascii') 

request = req.Request(url, headers={
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}, method='POST', data=postDataEncode)

with req.urlopen(request) as res:
  data = res.read().decode('utf-8')

data = json.loads(data)
LiveLogJson = data['LiveLogJson']
ScoreboardJson = data['ScoreboardJson']

# 寫入 json 檔案
with open("datas202/live-log-json.json", mode="w") as file:
  file.write(LiveLogJson)

with open("datas202/scoreboard-json.json", mode="w") as file:
  file.write(ScoreboardJson)

# 讀取檔案(202)
import json
with open("datas202/live-log-json.json", mode="r") as file:
  liveLogJson202 = json.load(file)
with open("datas202/scoreboard-json.json", mode="r") as file:
  scoreboardJson202 = json.load(file)

# 讀取檔案(1)
with open("datas/live-log-json.json", mode="r") as file:
  liveLogJson = json.load(file)
with open("datas/scoreboard-json.json", mode="r") as file:
  scoreboardJson = json.load(file)

# 路由GameSno, KindCode, Year
@app.route("/")
def index():
  return render_template('index.html')

@app.route("/livelog")
def livelog(): 
  return jsonify(liveLogJson)

@app.route("/scoreboard")
def scoreboard(): 
  return jsonify(scoreboardJson)

@app.route("/livelog202")
def livelog202(): 
  return jsonify(liveLogJson202)

@app.route("/scoreboard202")
def scoreboard202(): 
  return jsonify(scoreboardJson202)

# run server
if __name__ == "__main__":
  app.run()