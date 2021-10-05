from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
import json

import apis.getlive

record_blueprint = Blueprint('record', __name__)

# form page
@record_blueprint.route("/record", methods=["POST", "GET"])
def recordIndex(): 
  if request.method == "POST":
    gameSno = request.form["gameSno"]
    kindCode = request.form["kindCode"]
    year = request.form["year"]
    dataType = request.form["dataType"]

    return redirect(url_for("record.record", gameSno=gameSno, kindCode=kindCode, year=year, dataType=dataType))

  else:
    return render_template("record.html")

# json
@record_blueprint.route("/record/<gameSno>/<kindCode>/<year>/<dataType>")
def record(gameSno, kindCode, year, dataType): 
  data = apis.getlive.fetchDatas(gameSno, kindCode, year, dataType)
  data = json.loads(data)
  return {"data": data}