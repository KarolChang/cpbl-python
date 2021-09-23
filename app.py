# 使用 flask
from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_cors import CORS
import api
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

    return redirect(url_for("record", gameSno=gameSno, kindCode=kindCode, year=year, dataType=dataType))

  else:
    return render_template("index.html")


@app.route("/record/<gameSno>/<kindCode>/<year>/<dataType>")
def record(gameSno, kindCode, year, dataType): 
  data = api.fetchDatas(gameSno, kindCode, year, dataType)
  return {"data": json.loads(data)}

@app.route("/scoreboard")
def scoreboard(): 
  return jsonify(scoreboardJson)

# run server
if __name__ == "__main__":
  app.run()