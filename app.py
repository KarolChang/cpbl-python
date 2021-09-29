# 使用 flask
from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_cors import CORS
import api
import listData
import json

app = Flask(__name__)
CORS(app)

# 路由
@app.route("/", methods=["POST", "GET"])
def index():
  if request.method == "POST":
    gameSno = request.form["gameSno"]
    kindCode = request.form["kindCode"]
    year = request.form["year"]
    dataType = request.form["dataType"]
    # listScoreboard = request.form["listScoreboard"]
    # print('listScoreboard1', listScoreboard)

    return redirect(url_for("record", gameSno=gameSno, kindCode=kindCode, year=year, dataType=dataType))

  else:
    return render_template("index.html")


@app.route("/record/<gameSno>/<kindCode>/<year>/<dataType>")
def record(gameSno, kindCode, year, dataType): 
  data = api.fetchDatas(gameSno, kindCode, year, dataType) 
  data = json.loads(data)

  if(dataType == 'ScoreboardJson'):
    data = listData.listScoreboard(data)

  return {"data": data}

# @app.route("/scoreboard")
# def scoreboard(gameSno, kindCode, year): 
#   data = api.fetchDatas(gameSno, kindCode, year, 'ScoreboardJson')
#   return {"data": json.loads(data)}

# run server
if __name__ == "__main__":
  app.run()