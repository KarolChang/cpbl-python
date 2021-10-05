from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
import json

import apis.getschedule

schedule_blueprint = Blueprint('schedule', __name__)

# form page
@schedule_blueprint.route("/schedule", methods=["POST", "GET"])
def scheduleIndex(): 
  if request.method == "POST":
    year = request.form["year"]
    kindCode = request.form["kindCode"]

    return redirect(url_for("schedule.schedule", year=year, kindCode=kindCode))

  else:
    return render_template("schedule.html")

# json
@schedule_blueprint.route("/schedule/gamedatas/<kindCode>/<year>")
def schedule(kindCode, year): 
  data = apis.getschedule.fetchDatas(kindCode, year)
  data = json.loads(data)
  return {"data": data}