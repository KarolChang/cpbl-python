# 使用 flask
from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_cors import CORS
import apis.getlive
import apis.getschedule
import crawlers.standings
import json

app = Flask(__name__)
CORS(app)

# 路由
# index
@app.route("/")
def index():
  return render_template("index.html")

# page => record
@app.route("/record", methods=["POST", "GET"])
def recordIndex(): 
  if request.method == "POST":
    gameSno = request.form["gameSno"]
    kindCode = request.form["kindCode"]
    year = request.form["year"]
    dataType = request.form["dataType"]

    return redirect(url_for("record", gameSno=gameSno, kindCode=kindCode, year=year, dataType=dataType))

  else:
    return render_template("record.html")

# page => schedule
@app.route("/schedule", methods=["POST", "GET"])
def scheduleIndex(): 
  if request.method == "POST":
    year = request.form["year"]
    kindCode = request.form["kindCode"]

    return redirect(url_for("schedule", year=year, kindCode=kindCode))

  else:
    return render_template("schedule.html")

# page => standings
@app.route("/standings", methods=["POST", "GET"])
def standingsIndex(): 
  if request.method == "POST":
    return redirect(url_for("standings"))

  else:
    return render_template("standings.html")

# json data => record
@app.route("/record/<gameSno>/<kindCode>/<year>/<dataType>")
def record(gameSno, kindCode, year, dataType): 
  data = apis.getlive.fetchDatas(gameSno, kindCode, year, dataType)
  data = json.loads(data)
  return {"data": data}

# json data => schedule
@app.route("/schedule/gamedatas/<kindCode>/<year>")
def schedule(kindCode, year): 
  data = apis.getschedule.fetchDatas(kindCode, year)
  data = json.loads(data)
  return {"data": data}

# json data => standings
@app.route("/standings/datas")
def standings(): 
  data = crawlers.standings.fetchDatas()
  # data = json.loads(data)
  return {"data": data}

# run server
if __name__ == "__main__":
  app.run()