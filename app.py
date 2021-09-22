# 使用 flask
from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 讀取檔案
import json
with open("datas/live-log-json.json", mode="r") as file:
  liveLogJson = json.load(file)
with open("datas/scoreboard-json.json", mode="r") as file:
  scoreboardJson = json.load(file)

# 路由
@app.route("/")
def index():
  return render_template('index.html')

@app.route("/livelog")
def livelog(): 
  return jsonify(liveLogJson)

@app.route("/scoreboard")
def scoreboard(): 
  return jsonify(scoreboardJson)

# run server
if __name__ == "__main__":
  app.run()