# 使用 flask
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 讀取檔案
import json
with open("datas/live-log-json.json", mode="r") as file:
  liveLogJson = json.load(file)

# 路由
@app.route("/")
def index(): 
  return jsonify(liveLogJson)

# run server
if __name__ == "__main__":
  app.run()