# 使用 flask
from flask import Flask, jsonify
app = Flask(__name__)

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